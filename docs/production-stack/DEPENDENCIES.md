# DEPENDENCIES — закреплённые версии

Production-pipeline не должен сломаться завтра. Все версии зафиксированы точно (`==`).

## Системные бинарники

| Компонент | Версия | Проверка | Установка |
|---|---|---|---|
| FFmpeg | 6.1.1 | `ffmpeg -version` | `brew install ffmpeg` / `apt install ffmpeg` |
| ffprobe | 6.1.1 | `ffprobe -version` | идёт с FFmpeg |
| Git LFS | 3.4.1 | `git lfs version` | `brew install git-lfs && git lfs install` |
| Python | 3.11+ | `python3 -V` | — |
| Node.js | 22.x | `node -v` | нужен только для Claude Code |
| Claude Code | 2.1.238 | `claude --version` | — |

**Минимальные версии:** FFmpeg ≥ 6.0 (нужен фильтр `loudnorm` во второй проход),
Python ≥ 3.10 (синтаксис `match`, современный `typing`), Git LFS ≥ 3.0.

## Python

Воспроизводится из `requirements.txt` в корне:

```
yt-dlp==2026.6.9
faster-whisper==1.2.0
elevenlabs==2.18.0
google-genai==1.48.0
httpx==0.28.1
pydantic==2.12.4
python-dotenv==1.1.1
ffmpeg-python==0.2.0
Pillow==12.1.0
rich==14.3.0
```

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## MCP-серверы

| Сервер | Роль в production | Версия |
|---|---|---|
| higgsfield | генерация image / video / audio | управляется провайдером |
| github | исследование и работа с репозиториями | управляется провайдером |
| claude-code-remote | сессии и расписания | управляется провайдером |

Версии MCP на стороне провайдера не закрепляются. Поэтому все вызовы генерации идут
**через адаптеры** в `integrations/`: если контракт MCP поменяется, правится один файл,
а не весь pipeline.

## Политика обновлений

1. Версии не обновляются в середине производства сезона.
2. Обновление — только между сезонами, отдельным коммитом, с перезапуском smoke-теста.
3. Любое обновление FFmpeg требует повторной проверки `validate_render.py` на принятом эпизоде.
4. Модели генерации фиксируются по id и параметрам в `docs/production-stack/VIDEO_ENGINES.md`;
   смена модели посреди сезона запрещена — она ломает визуальную непрерывность.
