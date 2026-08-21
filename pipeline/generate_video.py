#!/usr/bin/env python3
"""Генерация видео-шотов из PROMPTS.md эпизода (image→video и text→video).

    python pipeline/generate_video.py 001
    python pipeline/generate_video.py 001 --execute --shot sh02

Результат: season-XX/episode-XXX/renders/<code>-<shot>-vNN.mp4 + .json с параметрами.
Кейфрейм берётся из поля input_image; если файла нет — сначала generate_images.py.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from common import (
    ROOT, Shot, add_common_args, find_episode, load_env, log,
    parse_prompts, require_env, write_manifest,
)

VIDEO_TOOLS = {"seedance": "SEEDANCE_API_KEY", "kling": "KLING_API_KEY", "veo": "GEMINI_API_KEY"}
MAX_DURATION = 10.0


def next_version(folder: Path, code: str, shot: str) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    version = len(list(folder.glob(f"{code}-{shot}-v*.mp4"))) + 1
    return folder / f"{code}-{shot}-v{version:02d}.mp4"


def check(shot: Shot, episode_path: Path) -> None:
    if shot.tool not in VIDEO_TOOLS:
        raise SystemExit(f"{shot.shot}: инструмент {shot.tool!r} не для видео")
    if shot.duration and shot.duration > MAX_DURATION:
        raise SystemExit(
            f"{shot.shot}: {shot.duration}с — длиннее {MAX_DURATION}с. "
            f"Длинные планы собираем склейкой, а не одной генерацией."
        )
    if shot.input_image and not (episode_path / shot.input_image).exists():
        log(f"ВНИМАНИЕ {shot.shot}: нет кейфрейма {shot.input_image}")


def generate(shot: Shot, target: Path, execute: bool) -> None:
    if not execute:
        log(f"DRY-RUN {shot.tool}: {shot.shot} {shot.duration or '?'}с -> {target.relative_to(ROOT)}")
        return
    require_env(VIDEO_TOOLS[shot.tool])
    raise SystemExit(
        f"Адаптер {shot.tool} ещё не подключён. Реализуйте вызов API в generate() "
        f"и верните файл {target.relative_to(ROOT)}."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(parser)
    args = parser.parse_args()

    load_env()
    episode = find_episode(args.episode)
    shots = [s for s in parse_prompts(episode.read("PROMPTS.md")) if s.type != "image"]
    if args.shot:
        shots = [s for s in shots if s.shot in args.shot]
    if not shots:
        raise SystemExit("В PROMPTS.md нет видео-шотов.")

    out_dir = Path(args.out) if args.out else episode.path / "renders"
    log(f"{episode.slug}: {len(shots)} шот(ов)")

    for shot in shots:
        check(shot, episode.path)
        target = next_version(out_dir, episode.code, shot.shot)
        generate(shot, target, args.execute)
        write_manifest(
            target.with_suffix(".json"),
            {
                "episode": episode.code, "shot": shot.shot, "tool": shot.tool,
                "seed": shot.seed, "duration": shot.duration,
                "input_image": shot.input_image, "prompt": shot.prompt,
                "negative": shot.negative,
            },
            dry_run=not args.execute,
        )

    log("Не забудьте проставить статусы шотов в SHOTLIST.md")


if __name__ == "__main__":
    main()
