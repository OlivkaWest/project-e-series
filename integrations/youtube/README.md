# YouTube — `NEEDS_KEY` (частично работает без ключа)

## Без ключа — `yt-dlp==2026.6.9`

Метаданные ролика, субтитры, аудиодорожка, список видео канала.
Этого достаточно для research-блока: разбор хуков, структуры и механик конкурентов.

```bash
yt-dlp --skip-download --write-info-json --write-auto-subs --sub-lang ru,en <URL>
```

## С ключом — YouTube Data API v3

Нужен `YOUTUBE_API_KEY`. Даёт аналитику канала, статистику, поиск по критериям.
Понадобится **после публикации**, для замера результатов тест-блока.

## Цепочка research

```
VIDEO → TRANSCRIPT → HOOK → STORY STRUCTURE → RETENTION MECHANICS → CLIFFHANGER → REUSABLE PATTERN
```

Транскрипт: субтитры yt-dlp, если есть; иначе `faster-whisper` по аудиодорожке.
Разбор структуры делает `showrunner` по методике `research/manus-analysis/VIRAL_PATTERNS.md`.
