"""Image-to-video по шот-листу эпизода.

Читает SHOTLIST.md, сверяет наличие входных master frames и печатает план генерации.
Вызовы Seedance/Kling/Veo подключаются после утверждения пилота.

Пример: python pipeline/generate_video.py --season 1 --episode 1
"""

from __future__ import annotations

import argparse

from _common import episode_dir, parse_table, read_doc


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", type=int, default=1)
    ap.add_argument("--episode", type=int, required=True)
    ap.add_argument("--execute", action="store_true")
    args = ap.parse_args()

    shots = parse_table(read_doc(args.season, args.episode, "SHOTLIST.md"))
    renders = episode_dir(args.season, args.episode) / "renders"

    print(f"шотов в листе: {len(shots)}")
    for shot in shots:
        shot_id = shot.get("Шот", "?")
        tool = shot.get("Инструмент", "seedance")
        print(f"  {shot_id}: {tool}, {shot.get('Длит.', '?')} c → {renders.name}/")
    if args.execute:
        raise SystemExit("генерация видео ещё не подключена (CHECKPOINT 9)")


if __name__ == "__main__":
    main()
