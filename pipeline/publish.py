"""Публикация готового эпизода.

Собирает метаданные (заголовок, описание, теги, обложка) и проверяет,
что мастер-файлы лежат в output/. Выгрузка на площадки подключается отдельно.

Пример: python pipeline/publish.py --season 1 --episode 1 --platform shorts
"""

from __future__ import annotations

import argparse

from _common import ROOT

PLATFORMS = ("shorts", "youtube", "reels", "telegram")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", type=int, default=1)
    ap.add_argument("--episode", type=int, required=True)
    ap.add_argument("--platform", choices=PLATFORMS, required=True)
    ap.add_argument("--execute", action="store_true")
    args = ap.parse_args()

    master = ROOT / "output" / args.platform / f"ep{args.episode:03d}.mp4"
    print(f"площадка: {args.platform}")
    print(f"мастер:   {master} — {'найден' if master.exists() else 'ОТСУТСТВУЕТ'}")
    if args.execute:
        raise SystemExit("выгрузка на площадки ещё не подключена")


if __name__ == "__main__":
    main()
