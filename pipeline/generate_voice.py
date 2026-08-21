"""Синтез реплик эпизода.

Читает VOICE.md, печатает список реплик с настройками голоса.
Подключение ElevenLabs — после утверждения пилота.

Пример: python pipeline/generate_voice.py --season 1 --episode 1
"""

from __future__ import annotations

import argparse

from _common import parse_table, read_doc


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", type=int, default=1)
    ap.add_argument("--episode", type=int, required=True)
    ap.add_argument("--execute", action="store_true")
    args = ap.parse_args()

    lines = parse_table(read_doc(args.season, args.episode, "VOICE.md"))
    print(f"реплик к синтезу: {len(lines)}")
    for line in lines:
        print(f"  {line.get('Реплика', '?')}: {line.get('Персонаж', '?')} — {line.get('Текст', '')[:60]}")
    if args.execute:
        raise SystemExit("синтез речи ещё не подключён (CHECKPOINT 9)")


if __name__ == "__main__":
    main()
