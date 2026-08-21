"""Master frames эпизода.

Читает PROMPTS.md эпизода, показывает план генерации и складывает результат
в season-XX/episode-XXX/assets/. Вызов генеративного API подключается после
утверждения пилота — сейчас скрипт работает в режиме плана (--dry-run по умолчанию).

Пример: python pipeline/generate_images.py --season 1 --episode 1
"""

from __future__ import annotations

import argparse

from _common import episode_dir, read_doc


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", type=int, default=1)
    ap.add_argument("--episode", type=int, required=True)
    ap.add_argument("--execute", action="store_true", help="реально вызывать API")
    args = ap.parse_args()

    doc = read_doc(args.season, args.episode, "PROMPTS.md")
    blocks = [b for b in doc.split("\n## ") if "```" in b]
    out = episode_dir(args.season, args.episode) / "assets"

    print(f"эпизод {args.episode:03d}: найдено промпт-блоков — {len(blocks)}")
    print(f"каталог результата: {out}")
    for block in blocks:
        print("  -", block.splitlines()[0].strip())
    if args.execute:
        raise SystemExit("генерация изображений ещё не подключена (CHECKPOINT 9)")


if __name__ == "__main__":
    main()
