# IDENTITY LOCK — Прохор Ветлугин

> ⚠️ **Точка невозврата пройдена 21.08.2026.** Внешность утверждена владельцем.
> Файл закрыт на изменения до конца сезона. Любая правка = визуальный разрыв сериала.

## 1. Канонический сид

| Параметр | Значение |
|---|---|
| Модель | `soul_2` (text2image_soul_v2) |
| Seed | **753292** — turnaround v2, принят 21.08.2026 |
| Разрешение | 1152×2048 |
| Эталон | `references/hero-canonical.png` |

### Отменённые кандидаты

Три одиночных портрета (сиды 841891, 833286, 528046) отменены: turnaround собран
с нуля по locked-блоку и заменил их. Выбор вслепую не потребовался.

### Неудачная попытка turnaround — 21.08.2026

Десять ракурсов и выражений были сгенерированы с вариантом C в качестве **референсного
изображения**. Весь батч забракован: модель принудительно переписала промпты и заменила
персонажа на «model-like symmetrical» лицо с синими глазами и бородой, а все ракурсы —
на фронтальный крупный план.

**Вывод:** turnaround собирается только text-to-image с дословным locked-блоком,
без референсной картинки. См. `docs/production-stack/VIDEO_ENGINES.md` §3-бис.

### Turnaround v2 — 21.08.2026, **ПРИНЯТ**

| Параметр | Значение |
|---|---|
| Job ID | `1ac61c5a-517e-448f-885c-061d2c8daa85` |
| Seed | **753292** |
| Модель | `soul_2`, 2048×1152, 16:9 |
| `enhance_prompt` | **false** — промпт сохранён дословно, подтверждено в ответе API |
| Состав | четыре ракурса в одном кадре: фас, 3/4, профиль, спина |

Собран по методике character-sheet: **одна генерация вместо семи**. Лицо физически
не может разойтись между панелями, потому что панели нарисованы одновременно.

В промпт вошёл анти-ретушь модуль (`visible pores, natural asymmetry, no beauty filter,
no AI-airbrushed look`) и отдельные запреты `no babyface`, `no model-like symmetrical
features`, `no handsome idealized face` — прямо против искажений, которые дал прошлый батч.
Нашивка заказана **пустой**: `completely blank embroidered patch bearing no text at all`.

**Лист принят владельцем 21.08.2026.** Он становится эталоном: `references/hero-canonical.png`.

### Расхождения принятого листа с исходным текстом — locked-блок приведён к факту

Правило: **lock описывает то, что реально воспроизводится, а не то, что было написано.**
Ниже — что изменено в блоке §2 после приёмки.

| Что | Было в тексте | Что на принятом листе | Решение |
|---|---|---|---|
| Глаза | серо-зелёные | **серо-голубые**, холодные | блок исправлен по факту |
| Волосы | 3 см, без пробора, растрёпаны | длиннее, зачёсаны назад, с укладкой | **длина и посадка приняты**, растрёпанность переведена в состояние сцены |
| Шрам | через правую бровь | ложится **над** правой бровью, по надбровной дуге | блок исправлен по факту 21.08.2026, см. ниже |
| Нашивка | пустая, на левой груди | **на спине, бежевая, с мусорным текстом** | ❌ брак, исправляется во всех последующих кадрах |

### Три производственные поправки, обязательные для каждого кадра

1. **Нашивка.** Модель поставила на спину крупную нашивку с нечитаемыми буквами.
   В негатив каждого кадра с Прохором добавляется:
   `patch on the back, back patch, embroidered lettering, any text on clothing`.
   На груди нашивка допускается только пустой и мелкой.
2. **Волосы — это состояние, а не идентичность.** На листе они уложены, потому что лист
   студийный. В сериале Прохор в конце ночной смены: в промптах кадров добавляется
   `hair dishevelled and flattened after a long shift, not styled, no product`.
   Длина и линия роста остаются как на листе.
3. **Кожа.** На листе лоб местами глянцевый. В кадрах серии усиливается `matte complexion,
   no highlight blooms on the forehead` — блеск противоречит `COLOR_BIBLE`.

## 2. LOCKED-блок — вставляется в КАЖДЫЙ промпт дословно

