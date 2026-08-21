---
name: video-production
description: Создаёт production-ready промпты для видеогенерации в формате, который понимает последовательность движения. Используй при подготовке любого видеокадра. Раньше называлось seedance-production; формат сохранён, движки актуализированы.
---

# VIDEO PRODUCTION — промпт-движок

## Статус движков на 21.08.2026

**Seedance недоступен через подключённый канал.** Официальный путь — Volcengine Ark
(`doubao-seedance-2-0-260128`, 24 fps, старт и финал кадра, нативный звук), требует
отдельного ключа. Статус: `NEEDS_KEY`.

Формат промпта ниже **не привязан к Seedance** — он переносится на любой движок
из `docs/production-stack/VIDEO_ENGINES.md` без переписывания.

## Структура

```
SHOT:                  ep0NN-scN-shNN
MODEL:                 движок и параметры
INPUT IMAGE:           принятый мастер-кадр
DURATION:              секунды
ASPECT RATIO:          9:16
SUBJECT:               кто или что
INITIAL STATE:         состояние в нулевой момент
ACTION TIMELINE:       последовательность с секундами
CAMERA MOTION:         тип из bible/CAMERA_LANGUAGE.md
ENVIRONMENT:           пространство
PHYSICS:               скорость, масса, инерция, контакт, порядок
LIGHTING:              что делает свет во времени
FACIAL BEHAVIOR:       мимика или её отсутствие
CONTINUITY:            что остаётся неизменным
END STATE:             финальный кадр
NEGATIVE CONSTRAINTS:  запреты
```

## Главное правило

Модель должна понимать **что начинает происходить → как развивается движение →
где заканчивается кадр**. Не настроение.

```
ПЛОХО
cinematic mysterious scary atmosphere

ХОРОШО
0.0–1.0  The man remains completely still.
1.0–2.5  His eyes shift toward the doorway. The head does not move yet.
2.5–4.0  Only after the eyes have moved does the head begin to turn, fifteen degrees.
         At the same moment, deep in the background, a human-shaped shadow shifts
         once and stops. It never approaches the camera.
CAMERA   Locked off. No movement.
PHYSICS  The shadow is soft-edged, consistent with a figure five metres away.
         Nothing else in the frame responds.
IDENTITY Face, proportions, jacket and keyring remain completely unchanged.
```

## Физика описывается всегда

Что деформируется, с какой скоростью, что сопротивляется, в каком порядке.
Пример: кольцо цепляется за ручку — сопротивление видно **до** срыва,
след на коже появляется **после** контакта, а не во время.

## Обязательные запреты в каждом промпте

```
monster, creature, gore, jump scare, glowing eyes, plastic skin,
digital glitch, VHS artefacts, text, letters, numbers, signage, watermark,
extra fingers, deformed hands, camera movement (для статичных кадров),
focus pull onto the background
```

## Настройка вызова

* `sound: off` — **всегда**. Нативный звук моделей ломает звуковую конструкцию сериала.
* Соотношение сторон `9:16` — всегда.
* Длительность берётся из шот-листа, не округляется.
* `start_image` — принятый мастер-кадр. `end_image` — если движок поддерживает и кадр
  требует точного финального состояния.

## После генерации

Клип идёт в `visual-qc`. Результат с seed и job id записывается в журнал попыток эпизода.
