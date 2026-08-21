"""Нормализация громкости до мастер-нормы проекта: -14 LUFS, пики <= -1 dBTP.

Двухпроходный loudnorm: сначала измерение, потом применение с измеренными
значениями. Однопроходный вариант даёт заметно худший результат на коротких файлах.

    python3 pipeline/edit/normalize_audio.py input.wav output.wav
    python3 pipeline/edit/normalize_audio.py input.mp4 --measure-only
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from _ff import MASTER, measure_loudness, require, run  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst", nargs="?")
    ap.add_argument("--measure-only", action="store_true")
    args = ap.parse_args()

    m = measure_loudness(args.src)
    print(f"измерено: {m.get('input_i')} LUFS, TP {m.get('input_tp')} dBTP, LRA {m.get('input_lra')}")
    print(f"норма:    {MASTER['lufs']} LUFS, TP {MASTER['true_peak']} dBTP")

    if args.measure_only or not args.dst:
        delta = abs(float(m.get("input_i", 0)) - MASTER["lufs"])
        print("вердикт:", "В НОРМЕ" if delta < 1.0 else f"ОТКЛОНЕНИЕ {delta:.1f} LU")
        return 0

    af = (
        f"loudnorm=I={MASTER['lufs']}:TP={MASTER['true_peak']}:LRA=11:"
        f"measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
        f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:"
        f"offset={m.get('target_offset', 0)}:linear=true:print_format=summary"
    )
    run([
        require("ffmpeg"), "-y", "-hide_banner", "-loglevel", "error",
        "-i", args.src, "-af", af, "-ar", "48000", args.dst,
    ])
    print(f"готово: {args.dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