```text
29 year old man, eastern european, 182cm lean wiry build,
face: narrow elongated oval, high forehead, visible cheekbones,
      slight natural asymmetry with the left eye set 2mm higher than the right,
eyes: grey-blue, cold, narrow set, heavy upper eyelids, dark shadows of chronic lack of sleep,
nose: straight with a barely visible bridge bump in profile,
lips: thin, upper thinner than lower, corners slightly down at rest,
skin: desaturated, large visible pores on nose and cheeks, faint perspiration,
hair: dark brown, short at the sides, slightly longer on top and swept back off the high forehead,
facial hair: constant three-day stubble,
marks: a thin 2cm scar lying horizontally along the RIGHT brow ridge,
       just above the eyebrow, not across the nose bridge,
       scraped knuckles on the right hand,
       an old soldering burn scar on the left forearm,
hands: broad palms, short nails with ingrained dirt, callus at the base of the index finger
```

### Поправка о шраме — 21.08.2026

Три генерации подряд — принятый turnaround и обе версии sh02 — поставили рубец
**над** правой бровью, по надбровной дуге, а не сквозь волоски брови. Сторона,
длина и горизонталь воспроизводятся устойчиво; расходится только высота, около
сантиметра, и на вертикальном экране эта разница не читается.

Блок приведён к факту по тому же правилу, по которому раньше был исправлен цвет
глаз: **lock описывает то, что реально воспроизводится, а не то, что было написано.**
Опознавательный признак сохранён целиком — тонкий горизонтальный рубец справа.

## 3. Неизменяемо

Форма головы и лица · разрез и цвет глаз · асимметрия глаз · горбинка носа ·
линия губ · посадка волос по принятому листу · постоянная трёхдневная щетина ·
**шрам через правую бровь** ·
рост и пропорции · сбитые костяшки правой руки.

## 4. Изменяемо

Свет, ракурс, эмоция, грязь, усталость, пот, повреждения по сюжету.
**Каждое повреждение записывается в `bible/CONTINUITY.md`** и переносится в следующие серии.

Текущее: ссадина на **левой** ладони с EP01, держится до EP03, заживает к EP04.

## 5. Гардероб

Базовый комплект неизменен весь сезон:

```text
dark navy utility work jacket, worn, with a small embroidered patch on the LEFT chest,
grey cotton t-shirt underneath, dark jeans, worn brown work boots,
keyring with 6 keys on the RIGHT hip
```

## 6. Как задаётся идентичность в промпте

**Негативного списка у персонажа больше нет.** Он снят 21.08.2026 по итогам пяти
прогонов эталонов: каждое существительное, оставленное в негативе, модель рисовала
в кадре. Правила — `.claude/agents/prompt-director.md`.

Всё, чего в лице быть не должно, формулируется утверждением о том, что там есть.
Таблица перевода обязательна к применению:

| Было в негативе | Стало утверждением |
|---|---|
| `beard, clean shaven` | `constant three-day stubble, never longer, never shaved` |
| `blue eyes, brown eyes` | `eyes grey-blue and cold` |
| `long hair, parted hair` | `short at the sides, slightly longer on top, swept back, no parting` |
| `scar on the left eyebrow` | `a thin 2cm scar along the RIGHT brow ridge` |
| `plastic skin, airbrushed, beauty retouching` | `matte, dry, visibly porous skin, natural asymmetry` |
| `smiling` | `mouth closed, corners of the lips slightly down at rest` |
| `glowing eyes` | `eyes lit only by the lamp present in the scene` |
| `younger man, older man` | `29 years old` |
| `muscular build` | `lean wiry build, 182cm` |
| `patch on the back, embroidered lettering` | `one small blank patch on the left chest, everywhere else the cloth is plain unmarked fabric` |
| `extra fingers, deformed hands` | `broad palms, five fingers, short nails with ingrained dirt` |

Первая строка любого промпта с Прохором:
`the same person as in the reference sheet, the same face in every feature`,
дальше LOCKED-блок §2 дословно.

## 7. Проверка перед приёмкой кадра

- [ ] Расстояние между глазами и разница высот совпадают с эталоном
- [ ] Горбинка носа читается в профиль
- [ ] Шрам на **правой** надбровной дуге на месте, горизонтальный, тонкий
- [ ] Щетина трёхдневная, не больше и не меньше
- [ ] Волосы по принятому листу: короче по бокам, длиннее сверху, зачёсаны назад, без пробора
- [ ] Куртка с нашивкой на левой груди, ключи на правом бедре
- [ ] Кожа с порами, без ретуши
