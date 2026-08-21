# Project E — AI-native production system

Продакшн вертикального AI-сериала как репозиторий: история, персонажи, промпты,
ассеты и скрипты генерации лежат рядом и версионируются вместе.

## Структура

```
bible/          канон сериала: мир, правила, визуальный язык, непрерывность
characters/     персонажи + identity-lock для консистентности лиц
season-01/      арка сезона и эпизоды (story → script → shotlist → prompts → edit)
prompts/        правила и журналы промптов по каждому инструменту
assets/         сквозные ассеты: локации, реквизит, текстуры, лого, музыка, sfx
pipeline/       скрипты генерации и сборки
research/       форматы, референсы, конкуренты
output/         мастера по площадкам
```

## Как делается эпизод

| # | Шаг | Файл | Инструмент |
|---|-----|------|-----------|
| 1 | Идея и биты | `STORY.md` | — |
| 2 | Сценарий | `SCRIPT.md` | — |
| 3 | Разбивка на шоты | `SHOTLIST.md` | — |
| 4 | Раскадровка | `STORYBOARD.md` | nano-banana |
| 5 | Промпты | `PROMPTS.md` | — |
| 6 | Кейфреймы | `assets/keyframes/` | `generate_images.py` |
| 7 | Видео-шоты | `renders/` | `generate_video.py` |
| 8 | Озвучка | `assets/voice/` | `generate_voice.py` |
| 9 | Музыка и звук | `MUSIC.md` | — |
| 10 | Монтаж | `EDIT.md` | `assemble_episode.py` |
| 11 | Публикация | `output/` | `publish.py` |
| 12 | Непрерывность | `bible/CONTINUITY.md` | — |

## Быстрый старт

```bash
cp .env.example .env          # заполнить ключи
python pipeline/generate_images.py 001        # dry-run
python pipeline/generate_video.py 001 --execute
python pipeline/assemble_episode.py 001 --execute
```

Все скрипты по умолчанию в dry-run: без `--execute` кредиты не тратятся.
Нужен Python 3.10+ и `ffmpeg` (для сборки). Подробности — [`pipeline/README.md`](pipeline/README.md).

## Новый эпизод

```bash
cp -r season-01/_episode-template season-01/episode-004
grep -rl 'EP-000\|ep000' season-01/episode-004 | xargs sed -i 's/EP-000/EP-004/g; s/ep000/ep004/g'
```

## Правила проекта

1. Канон живёт в `bible/`. Противоречие канону — баг, а не творческая находка.
2. Лицо персонажа задаётся только блоком из `identity-lock.md`, дословно.
3. Промпт без seed и версии модели в продакшн не идёт.
4. Бинарники в git не коммитятся — в репозитории описания и ссылки.
5. После рендера обновляется `bible/CONTINUITY.md`.

Подробные инструкции для агентов — [`CLAUDE.md`](CLAUDE.md).
