# SKILL MANIFEST

Всё, что усиливает Claude Code в этом проекте: скиллы, агенты, MCP, пакеты, бинарники.

## Скиллы проекта

| Skill | Source | Purpose | Installed | Version | Used by |
|---|---|---|---|---|---|
| `episode-production` | написан под проект | оркестратор конвейера эпизода | ✅ | 1.0 | владелец, все агенты |
| `video-production` | написан под проект | промпты видеогенерации | ✅ | 1.0 | `video-director` |
| `elevenlabs-production` | написан под проект | озвучка через официальный SDK | ✅ | 1.0 | `voice-director` |
| `episode-cover` | написан под проект | обложки и заголовки | ✅ | 1.0 | владелец |

## Агенты проекта

| Агент | Source | Purpose | Installed |
|---|---|---|---|
| 15 агентов, см. `AGENT_MAP.md` | написаны под библию проекта | production-роли | ✅ |

## MCP-серверы

| Skill | Source | Purpose | Installed | Version | Used by |
|---|---|---|---|---|---|
| `higgsfield` | провайдер | генерация image / video / audio, upscale, reframe | ✅ авторизован | провайдер | `prompt-director`, `video-director` |
| `github` | провайдер | исследование репозиториев, PR, issue | ✅ | провайдер | владелец |
| `claude-code-remote` | провайдер | сессии, расписания, уведомления | ✅ | провайдер | владелец |

## Системные бинарники

| Skill | Source | Purpose | Installed | Version | Used by |
|---|---|---|---|---|---|
| FFmpeg | apt / brew | сборка, микс, нормализация, экспорт | ✅ | 6.1.1 | `pipeline/edit/*` |
| ffprobe | идёт с FFmpeg | технический QA | ✅ | 6.1.1 | `video-qc` |
| Git LFS | apt / brew | хранение медиа | ✅ | 3.4.1 | репозиторий |

## Python-пакеты

| Skill | Source | Purpose | Installed | Version | Used by |
|---|---|---|---|---|---|
| yt-dlp | PyPI | метаданные и транскрипты YouTube | ✅ | 2026.6.9 | research |
| faster-whisper | PyPI | словные таймкоды → субтитры | ✅ | 1.2.0 | `pipeline/edit/add_subtitles.py` |
| elevenlabs | PyPI, официальный | озвучка | ✅ | 2.18.0 | `integrations/elevenlabs` |
| google-genai | PyPI, официальный | Gemini / Nano Banana | ✅ | 1.48.0 | `integrations/gemini` |
| ffmpeg-python | PyPI | обвязка FFmpeg | ✅ | 0.2.0 | `pipeline/edit/*` |
| httpx | PyPI | HTTP адаптеров | ✅ | 0.28.1 | `integrations/*` |
| pydantic | PyPI | схемы pipeline | ✅ | 2.12.4 | `pipeline/*` |
| python-dotenv | PyPI | загрузка `.env` | ✅ | 1.1.1 | `integrations/*` |
| Pillow | PyPI | кадры и обложки | ✅ | 12.1.0 | `episode-cover` |
| rich | PyPI | вывод CLI | ✅ | 14.3.0 | `pipeline/*` |

## Сознательно не установлено

ComfyUI · whisperX · auto-editor · MoviePy · Playwright · сторонние каталоги
claude-скиллов · сторонние обёртки над официальными SDK.
Причины — `docs/production-stack/GITHUB_RESEARCH.md`, раздел REJECTED.
