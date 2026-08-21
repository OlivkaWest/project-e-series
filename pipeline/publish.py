#!/usr/bin/env python3
"""Подготовка и публикация мастера эпизода по площадкам.

    python pipeline/publish.py 001                              # dry-run
    python pipeline/publish.py 001 --execute --target telegram
    python pipeline/publish.py 001 --execute --target all

Берёт output/shorts/<code>.mp4, делает деривативы под площадки и публикует там,
где подключён адаптер. Реализован Telegram (Bot API); YouTube/Reels — заготовки.
"""

from __future__ import annotations

import argparse
import mimetypes
import urllib.request
import uuid
from pathlib import Path

from common import ROOT, ffmpeg, find_episode, load_env, log, require_env

TARGETS = {
    "shorts": {"size": (1080, 1920)},
    "reels": {"size": (1080, 1920)},
    "telegram": {"size": (1080, 1920)},
    "youtube": {"size": (1920, 1080)},
}
TELEGRAM_LIMIT_MB = 50


def derive(master: Path, name: str, code: str, dry: bool) -> Path:
    width, height = TARGETS[name]["size"]
    target = ROOT / "output" / name / f"{code}.mp4"
    target.parent.mkdir(parents=True, exist_ok=True)
    if target == master:
        return target
    vf = (f"scale={width}:{height}:force_original_aspect_ratio=decrease,"
          f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:color=black")
    ffmpeg(["-i", str(master), "-vf", vf, "-c:v", "libx264", "-crf", "19",
            "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "copy",
            "-movflags", "+faststart", str(target)], dry)
    return target


def publish_telegram(video: Path, code: str, dry: bool) -> None:
    if not dry and video.stat().st_size > TELEGRAM_LIMIT_MB * 1024 * 1024:
        raise SystemExit(f"{video.name}: больше {TELEGRAM_LIMIT_MB} МБ — пережмите перед отправкой.")
    if dry:
        log(f"DRY-RUN telegram: отправил бы {video.relative_to(ROOT)}")
        return

    token = require_env("TELEGRAM_BOT_TOKEN")
    chat_id = require_env("TELEGRAM_CHAT_ID")
    boundary = uuid.uuid4().hex
    mime = mimetypes.guess_type(video.name)[0] or "video/mp4"
    body = b"".join([
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"chat_id\"\r\n\r\n{chat_id}\r\n".encode(),
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"caption\"\r\n\r\n{code}\r\n".encode(),
        f"--{boundary}\r\nContent-Disposition: form-data; name=\"video\"; filename=\"{video.name}\"\r\n"
        f"Content-Type: {mime}\r\n\r\n".encode(),
        video.read_bytes(),
        f"\r\n--{boundary}--\r\n".encode(),
    ])
    request = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/sendVideo",
        data=body,
        headers={"content-type": f"multipart/form-data; boundary={boundary}"},
    )
    with urllib.request.urlopen(request, timeout=300) as response:
        log(f"telegram: {response.status}")


def publish_stub(name: str, video: Path, dry: bool) -> None:
    log(f"{'DRY-RUN ' if dry else ''}{name}: файл готов — {video.relative_to(ROOT)}")
    if not dry:
        log(f"Адаптер {name} не подключён: загрузите файл вручную или реализуйте publish_{name}().")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("episode", help="номер эпизода (1, 001) или путь к папке")
    parser.add_argument("--target", action="append", default=[],
                        help=f"площадка: {', '.join(TARGETS)} или all (по умолчанию all)")
    parser.add_argument("--execute", action="store_true", help="реально жать и публиковать")
    args = parser.parse_args()

    load_env()
    episode = find_episode(args.episode)
    dry = not args.execute

    master = ROOT / "output" / "shorts" / f"{episode.code}.mp4"
    if not master.exists() and not dry:
        raise SystemExit(f"Нет мастера {master.relative_to(ROOT)} — сначала assemble_episode.py")

    names = list(TARGETS) if not args.target or "all" in args.target else args.target
    unknown = [n for n in names if n not in TARGETS]
    if unknown:
        raise SystemExit(f"Неизвестные площадки: {unknown}")

    for name in names:
        video = derive(master, name, episode.code, dry)
        if name == "telegram":
            publish_telegram(video, episode.code, dry)
        else:
            publish_stub(name, video, dry)

    log("Запишите ссылки в output/README.md и метрики в research/viral-formats.md")


if __name__ == "__main__":
    main()
