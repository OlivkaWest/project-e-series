# project-e-series · «Квартира 46»

AI-production studio для вертикального сериала. Не один ролик — конвейер на десятки серий.

> **В доме, где 45 квартир, каждую ночь в 00:46 открывается сорок шестая.**
> За ней — завтрашний день одного из жильцов. Прохор нашёл там свою мать, которую
> в этом подъезде больше никто не помнит, — но дом отдаёт только в обмен: за каждого,
> кого выносишь, кто-то отсюда перестаёт существовать.

**Формат:** 9:16, 1080×1920, 30 fps, серия 25–40 сек · **Сезон 1:** 12 серий
**Статус:** CHECKPOINT 5 — персонажи. Актуальное состояние — `PRODUCTION.md`.

---

## Как устроено производство

```
RESEARCH → SHOWRUNNING → SCRIPT → CHARACTERS → STORYBOARD → IMAGE → VIDEO
    → VOICE → MUSIC → SFX → EDIT → QA → PUBLISHING
```

Каждый этап ведёт свой агент. Их пятнадцать, у каждого узкая функция и право
остановить конвейер. Карта — `.claude/AGENT_MAP.md`.

Конвейер запускается скиллом `episode-production`: он проводит серию от идеи до экспорта
и не даёт пропустить контрольные точки.

## Быстрый старт

```bash
# 1. бинарники
brew install ffmpeg git-lfs jq      # macOS
git lfs install

# 2. python
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 3. ключи
cp .env.example .env                # заполнить, в репозиторий не коммитить

# 4. проверка окружения
python3 pipeline/edit/validate_render.py --selftest
```

## Какие ключи нужны

| Сервис | Обязателен | Зачем |
|---|---|---|
| Higgsfield | ✅ подключён через MCP | генерация изображений и видео |
| ElevenLabs | 🔑 нужен | голоса персонажей |
| Gemini | 🔑 опционально | альтернативный image-канал |
| Volcengine Ark | 🔑 опционально | Seedance |
| YouTube Data | 🔑 после публикации | аналитика |

Статусы всех интеграций — `integrations/README.md`.

## Производство одного эпизода

```
скилл episode-production
   ↓
IDEA → CANON CHECK → SCRIPT → RETENTION QA
   ⛔ SCRIPT APPROVAL
SHOTLIST → CONTINUITY CHECK
   ⛔ STORYBOARD APPROVAL
IMAGE PROMPTS → MASTER FRAMES
   ⛔ MASTER FRAME APPROVAL
VIDEO → VOICE → SFX → MUSIC → EDIT
   ↓
VISUAL QC → VIDEO QC → RETENTION QC
   ⛔ FINAL APPROVAL
EXPORT → CONTINUITY UPDATE
```

Творческие решения не автоматизируются: шесть контрольных точек — обязательная остановка.

**Сначала пилот.** Весь сезон не производится, пока EP01 не доведён до максимума и разобран.

## Где что лежит

| Путь | Что |
|---|---|
| `bible/` | библия сериала: мир, правила, визуальный язык, символы, звук, имена, заставка |
| `characters/` | персонажи: character bible, identity lock, референсы, промпты |
| `season-01/` | арка, карта 12 серий, полные пакеты эпизодов |
| `season-01/*/assets/` | мастер-кадры и эталонные ассеты (Git LFS) |
| `season-01/*/renders/` | клипы и сборки (Git LFS) |
| `prompts/templates/` | адаптеры промптов под каждую модель |
| `integrations/` | адаптеры сервисов и их статусы |
| `pipeline/edit/` | монтажный блок на FFmpeg |
| `research/` | исследование рынка и его разбор |
| `output/` | готовые ролики по площадкам |
| `docs/production-stack/` | аудит окружения, исследование инструментов, зависимости, движки |
| `.claude/` | агенты, скиллы, карта ролей, манифест |

## Читать в этом порядке

**Сериал**

1. `bible/SERIES_BIBLE.md` — что это за сериал
2. `bible/VISUAL_LANGUAGE.md` — визуальный язык (+ шесть профильных файлов)
3. `bible/WORLD.md` — мир и правило «Дом отдаёт — дом стирает»
4. `bible/NAMING.md` — имена как часть IP
5. `bible/STORY_RULES.md` — Story Engine и сетка по секундам
6. `season-01/EPISODE_MAP.md` — карта всех серий
7. `season-01/episode-001/SCRIPT.md` — **сценарий первой серии**

**Производство**

8. `PRODUCTION.md` — где мы сейчас
9. `.claude/AGENT_MAP.md` — кто за что отвечает
10. `docs/production-stack/VIDEO_ENGINES.md` — какой движок под какой кадр

**Исследование**

11. `research/manus-analysis/FINAL_DECISION.md` — почему выбран этот формат

## Правила, которые не обсуждаются

* Первые 2 секунды серии — без логотипов, титров и номера серии.
* В кадре ровно одна неправильная деталь. Не две и не ноль.
* Красный только с физическим источником в кадре.
* Цена показывается в кадре, а не проговаривается.
* Заставка никогда не ставится в начало серии.
* Генерация не пишет текст — кириллица рисуется в композе.
* Ключи живут в `.env` и не попадают в репозиторий.
