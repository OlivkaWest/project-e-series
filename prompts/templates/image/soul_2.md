# soul_2 — основной image-движок

**Проверен на холодном тесте 21.08.2026.** Хорошо держит фактуру, свет и палитру.
Известная слабость: **самовольно дописывает текст** и не пишет кириллицу.

```text
<STYLE BLOCK из bible/VISUAL_LANGUAGE.md §11>
<IDENTITY LOCK персонажа, если в кадре человек>

SUBJECT:     кто или что
ACTION:      что делает
LOCATION:    где
CAMERA:      тип кадра
LENS:        100mm macro / 85mm / 50mm / 35mm / 24mm
LIGHTING:    один мотивированный источник
COMPOSITION: 9:16, нижняя треть, безопасные зоны
MATERIALS:   какие фактуры обязаны читаться
ATMOSPHERE:  одна фраза
CONTINUITY:  что совпадает с эталоном
NEGATIVE:    <общий негатив> + text, letters, numbers, signage, watermark, caption
```

**Параметры вызова:** `aspect_ratio: "9:16"`, `use_unlim: false`, quality по умолчанию 2k.
Seed принятого кадра фиксируется в журнале эпизода.
