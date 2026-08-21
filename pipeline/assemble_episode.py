#!/usr/bin/env python3
"""Сборка эпизода из отрендеренных шотов по таблице тайм-лайна в EDIT.md.

    python pipeline/assemble_episode.py 001                 # dry-run: показать команды ffmpeg
    python pipeline/assemble_episode.py 001 --execute
    python pipeline/assemble_episode.py 001 --execute --burn-subs

Шаги: нарезка шотов по In/Out -> конкат -> подмешивание музыки -> нормализация -14 LUFS
-> (опционально) вжигание субтитров -> output/shorts/<code>.mp4.
"""

from __future__ import annotations

import argparse
import shutil
import tempfile
from pathlib import Path

from common import ROOT, ffmpeg, find_episode, load_env, log, parse_table

WIDTH, HEIGHT, FPS = 1080, 1920, 30
SCALE = f"scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=increase,crop={WIDTH}:{HEIGHT},fps={FPS}"
LOUDNESS = "loudnorm=I=-14:TP=-1:LRA=11"


def timeline(episode) -> list[dict[str, str]]:
    rows = parse_table(episode.read("EDIT.md"), "Переход")
    clips = []
    for row in rows:
        source = row.get("Файл", "").strip().strip("`")
        if not source or source == "TBD":
            continue
        path = episode.path / source
        if not path.exists():
            raise SystemExit(f"Нет файла шота: {path.relative_to(ROOT)} (сначала generate_video.py)")
        clips.append({"shot": row.get("Шот", ""), "path": path, "in": row.get("In", "0"), "out": row.get("Out", "")})
    return clips


def music_track(episode) -> Path | None:
    for row in parse_table(episode.read("MUSIC.md"), "Параметр"):
        if row.get("Параметр", "").strip() == "Файл":
            candidate = episode.path / row.get("Значение", "").strip().strip("`")
            return candidate if candidate.exists() else None
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("episode", help="номер эпизода (1, 001) или путь к папке")
    parser.add_argument("--execute", action="store_true", help="реально запускать ffmpeg")
    parser.add_argument("--burn-subs", action="store_true", help="вжечь субтитры из assets/subs/<code>.srt")
    parser.add_argument("--out", help="путь итогового файла")
    args = parser.parse_args()

    load_env()
    episode = find_episode(args.episode)
    clips = timeline(episode)
    if not clips:
        raise SystemExit("В EDIT.md не заполнен тайм-лайн.")

    target = Path(args.out) if args.out else ROOT / "output" / "shorts" / f"{episode.code}.mp4"
    target.parent.mkdir(parents=True, exist_ok=True)
    dry = not args.execute
    log(f"{episode.slug}: {len(clips)} клип(ов) -> {target.relative_to(ROOT)}")

    workdir = Path(tempfile.mkdtemp(prefix=f"{episode.code}-"))
    try:
        pieces = []
        for index, clip in enumerate(clips, start=1):
            piece = workdir / f"{index:03d}-{clip['shot'] or 'clip'}.mp4"
            trim = ["-ss", str(clip["in"] or 0)]
            if clip["out"]:
                trim += ["-to", str(clip["out"])]
            ffmpeg([*trim, "-i", str(clip["path"]), "-vf", SCALE,
                    "-c:v", "libx264", "-crf", "18", "-preset", "medium",
                    "-c:a", "aac", "-ar", "48000", str(piece)], dry)
            pieces.append(piece)

        listing = workdir / "concat.txt"
        if not dry:
            listing.write_text("".join(f"file '{p}'\n" for p in pieces), encoding="utf-8")
        cut = workdir / "cut.mp4"
        ffmpeg(["-f", "concat", "-safe", "0", "-i", str(listing), "-c", "copy", str(cut)], dry)

        stage = cut
        music = music_track(episode)
        if music:
            mixed = workdir / "mixed.mp4"
            ffmpeg(["-i", str(stage), "-i", str(music),
                    "-filter_complex", "[1:a]volume=-12dB[m];[0:a][m]amix=inputs=2:duration=first:dropout_transition=0[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", str(mixed)], dry)
            stage = mixed
        else:
            log("музыка не найдена — собираю без неё")

        video_filters = [SCALE]
        subs = episode.path / "assets" / "subs" / f"{episode.code}.srt"
        if args.burn_subs:
            if not subs.exists() and not dry:
                raise SystemExit(f"Нет субтитров: {subs.relative_to(ROOT)}")
            video_filters.append(f"subtitles='{subs}'")

        ffmpeg(["-i", str(stage), "-vf", ",".join(video_filters), "-af", LOUDNESS,
                "-c:v", "libx264", "-crf", "18", "-preset", "slow", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(target)], dry)
    finally:
        shutil.rmtree(workdir, ignore_errors=True)

    log("Готово. Дальше: pipeline/publish.py")


if __name__ == "__main__":
    main()
