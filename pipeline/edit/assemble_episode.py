"""Сборка эпизода по таблице таймлайна из EDIT.md.

Каждый клип приводится к мастер-формату проекта (1080x1920, 30 fps) и режется
по длительности из таблицы. Переходы — только hard cut: это правило сериала,
а не ограничение скрипта.

    python3 pipeline/edit/assemble_episode.py --season 1 --episode 1
    python3 pipeline/edit/assemble_episode.py --season 1 --episode 1 --execute
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from _common import ROOT, episode_dir, parse_table, read_doc  # noqa: E402
from _ff import MASTER, require, run  # noqa: E402

TIME = re.compile(r"(\d+):(\d+)[,.](\d+)|(\d+):(\d+)")


def to_seconds(value: str) -> float:
    value = value.strip().replace(" ", "")
    m = TIME.fullmatch(value)
    if not m:
        raise ValueError(f"не разобрать таймкод: {value!r}")
    if m.group(1) is not None:
        return int(m.group(1)) * 60 + int(m.group(2)) + float(f"0.{m.group(3)}")
    return int(m.group(4)) * 60 + int(m.group(5))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", type=int, default=1)
    ap.add_argument("--episode", type=int, required=True)
    ap.add_argument("--execute", action="store_true", help="реально собрать файл")
    args = ap.parse_args()

    ep = episode_dir(args.season, args.episode)
    rows = [r for r in parse_table(read_doc(args.season, args.episode, "EDIT.md")) if r.get("Клип")]
    if not rows:
        print("таймлайн пуст — нечего собирать")
        return 1

    plan, missing, total = [], [], 0.0
    for row in rows:
        clip = row.get("Клип", "").strip("`").strip()
        if not clip or clip.startswith("чёрный"):
            continue
        src = ep / clip
        if not src.exists():
            src = ep / "renders" / Path(clip).name
        dur = to_seconds(row["Аут"]) - to_seconds(row["Ин"])
        total += dur
        (plan if src.exists() else missing).append((src, dur))

    print(f"эпизод {args.episode:03d}: клипов {len(rows)}, найдено {len(plan)}, нет {len(missing)}")
    print(f"расчётная длительность: {total:.1f} сек")
    print(f"мастер: {MASTER['width']}x{MASTER['height']}, {MASTER['fps']} fps")
    for src, dur in missing:
        print(f"  ОТСУТСТВУЕТ  {src.relative_to(ROOT)}  ({dur:.1f} c)")

    if not args.execute:
        print("\nрежим плана. Для сборки добавь --execute")
        return 0
    if missing:
        print("\nсборка невозможна: не все клипы на месте")
        return 1

    work = ep / "renders" / "_norm"
    work.mkdir(parents=True, exist_ok=True)
    parts = []
    for i, (src, dur) in enumerate(plan):
        dst = work / f"{i:02d}.mp4"
        run([
            require("ffmpeg"), "-y", "-hide_banner", "-loglevel", "error",
            "-i", str(src), "-t", f"{dur:.3f}",
            "-vf", (
                f"scale={MASTER['width']}:{MASTER['height']}:force_original_aspect_ratio=increase,"
                f"crop={MASTER['width']}:{MASTER['height']},fps={MASTER['fps']}"
            ),
            "-c:v", MASTER["vcodec"], "-pix_fmt", MASTER["pix_fmt"],
            "-crf", "16", "-preset", "slow", "-an", str(dst),
        ])
        parts.append(dst)

    listing = work / "concat.txt"
    listing.write_text("".join(f"file '{p.name}'\n" for p in parts), encoding="utf-8")
    out = ep / "renders" / f"ep{args.episode:03d}-video.mp4"
    run([
        require("ffmpeg"), "-y", "-hide_banner", "-loglevel", "error",
        "-f", "concat", "-safe", "0", "-i", str(listing),
        "-c", "copy", str(out),
    ])
    print(f"\nсобрано: {out.relative_to(ROOT)}")
    print("дальше: mix_audio.py → normalize_audio.py → add_subtitles.py → export_short.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
