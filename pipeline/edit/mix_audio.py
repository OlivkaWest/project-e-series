"""Сведение звуковых слоёв эпизода: речь, музыка, SFX, ambience.

Уровни берутся из bible/SOUND_LANGUAGE.md и не выдумываются на месте.

    python3 pipeline/edit/mix_audio.py --season 1 --episode 1 --execute
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from _common import ROOT, episode_dir  # noqa: E402
from _ff import require, run  # noqa: E402

# уровни в dB относительно исходного, соответствуют нормам библии
LAYERS = {
    "voice": 0.0,
    "sfx": -4.0,
    "music": -8.0,
    "ambience": -14.0,
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", type=int, default=1)
    ap.add_argument("--episode", type=int, required=True)
    ap.add_argument("--execute", action="store_true")
    args = ap.parse_args()

    ep = episode_dir(args.season, args.episode)
    found = {}
    for layer in LAYERS:
        files = sorted((ep / "assets").glob(f"*{layer}*.wav"))
        if files:
            found[layer] = files

    print(f"эпизод {args.episode:03d}: слоёв найдено {len(found)} из {len(LAYERS)}")
    for layer, files in found.items():
        print(f"  {layer:10} {LAYERS[layer]:+5.1f} dB   файлов: {len(files)}")
    for layer in LAYERS:
        if layer not in found:
            print(f"  {layer:10} ОТСУТСТВУЕТ")

    if not args.execute:
        print("\nрежим плана. Для сведения добавь --execute")
        return 0
    if not found:
        print("нечего сводить")
        return 1

    inputs, filters = [], []
    for i, (layer, files) in enumerate(found.items()):
        inputs += ["-i", str(files[0])]
        filters.append(f"[{i}:a]volume={LAYERS[layer]}dB[a{i}]")
    mix = "".join(f"[a{i}]" for i in range(len(found)))
    graph = ";".join(filters) + f";{mix}amix=inputs={len(found)}:duration=longest:normalize=0[out]"

    out = ep / "renders" / f"ep{args.episode:03d}-mix.wav"
    out.parent.mkdir(parents=True, exist_ok=True)
    run([
        require("ffmpeg"), "-y", "-hide_banner", "-loglevel", "error",
        *inputs, "-filter_complex", graph, "-map", "[out]",
        "-ar", "48000", "-ac", "2", str(out),
    ])
    print(f"\nсведено: {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
