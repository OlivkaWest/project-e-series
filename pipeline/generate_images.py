#!/usr/bin/env python3
"""Генерация изображений (кейфреймы, референсы) из PROMPTS.md эпизода.

    python pipeline/generate_images.py 001            # dry-run: показать план
    python pipeline/generate_images.py 001 --execute  # реальные вызовы API
    python pipeline/generate_images.py 001 --shot sh01

Результат: season-XX/episode-XXX/assets/keyframes/<shot>-vNN.png + .json с параметрами.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from common import (
    ROOT, Shot, add_common_args, find_episode, load_env, log,
    parse_prompts, require_env, write_manifest,
)

IMAGE_TOOLS = {"nano-banana", "grok"}


def next_version(folder: Path, shot: str, ext: str) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    version = len(list(folder.glob(f"{shot}-v*{ext}"))) + 1
    return folder / f"{shot}-v{version:02d}{ext}"


def generate(shot: Shot, target: Path, execute: bool) -> None:
    """Диспетчер по инструментам. Адаптеры подключаются здесь."""
    if not execute:
        log(f"DRY-RUN {shot.tool}: {shot.shot} -> {target.relative_to(ROOT)} (seed={shot.seed})")
        return

    if shot.tool == "nano-banana":
        require_env("GEMINI_API_KEY")
    elif shot.tool == "grok":
        require_env("XAI_API_KEY")
    else:
        raise SystemExit(f"{shot.shot}: инструмент {shot.tool!r} не для изображений")

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
    shots = [s for s in parse_prompts(episode.read("PROMPTS.md")) if s.type == "image" or s.tool in IMAGE_TOOLS]
    if args.shot:
        shots = [s for s in shots if s.shot in args.shot]
    if not shots:
        raise SystemExit("В PROMPTS.md нет подходящих блоков (нужен type: image).")

    out_dir = Path(args.out) if args.out else episode.path / "assets" / "keyframes"
    log(f"{episode.slug}: {len(shots)} изображени(й)")

    for shot in shots:
        target = next_version(out_dir, shot.shot, ".png")
        generate(shot, target, args.execute)
        write_manifest(
            target.with_suffix(".json"),
            {
                "episode": episode.code, "shot": shot.shot, "tool": shot.tool,
                "seed": shot.seed, "prompt": shot.prompt, "negative": shot.negative,
            },
            dry_run=not args.execute,
        )


if __name__ == "__main__":
    main()
