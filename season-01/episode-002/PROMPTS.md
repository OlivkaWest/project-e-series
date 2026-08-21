# EP-002 — Промпты

Формат машиночитаемый: блоки ниже читает [`pipeline/generate_images.py`](../../pipeline/generate_images.py)
и [`pipeline/generate_video.py`](../../pipeline/generate_video.py).
Менять заголовки полей нельзя, добавлять поля — можно.

---

## sh01 — кейфрейм

```yaml
shot: sh01
tool: nano-banana
type: image
seed: 0
prompt: |
  CHARACTER: <блок из characters/main-character/identity-lock.md §1>
  SHOT: extreme close-up, 85mm, eye level
  SETTING: <LOC-01, время суток>
  LIGHT: <из bible/VISUAL_LANGUAGE.md §3>
  STYLE: <из bible/VISUAL_LANGUAGE.md §1>
negative: |
  <общий негатив + персональный>
```

Результат кладём в `assets/keyframes/sh01.png` (лучший дубль переименовываем без версии).

---

## sh01 — видео

```yaml
shot: sh01
tool: seedance
type: video
input_image: assets/keyframes/sh01.png
seed: 0
duration: 1.0
prompt: |
  CHARACTER: <блок из characters/main-character/identity-lock.md §1>
  SHOT: extreme close-up, 85mm, static
  ACTION: <одно действие>
  LOCATION: <LOC-01, детали из bible/WORLD.md §3>
  LIGHT: <из bible/VISUAL_LANGUAGE.md §3>
  STYLE: <из bible/VISUAL_LANGUAGE.md §1>
negative: |
  <общий негатив + персональный>
```

---

## sh02 — видео

```yaml
shot: sh02
tool: kling
type: video
input_image: assets/keyframes/sh02.png
seed: 0
duration: 2.0
prompt: |
  CHARACTER: <identity-lock>
  SHOT: medium shot, 50mm, slow push-in
  ACTION: <одно действие>
  LOCATION: <LOC-01>
  LIGHT: <...>
  STYLE: <...>
negative: |
  <...>
```

---

## Журнал попыток

| Шот | Версия | Seed | Что поменяли | Результат |
|-----|--------|------|--------------|-----------|
| sh01 | v01 | 0 | базовый прогон | TBD |
