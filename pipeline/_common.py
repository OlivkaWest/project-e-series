"""Общие утилиты пайплайна: пути эпизодов и чтение проектных документов."""

from __future__ import annotations

import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def episode_dir(season: int, episode: int) -> Path:
    return ROOT / f"season-{season:02d}" / f"episode-{episode:03d}"


def read_doc(season: int, episode: int, name: str) -> str:
    path = episode_dir(season, episode) / name
    if not path.exists():
        raise FileNotFoundError(f"нет документа {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def parse_table(markdown: str) -> list[dict]:
    """Разбирает первую markdown-таблицу документа в список словарей."""
    rows = [ln.strip() for ln in markdown.splitlines() if ln.strip().startswith("|")]
    if len(rows) < 2:
        return []
    header = [c.strip() for c in rows[0].strip("|").split("|")]
    out = []
    for line in rows[2:]:
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != len(header):
            continue
        out.append(dict(zip(header, cells)))
    return out


def require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"не задана переменная окружения {name} (см. .env.example)")
    return value


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
