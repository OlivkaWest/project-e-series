"""Транскрипт со словными таймкодами -> SRT -> вшитые субтитры.

    VOICE -> TRANSCRIPT -> WORD TIMESTAMPS -> SUBTITLES -> BURN-IN / SRT

Транскрипция: faster-whisper (в разы быстрее оригинального whisper при том же
качестве). Формат SRT пишется напрямую — это 15 строк, отдельная зависимость не нужна.

    python3 pipeline/edit/add_subtitles.py --audio ep001-mix.wav --srt ep001.srt
    python3 pipeline/edit/add_subtitles.py --video ep001.mp4 --srt ep001.srt --burn out.mp4
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from _ff import require, run  # noqa: E402

# нормы из bible/TYPOGRAPHY.md
MAX_CHARS_PER_LINE = 42
MAX_LINES = 2
BOTTOM_SAFE_PCT = 20


def stamp(seconds: float) -> str:
    h, rem = divmod(max(seconds, 0.0), 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int((s % 1) * 1000):03d}"


def wrap(text: str) -> str:
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > MAX_CHARS_PER_LINE:
            lines.append(cur.strip())
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    if len(lines) > MAX_LINES:
        print(f"  ВНИМАНИЕ: {len(lines)} строк вместо {MAX_LINES} — сократи реплику")
    return "\n".join(lines[:MAX_LINES])


def transcribe(audio: str, language: str = "ru") -> list[tuple[float, float, str]]:
    from faster_whisper import WhisperModel

    model = WhisperModel("small", device="cpu", compute_type="int8")
    segments, _ = model.transcribe(audio, language=language, word_timestamps=True)
    return [(s.start, s.end, s.text.strip()) for s in segments if s.text.strip()]


def write_srt(cues: list[tuple[float, float, str]], path: str) -> None:
    blocks = []
    for i, (start, end, text) in enumerate(cues, 1):
        blocks.append(f"{i}\n{stamp(start)} --> {stamp(end)}\n{wrap(text)}\n")
    Path(path).write_text("\n".join(blocks), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audio")
    ap.add_argument("--video")
    ap.add_argument("--srt", required=True)
    ap.add_argument("--burn", help="вшить субтитры в этот выходной файл")
    ap.add_argument("--language", default="ru")
    args = ap.parse_args()

    source = args.audio or args.video
    if source:
        print(f"транскрибирую: {source}")
        cues = transcribe(source, args.language)
        write_srt(cues, args.srt)
        print(f"написано реплик: {len(cues)} -> {args.srt}")

    if args.burn:
        if not args.video:
            print("для вшивания нужен --video")
            return 1
        style = (
            "FontName=Golos Text,FontSize=22,PrimaryColour=&H00E4E2E8,"
            f"Outline=0,Shadow=0,Alignment=2,MarginV={int(1920 * BOTTOM_SAFE_PCT / 100)}"
        )
        run([
            require("ffmpeg"), "-y", "-hide_banner", "-loglevel", "error",
            "-i", args.video,
            "-vf", f"subtitles={args.srt}:force_style='{style}'",
            "-c:a", "copy", args.burn,
        ])
        print(f"вшито: {args.burn}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
