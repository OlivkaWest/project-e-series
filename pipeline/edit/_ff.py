"""Общие утилиты FFmpeg для монтажного блока."""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path
from typing import Any

MASTER = {
    "width": 1080,
    "height": 1920,
    "fps": 30,
    "vcodec": "libx264",
    "pix_fmt": "yuv420p",
    "acodec": "aac",
    "sample_rate": 48000,
    "lufs": -14.0,
    "true_peak": -1.0,
}


def require(binary: str) -> str:
    path = shutil.which(binary)
    if not path:
        raise RuntimeError(
            f"{binary} не найден. macOS: brew install ffmpeg. Linux: apt install ffmpeg"
        )
    return path


def run(args: list[str], capture: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(args, check=True, capture_output=capture, text=True)


def probe(path: str | Path) -> dict[str, Any]:
    """Полные метаданные файла через ffprobe."""
    out = run(
        [
            require("ffprobe"), "-v", "error",
            "-print_format", "json",
            "-show_format", "-show_streams",
            str(path),
        ],
        capture=True,
    ).stdout
    return json.loads(out)


def video_stream(meta: dict[str, Any]) -> dict[str, Any] | None:
    for s in meta.get("streams", []):
        if s.get("codec_type") == "video":
            return s
    return None


def audio_stream(meta: dict[str, Any]) -> dict[str, Any] | None:
    for s in meta.get("streams", []):
        if s.get("codec_type") == "audio":
            return s
    return None


def fps_of(stream: dict[str, Any]) -> float:
    raw = stream.get("r_frame_rate", "0/1")
    num, _, den = raw.partition("/")
    try:
        return float(num) / float(den or 1)
    except ZeroDivisionError:
        return 0.0


def measure_loudness(path: str | Path) -> dict[str, float]:
    """Первый проход loudnorm: измерение без изменения файла."""
    proc = subprocess.run(
        [
            require("ffmpeg"), "-hide_banner", "-nostats", "-i", str(path),
            "-af", "loudnorm=I=-14:TP=-1:LRA=11:print_format=json",
            "-f", "null", "-",
        ],
        capture_output=True, text=True,
    )
    tail = proc.stderr[proc.stderr.rfind("{"): proc.stderr.rfind("}") + 1]
    if not tail:
        raise RuntimeError("loudnorm не вернул измерение")
    data = json.loads(tail)
    return {k: float(v) for k, v in data.items() if _is_number(v)}


def _is_number(value: str) -> bool:
    try:
        float(value)
        return True
    except (TypeError, ValueError):
        return False
