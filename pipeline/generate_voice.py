#!/usr/bin/env python3
"""Озвучка реплик эпизода через ElevenLabs по таблицам из VOICE.md.

    python pipeline/generate_voice.py 001
    python pipeline/generate_voice.py 001 --execute

Читает две таблицы VOICE.md: «Голоса» (voice_id и настройки на персонажа)
и «Реплики» (кто, что и в какой файл). Результат — mp3 в assets/voice/.
"""

from __future__ import annotations

import argparse
import json
import urllib.error
import urllib.request
from pathlib import Path

from common import ROOT, add_common_args, find_episode, load_env, log, parse_table, require_env

API = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
DEFAULT_MODEL = "eleven_multilingual_v2"
DEFAULTS = {"stability": 0.45, "similarity_boost": 0.85, "style": 0.30}


def voices(text: str) -> dict[str, dict[str, float | str]]:
    table = {}
    for row in parse_table(text, "Voice ID"):
        name = row.get("Персонаж", "").strip()
        voice_id = row.get("Voice ID", "").strip().strip("`")
        if not name or not voice_id or voice_id == "TBD":
            continue
        table[name] = {
            "voice_id": voice_id,
            "stability": _num(row.get("Stability"), DEFAULTS["stability"]),
            "similarity_boost": _num(row.get("Similarity"), DEFAULTS["similarity_boost"]),
            "style": _num(row.get("Style"), DEFAULTS["style"]),
            "speed": _num(row.get("Speed"), 1.0),
        }
    return table


def lines(text: str) -> list[dict[str, str]]:
    result = []
    for row in parse_table(text, "Текст"):
        line = row.get("Текст", "").strip().strip("«»\"")
        target = row.get("Файл", "").strip().strip("`")
        if not line or line == "TBD" or not target:
            continue
        result.append(
            {
                "shot": row.get("Шот", "").strip(),
                "character": row.get("Персонаж", "").strip(),
                "text": line,
                "delivery": row.get("Подача", "").strip(),
                "file": target,
            }
        )
    return result


def synthesize(line: dict[str, str], voice: dict, target: Path, execute: bool) -> None:
    if not execute:
        log(f"DRY-RUN elevenlabs: {line['character']} «{line['text'][:40]}…» -> {target.relative_to(ROOT)}")
        return

    payload = json.dumps(
        {
            "text": line["text"],
            "model_id": DEFAULT_MODEL,
            "voice_settings": {
                "stability": voice["stability"],
                "similarity_boost": voice["similarity_boost"],
                "style": voice["style"],
                "use_speaker_boost": True,
            },
        }
    ).encode("utf-8")

    request = urllib.request.Request(
        API.format(voice_id=voice["voice_id"]),
        data=payload,
        headers={
            "xi-api-key": require_env("ELEVENLABS_API_KEY"),
            "content-type": "application/json",
            "accept": "audio/mpeg",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            audio = response.read()
    except urllib.error.HTTPError as error:
        raise SystemExit(f"ElevenLabs {error.code}: {error.read().decode('utf-8', 'replace')[:300]}")

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(audio)
    log(f"OK {target.relative_to(ROOT)} ({len(audio) // 1024} КБ)")


def _num(value, fallback: float) -> float:
    try:
        return float(str(value).replace(",", "."))
    except (TypeError, ValueError):
        return fallback


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(parser)
    args = parser.parse_args()

    load_env()
    episode = find_episode(args.episode)
    text = episode.read("VOICE.md")
    voice_table, line_rows = voices(text), lines(text)

    if args.shot:
        line_rows = [l for l in line_rows if l["shot"] in args.shot]
    if not line_rows:
        raise SystemExit("В VOICE.md нет заполненных реплик.")

    log(f"{episode.slug}: {len(line_rows)} реплик(и)")
    for line in line_rows:
        voice = voice_table.get(line["character"])
        if not voice:
            raise SystemExit(
                f"Для персонажа {line['character']!r} не задан Voice ID в таблице «Голоса»."
            )
        target = episode.path / line["file"]
        if target.exists():
            log(f"пропуск (файл уже есть): {target.relative_to(ROOT)}")
            continue
        synthesize(line, voice, target, args.execute)


if __name__ == "__main__":
    main()
