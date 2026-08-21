"""Экспорт мастера под площадки.

    python3 pipeline/edit/export_short.py --season 1 --episode 1 --platform shorts --execute
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from _common import ROOT, episode_dir  # noqa: E402
from _ff import MASTER, require, run  # noqa: E402

PLATFORMS = {
    "shorts":   {"crf": 18, "max_mb": None, "dir": "shorts"},
    "reels":    {"crf": 18, "max_mb": None, "dir": "reels"},
    "telegram": {"crf": 21, "max_mb": 50,   "dir": "telegram"},
    "youtube":  {"crf": 16, "max_mb": None, "dir": "youtube"},
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", type=int, default=1)
    ap.add_argument("--episode", type=int, required=True)
    ap.add_argument("--platform", choices=sorted(PLATFORMS), required=True)
    ap.add_argument("--execute", action="store_true")
    args = ap.parse_args()

    cfg = PLATFORMS[args.platform]
    ep = episode_dir(args.season, args.episode)
    src = ep / "renders" / f"ep{args.episode:03d}-final.mp4"
    dst = ROOT / "output" / cfg["dir"] / f"ep{args.episode:03d}.mp4"

    print(f"площадка: {args.platform}")
    print(f"источник: {src.relative_to(ROOT)} — {'найден' if src.exists() else 'ОТСУТСТВУЕТ'}")
    print(f"мастер:   {MASTER['width']}x{MASTER['height']}, {MASTER['fps']} fps, CRF {cfg['crf']}")
    if cfg["max_mb"]:
        print(f"лимит:    {cfg['max_mb']} МБ")

    if not args.execute:
        print("\nрежим плана. Для экспорта добавь --execute")
        return 0
    if not src.exists():
        return 1

    dst.parent.mkdir(parents=True, exist_ok=True)
    run([
        require("ffmpeg"), "-y", "-hide_banner", "-loglevel", "error",
        "-i", str(src),
        "-c:v", MASTER["vcodec"], "-pix_fmt", MASTER["pix_fmt"],
        "-crf", str(cfg["crf"]), "-preset", "slow",
        "-r", str(MASTER["fps"]),
        "-c:a", MASTER["acodec"], "-b:a", "192k", "-ar", str(MASTER["sample_rate"]),
        "-movflags", "+faststart", str(dst),
    ])
    size_mb = dst.stat().st_size / 1_048_576
    print(f"\nэкспортировано: {dst.relative_to(ROOT)} — {size_mb:.1f} МБ")
    if cfg["max_mb"] and size_mb > cfg["max_mb"]:
        print(f"ПРЕВЫШЕН ЛИМИТ площадки на {size_mb - cfg['max_mb']:.1f} МБ — подними CRF")
        return 1
    print("дальше: validate_render.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
