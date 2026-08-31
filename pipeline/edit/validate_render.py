"""Технический контроль готового файла против норм проекта.

Возвращает ненулевой код при любом отклонении — удобно вешать в CI.

    python3 pipeline/edit/validate_render.py output/shorts/ep001.mp4
    python3 pipeline/edit/validate_render.py --selftest
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from _ff import (MASTER, audio_stream, fps_of, measure_loudness,  # noqa: E402
                 probe, require, video_stream)

DUR_MIN, DUR_MAX = 55.0, 95.0


def check(name: str, actual, expected, ok: bool) -> tuple[str, str, str, bool]:
    return (name, str(actual), str(expected), ok)


def validate(path: str) -> int:
    meta = probe(path)
    v, a = video_stream(meta), audio_stream(meta)
    rows = []

    if not v:
        print("видеопоток отсутствует")
        return 1

    w, h = int(v["width"]), int(v["height"])
    fps = fps_of(v)
    dur = float(meta["format"]["duration"])
    size_mb = int(meta["format"]["size"]) / 1_048_576

    rows.append(check("разрешение", f"{w}x{h}", f"{MASTER['width']}x{MASTER['height']}",
                      (w, h) == (MASTER["width"], MASTER["height"])))
    rows.append(check("соотношение", f"{w}:{h}", "9:16", abs(w / h - 9 / 16) < 0.01))
    rows.append(check("fps", f"{fps:.2f}", MASTER["fps"], abs(fps - MASTER["fps"]) < 0.05))
    rows.append(check("кодек", v.get("codec_name"), "h264", v.get("codec_name") == "h264"))
    rows.append(check("pix_fmt", v.get("pix_fmt"), MASTER["pix_fmt"], v.get("pix_fmt") == MASTER["pix_fmt"]))
    rows.append(check("длительность", f"{dur:.1f} c", f"{DUR_MIN}-{DUR_MAX} c", DUR_MIN <= dur <= DUR_MAX))
    rows.append(check("размер", f"{size_mb:.1f} МБ", "информативно", True))

    if a:
        sr = int(a.get("sample_rate", 0))
        rows.append(check("аудиокодек", a.get("codec_name"), "aac", a.get("codec_name") == "aac"))
        rows.append(check("частота", sr, MASTER["sample_rate"], sr == MASTER["sample_rate"]))
        try:
            m = measure_loudness(path)
            lufs, tp = float(m["input_i"]), float(m["input_tp"])
            rows.append(check("громкость", f"{lufs:.1f} LUFS", f"{MASTER['lufs']} LUFS",
                              abs(lufs - MASTER["lufs"]) < 1.0))
            rows.append(check("истинный пик", f"{tp:.1f} dBTP", f"<= {MASTER['true_peak']}",
                              tp <= MASTER["true_peak"] + 0.1))
        except Exception as exc:  # noqa: BLE001
            rows.append(check("громкость", f"не измерена: {exc}", "-14 LUFS", False))
    else:
        rows.append(check("аудиопоток", "отсутствует", "есть", False))

    width = max(len(r[0]) for r in rows) + 2
    print(f"{'параметр'.ljust(width)}{'факт'.ljust(22)}{'норма'.ljust(20)}вердикт")
    print("-" * (width + 50))
    failed = 0
    for name, actual, expected, ok in rows:
        mark = "OK" if ok else "ОТКЛОНЕНИЕ"
        failed += 0 if ok else 1
        print(f"{name.ljust(width)}{actual.ljust(22)}{expected.ljust(20)}{mark}")
    print("-" * (width + 50))
    print(f"проверок: {len(rows)}, отклонений: {failed}")
    print("ВЕРДИКТ:", "ГОДЕН К ПУБЛИКАЦИИ" if failed == 0 else "ДОРАБОТКА")
    return 0 if failed == 0 else 1


def selftest() -> int:
    """Проверяет, что окружение готово: бинарники на месте, ffprobe работает."""
    print("самопроверка окружения")
    for binary in ("ffmpeg", "ffprobe"):
        print(f"  {binary}: {require(binary)}")
    tmp = Path("/tmp/_ff_selftest.mp4")
    from _ff import run
    run([
        require("ffmpeg"), "-y", "-hide_banner", "-loglevel", "error",
        "-f", "lavfi", "-i", f"color=c=black:s={MASTER['width']}x{MASTER['height']}:d=1:r={MASTER['fps']}",
        "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo", "-shortest",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", str(tmp),
    ])
    meta = probe(tmp)
    v = video_stream(meta)
    ok = v and int(v["width"]) == MASTER["width"] and abs(fps_of(v) - MASTER["fps"]) < 0.05
    tmp.unlink(missing_ok=True)
    print("  тестовый рендер и ffprobe:", "OK" if ok else "ОШИБКА")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("path", nargs="?")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if not args.path:
        ap.error("нужен путь к файлу или --selftest")
    return validate(args.path)


if __name__ == "__main__":
    raise SystemExit(main())
