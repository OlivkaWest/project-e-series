# Pipeline

Скрипты на чистом Python 3.10+ (плюс `ffmpeg` для сборки). Все запускаются
**в режиме dry-run по умолчанию** — без `--execute` ничего не генерируется и кредиты не тратятся.

## Порядок

```bash
python pipeline/generate_images.py 001 --execute   # кейфреймы из PROMPTS.md
python pipeline/generate_video.py  001 --execute   # шоты -> renders/
python pipeline/generate_voice.py  001 --execute   # реплики из VOICE.md
python pipeline/assemble_episode.py 001 --execute  # монтаж по EDIT.md -> output/shorts/
python pipeline/publish.py         001 --execute --target telegram
```

## Что откуда читается

| Скрипт | Источник | Результат |
|--------|----------|-----------|
| `generate_images.py` | `PROMPTS.md` (блоки `type: image`) | `assets/keyframes/` |
| `generate_video.py` | `PROMPTS.md` (видео-блоки) | `renders/` |
| `generate_voice.py` | `VOICE.md` (таблицы «Голоса» и «Реплики») | `assets/voice/` |
| `assemble_episode.py` | `EDIT.md` + `MUSIC.md` | `output/shorts/<code>.mp4` |
| `publish.py` | `output/shorts/<code>.mp4` | `output/<площадка>/` + публикация |

`common.py` — общие пути, парсинг markdown/yaml, обёртка над ffmpeg.

## Статус адаптеров

| Провайдер | Статус |
|-----------|--------|
| ElevenLabs (озвучка) | реализован |
| Telegram (публикация) | реализован |
| nano-banana / grok / seedance / kling / veo | заготовка: точка подключения в `generate()` |
| YouTube / Reels | заготовка: файл готовится, загрузка вручную |

Ключи — в `.env` (см. `.env.example`). Рядом с каждым результатом пишется `.json`
с промптом и seed — без него результат считается неповторяемым.
