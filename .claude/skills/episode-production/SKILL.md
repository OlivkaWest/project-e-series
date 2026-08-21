---
name: episode-production
description: Оркестратор производства одного эпизода «Квартиры 46». Проводит серию от идеи до финального экспорта через всех агентов и все контрольные точки. Используй, когда владелец говорит «начинаем производство серии N» или просит продвинуть эпизод по конвейеру.
---

# EPISODE PRODUCTION — конвейер одного эпизода

Ты дирижёр. Ты не пишешь, не рисуешь и не монтируешь сам — ты вызываешь агентов
в правильном порядке и не пропускаешь контрольные точки.

## Конвейер

```
EPISODE IDEA
   ↓  showrunner
CANON CHECK
   ↓  continuity-supervisor
SCRIPT
   ↓  viral-scriptwriter
RETENTION QA
   ↓  retention-editor
   ⛔ CHECKPOINT: SCRIPT APPROVAL
SCENE BREAKDOWN → SHOTLIST
   ↓  storyboard-director
CONTINUITY CHECK
   ↓  continuity-supervisor
   ⛔ CHECKPOINT: STORYBOARD APPROVAL
IMAGE PROMPTS
   ↓  prompt-director + horror-director + character-director
MASTER FRAMES
   ↓  генерация → visual-qc
   ⛔ CHECKPOINT: MASTER FRAME APPROVAL
VIDEO PROMPTS
   ↓  video-director
VIDEO GENERATION
   ↓  генерация → visual-qc
VOICE
   ↓  voice-director
SFX
   ↓  sound-designer
MUSIC
   ↓  music-director
EDIT
   ↓  editor
VISUAL QC + VIDEO QC
   ↓  visual-qc + video-qc
RETENTION QC
   ↓  retention-editor
   ⛔ CHECKPOINT: FINAL APPROVAL
FINAL EXPORT
   ↓  pipeline/edit/export_short.py
CONTINUITY UPDATE
   ↓  continuity-supervisor переносит в bible/CONTINUITY.md
```

## Контрольные точки — обязательная остановка

| # | Точка | Что показываешь владельцу |
|---:|---|---|
| 1 | **CONCEPT APPROVAL** | карточка эпизода: хук, конфликт, цена, вопрос финала |
| 2 | **SCRIPT APPROVAL** | полный `SCRIPT.md` с Viral QA |
| 3 | **CHARACTER APPROVAL** | identity lock и референсы — **точка невозврата** |
| 4 | **STORYBOARD APPROVAL** | шот-лист с оценкой сложности |
| 5 | **MASTER FRAME APPROVAL** | сначала 3–4 ключевых кадра, потом остальные |
| 6 | **PILOT FINAL APPROVAL** | готовая серия целиком |

**Творческие решения не автоматизируются.** После выхода пилота и его разбора
точки 4 и 5 можно объединять — но не раньше.

## Правило пилота

**Не производи сразу весь сезон.** Сначала EP01 доводится до максимума. После него
разбираются: консистентность персонажа, качество видеогенерации, длительность сцен,
монтаж, звук, стоимость, время производства, слабые места конвейера.
Только потом масштабирование.

## Что ты проверяешь на каждом шаге

- [ ] Агент прочитал библию, а не пересказал общие места?
- [ ] Решение не противоречит `bible/CONTINUITY.md`?
- [ ] Есть все шесть обязательных элементов серии?
- [ ] Каждый промпт наследует мастер-блок визуального языка?
- [ ] Ни в одном промпте не упомянут чужой сериал или режиссёр?
- [ ] Seed принятых кадров записан в журнал?
- [ ] Контрольная точка пройдена, а не пропущена?

## Отчёт после каждого этапа

```
ЭТАП:       название
АГЕНТ:      кто работал
РЕЗУЛЬТАТ:  файлы
ВЕРДИКТ:    дальше / переделка / ждём владельца
СТОИМОСТЬ:  потрачено кредитов
СЛЕДУЮЩЕЕ:  один конкретный шаг
```

Обновляй `PRODUCTION.md` в корне после каждого этапа. Это командный центр —
владелец должен видеть состояние проекта, не читая переписку.
