"""Общие утилиты пайплайна: пути, парсинг документов эпизода, вызов ffmpeg.

Все скрипты пайплайна по умолчанию работают в режиме --dry-run:
ничего не генерируют и не тратят кредиты, только показывают, что бы сделали.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parent.parent
SEASONS = sorted(p for p in ROOT.glob("season-*") if p.is_dir())

YAML_BLOCK = re.compile(r"```yaml\s*\n(.*?)```", re.DOTALL)
PLACEHOLDER = re.compile(r"^(TBD|—|-)?$")


# --------------------------------------------------------------------------- env


def load_env(path: Path | None = None) -> dict[str, str]:
    """Читает .env в os.environ (существующие переменные не перетирает)."""
    path = path or ROOT / ".env"
    if not path.exists():
        return {}
    loaded: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip().strip('"').strip("'")
        loaded[key] = value
        os.environ.setdefault(key, value)
    return loaded


def require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise SystemExit(
            f"Не задан {name}. Скопируйте .env.example в .env и заполните ключ, "
            f"или запускайте с --dry-run."
        )
    return value


# ------------------------------------------------------------------------ episode


@dataclass
class Episode:
    path: Path

    @property
    def slug(self) -> str:            # episode-001
        return self.path.name

    @property
    def code(self) -> str:            # ep001
        return "ep" + self.slug.split("-")[-1]

    def doc(self, name: str) -> Path:
        return self.path / name

    def read(self, name: str) -> str:
        f = self.doc(name)
        if not f.exists():
            raise SystemExit(f"Нет файла {f.relative_to(ROOT)}")
        return f.read_text(encoding="utf-8")


def find_episode(ref: str) -> Episode:
    """Принимает '1', '001', 'episode-001' или путь."""
    candidate = Path(ref)
    if candidate.is_dir():
        return Episode(candidate.resolve())
    num = re.sub(r"\D", "", ref)
    if not num:
        raise SystemExit(f"Не понял эпизод: {ref!r}")
    name = f"episode-{int(num):03d}"
    for season in SEASONS:
        if (season / name).is_dir():
            return Episode(season / name)
    raise SystemExit(f"Эпизод {name} не найден в {[s.name for s in SEASONS]}")


# ------------------------------------------------------------------------- parsing


@dataclass
class Shot:
    shot: str
    tool: str
    type: str = "video"
    prompt: str = ""
    negative: str = ""
    seed: int | None = None
    duration: float | None = None
    input_image: str | None = None
    extra: dict[str, Any] = field(default_factory=dict)


def parse_prompts(text: str) -> list[Shot]:
    """Достаёт ```yaml блоки из PROMPTS.md эпизода.

    PyYAML используется, если установлен; иначе — минимальный разбор
    'key: value' и 'key: |' блоков, которого хватает для нашего формата.
    """
    shots: list[Shot] = []
    for block in YAML_BLOCK.findall(text):
        data = _load_yaml(block)
        if not data.get("shot"):
            continue
        known = {"shot", "tool", "type", "prompt", "negative", "seed", "duration", "input_image"}
        shots.append(
            Shot(
                shot=str(data["shot"]),
                tool=str(data.get("tool", "")),
                type=str(data.get("type", "video")),
                prompt=str(data.get("prompt", "")).strip(),
                negative=str(data.get("negative", "")).strip(),
                seed=_as_int(data.get("seed")),
                duration=_as_float(data.get("duration")),
                input_image=data.get("input_image"),
                extra={k: v for k, v in data.items() if k not in known},
            )
        )
    return shots


def _load_yaml(block: str) -> dict[str, Any]:
    try:
        import yaml  # type: ignore

        parsed = yaml.safe_load(block)
        return parsed if isinstance(parsed, dict) else {}
    except ImportError:
        pass

    data: dict[str, Any] = {}
    key: str | None = None
    buffer: list[str] = []
    for line in block.splitlines():
        if key and (line.startswith(("  ", "\t")) or not line.strip()):
            buffer.append(line.strip())
            continue
        if key:
            data[key] = "\n".join(buffer).strip()
            key, buffer = None, []
        if ":" not in line:
            continue
        name, _, value = line.partition(":")
        name, value = name.strip(), value.strip()
        if value == "|":
            key = name
        elif name:
            data[name] = value
    if key:
        data[key] = "\n".join(buffer).strip()
    return data


def parse_table(text: str, header_contains: str) -> list[dict[str, str]]:
    """Разбирает markdown-таблицу, в шапке которой встречается header_contains."""
    rows: list[dict[str, str]] = []
    headers: list[str] | None = None
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            headers = None
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if set("".join(cells)) <= set("-: "):
            continue
        if headers is None:
            if header_contains.lower() in " ".join(cells).lower():
                headers = cells
            continue
        if len(cells) != len(headers):
            continue
        row = dict(zip(headers, cells))
        if all(PLACEHOLDER.match(v.strip("`")) for v in row.values()):
            continue
        rows.append(row)
    return rows


def _as_int(value: Any) -> int | None:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _as_float(value: Any) -> float | None:
    try:
        return float(str(value).rstrip("сcs"))
    except (TypeError, ValueError):
        return None


# --------------------------------------------------------------------------- io


def log(message: str) -> None:
    print(f"[pipeline] {message}", file=sys.stderr)


def ffmpeg(args: Iterable[str], dry_run: bool) -> None:
    binary = shutil.which("ffmpeg")
    cmd = [binary or "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", *args]
    if dry_run:
        log("DRY-RUN ffmpeg: " + " ".join(cmd))
        return
    if binary is None:
        raise SystemExit("ffmpeg не установлен — он нужен для сборки эпизода.")
    subprocess.run(cmd, check=True)


def write_manifest(path: Path, payload: dict[str, Any], dry_run: bool) -> None:
    """Пишет рядом с результатом json с параметрами генерации (для повторяемости)."""
    if dry_run:
        log(f"DRY-RUN manifest: {path.relative_to(ROOT)}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def add_common_args(parser) -> None:
    parser.add_argument("episode", help="номер эпизода (1, 001) или путь к папке")
    parser.add_argument(
        "--shot", action="append", default=[],
        help="только указанные шоты (можно повторять): --shot sh01 --shot sh02",
    )
    parser.add_argument("--execute", action="store_true", help="реально вызывать API (по умолчанию dry-run)")
    parser.add_argument("--out", help="переопределить папку результата")
