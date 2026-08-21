"""Сборка эпизода по EDIT.md.

Читает таймлайн, проверяет наличие всех клипов и печатает команду сборки.
Реальная склейка (ffmpeg) подключается после утверждения пилота.

Пример: python pipeline/assemble_episode.py --season 1 --episode 1
"""

from __future__ import annotations

import argparse

from _common import ROOT, parse_table, read_doc


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", type=int, default=1)
    ap.add_argument("--episode", type=int, required=True)
    ap.add_argument("--execute", action="store_true")
    args = ap.parse_args()

    timeline = parse_table(read_doc(args.season, args.episode, "EDIT.md"))
    missing = []
    for row in timeline:
        clip = row.get("Клип", "").strip("`")
        if clip and not (ROOT / f"season-{args.season:02d}" / f"episode-{args.episode:03d}" / clip).exists():
            missing.append(clip)

    print(f"позиций в таймлайне: {len(timeline)}")
    if missing:
        print("отсутствуют клипы:")
        for clip in missing:
            print("  -", clip)
    else:
        print("все клипы на месте")
    if args.execute:
        raise SystemExit("сборка ffmpeg ещё не подключена (CHECKPOINT 9)")


if __name__ == "__main__":
    main()
