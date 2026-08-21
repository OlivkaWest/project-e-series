# IDENTITY LOCK — Прохор Ветлугин

> ⚠️ **Точка невозврата.** После утверждения этот файл не меняется до конца сезона.
> Любое изменение = визуальный разрыв сериала.

## 1. Канонический сид

| Параметр | Значение |
|---|---|
| Модель | `soul_2` (text2image_soul_v2) |
| Seed | **ожидает выбора владельца** — три кандидата ниже |
| Разрешение | 1152×2048 |
| Эталон | `references/hero-canonical.png` |

### Кандидаты в канонический сид — прогон 21.08.2026

| Вариант | Seed | Job ID | Отличие промпта | Выбор |
|---|---:|---|---|---|
| A | **841891** | `6cccf614-c848-4eba-b6b3-e2d75021b841` | базовая формулировка | ⬜ |
| B | **833286** | `9bed7ebb-40af-4658-b51d-9117b12e1743` | hard chiaroscuro, акцент на щетине | ⬜ |
| C | **528046** | `c51bb514-11f3-41d6-931d-1d1ff1080581` | документальная подача, нашивка на куртке | ⬜ |

После выбора: seed вписывается в таблицу выше, два других кандидата удаляются,
файл закрывается на изменения до конца сезона.

### Неудачная попытка turnaround — 21.08.2026

Десять ракурсов и выражений были сгенерированы с вариантом C в качестве **референсного
изображения**. Весь батч забракован: модель принудительно переписала промпты и заменила
персонажа на «model-like symmetrical» лицо с синими глазами и бородой, а все ракурсы —
на фронтальный крупный план.

**Вывод:** turnaround собирается только text-to-image с дословным locked-блоком,
без референсной картинки. См. `docs/production-stack/VIDEO_ENGINES.md` §3-бис.

### Turnaround v2 — 21.08.2026, на приёмке

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

**После приёмки:** из листа делается Element, и все кадры EP01 и всё видео идут через него.

## 2. LOCKED-блок — вставляется в КАЖДЫЙ промпт дословно

```text
29 year old man, eastern european, 182cm lean wiry build,
face: narrow elongated oval, high forehead, visible cheekbones,
      slight natural asymmetry with the left eye set 2mm higher than the right,
eyes: grey-green, narrow set, heavy upper eyelids, dark shadows of chronic lack of sleep,
nose: straight with a barely visible bridge bump in profile,
lips: thin, upper thinner than lower, corners slightly down at rest,
skin: desaturated, large visible pores on nose and cheeks, faint perspiration,
hair: dark ash brown, short 3cm, no parting, slightly dishevelled,
facial hair: constant three-day stubble,
marks: a thin 2cm scar through the RIGHT eyebrow,
       scraped knuckles on the right hand,
       an old soldering burn scar on the left forearm,
hands: broad palms, short nails with ingrained dirt, callus at the base of the index finger
```

## 3. Неизменяемо

Форма головы и лица · разрез и цвет глаз · асимметрия глаз · горбинка носа ·
линия губ · длина волос 3 см · постоянная трёхдневная щетина · **шрам через правую бровь** ·
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

## 6. Негативный промпт персонажа

```text
different face, face morphing, inconsistent features, younger man, older man,
beard, clean shaven, long hair, parted hair, blue eyes, brown eyes,
scar on the left eyebrow, muscular build, plastic skin, airbrushed skin,
beauty retouching, smiling, glowing eyes, extra fingers, deformed hands
```

## 7. Проверка перед приёмкой кадра

- [ ] Расстояние между глазами и разница высот совпадают с эталоном
- [ ] Горбинка носа читается в профиль
- [ ] Шрам на **правой** брови на месте
- [ ] Щетина трёхдневная, не больше и не меньше
- [ ] Волосы 3 см, без пробора
- [ ] Куртка с нашивкой на левой груди, ключи на правом бедре
- [ ] Кожа с порами, без ретуши
