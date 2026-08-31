# EP01 — что и в каком порядке грузить в Grok

Все исходники лежат в репозитории: `incoming/REFERENCE_DUMP/`.
Имена файлов там — это ID генерации, поэтому ниже таблица соответствия.

**Порядок загрузки важен.** Номер в первой колонке — это порядок, в котором файл
добавляется в Grok. Первым всегда идёт стартовый кадр: он задаёт композицию,
свет и цвет. Вторым — то, что уточняет: конечное состояние, лицо или локация.

Промпты — `production/grok/EP01_GROK_PACKAGE/SHxxx/GROK_PROMPT.txt`.

---

## СЦЕНА 01 — кабина лифта

### SH001 · Панель лифта · генерируем 5 сек, в монтаж 2 сек

| № | Роль | Файл в репозитории | Что Grok берёт |
|--:|---|---|---|
| 1 | `01_START_FRAME` | [hf_20260821_160032_c791a9f4-63d9-4518-b625-4c1db5814165.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_160032_c791a9f4-63d9-4518-b625-4c1db5814165.png) | вход: металл ровный, не светится |
| 2 | `02_END_FRAME` | [hf_20260821_151228_b1fcec11-fc39-4905-a393-b3f80050a6ad.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_151228_b1fcec11-fc39-4905-a393-b3f80050a6ad.png) | выход: вспучина светится суриком |

### SH002 · Зеркало в кабине · генерируем 5 сек, в монтаж 2 сек

| № | Роль | Файл в репозитории | Что Grok берёт |
|--:|---|---|---|
| 1 | `01_START_FRAME` | [hf_20260821_151050_4752cbe1-68c6-49f8-b6a8-3cb9563c5478.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_151050_4752cbe1-68c6-49f8-b6a8-3cb9563c5478.png) | композиция, кабина, свет, поза |
| 2 | `02_CHARACTER_REFERENCE` | [hf_20260821_131258_1ac61c5a-517e-448f-885c-061d2c8daa85.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_131258_1ac61c5a-517e-448f-885c-061d2c8daa85.png) | ТОЛЬКО лицо и телосложение |

### SH003 · Палец не касается · генерируем 6 сек, в монтаж 3 сек

| № | Роль | Файл в репозитории | Что Grok берёт |
|--:|---|---|---|
| 1 | `01_START_FRAME` | [hf_20260821_151228_b1fcec11-fc39-4905-a393-b3f80050a6ad.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_151228_b1fcec11-fc39-4905-a393-b3f80050a6ad.png) | вход: вспучина горит, руки нет |
| 2 | `02_END_FRAME` | [hf_20260821_152531_419f4209-215a-4627-a770-3531301b4a93.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_152531_419f4209-215a-4627-a770-3531301b4a93.png) | выход: палец в воздухе, свет угас |

---

## СЦЕНА 02 — коридор 9-го этажа

### SH004 · Мигание трубки · генерируем 5 сек, в монтаж 3 сек

| № | Роль | Файл в репозитории | Что Grok берёт |
|--:|---|---|---|
| 1 | `01_START_FRAME` | [hf_20260821_134733_daedc142-05dc-4388-8a1b-eb57c98ae836.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_134733_daedc142-05dc-4388-8a1b-eb57c98ae836.png) | коридор целиком |

### SH005 · Четыре шага · генерируем 5 сек, в монтаж 3 сек

| № | Роль | Файл в репозитории | Что Grok берёт |
|--:|---|---|---|
| 1 | `01_START_FRAME` | [hf_20260821_135641_19a661c6-80ff-4c48-9270-b4bb221dd1cd.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_135641_19a661c6-80ff-4c48-9270-b4bb221dd1cd.png) | Прохор со спины в коридоре |
| 2 | `02_LOCATION_REFERENCE` | [hf_20260821_134237_7c9c1518-7f6b-49d0-9d89-29b78805c5cd.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_134237_7c9c1518-7f6b-49d0-9d89-29b78805c5cd.png) | архитектура и свет коридора |

### SH006 · Брелок качается · генерируем 5 сек, в монтаж 2.5 сек

| № | Роль | Файл в репозитории | Что Grok берёт |
|--:|---|---|---|
| 1 | `01_START_FRAME` | [hf_20260821_151228_8c77e469-2429-46b7-8d89-1f4afd53dec5.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_151228_8c77e469-2429-46b7-8d89-1f4afd53dec5.png) | ручка с рыбкой, ночь |

### SH007 · Волос шевелится · генерируем 4 сек, в монтаж 1.5 сек

| № | Роль | Файл в репозитории | Что Grok берёт |
|--:|---|---|---|
| 1 | `01_START_FRAME` | [hf_20260821_135641_c4d82186-5cc7-4ae6-bbd2-f475a196d9c6.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_135641_c4d82186-5cc7-4ae6-bbd2-f475a196d9c6.png) | один волос на латуни |

---

## СЦЕНА 03 — дверь 46

### SH008 · Узнавание · генерируем 5 сек, в монтаж 3 сек

| № | Роль | Файл в репозитории | Что Grok берёт |
|--:|---|---|---|
| 1 | `01_START_FRAME` | [hf_20260821_152015_66a87b60-3605-4412-8dc3-6f98f07c00c8.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_152015_66a87b60-3605-4412-8dc3-6f98f07c00c8.png) | лицо, половина в чёрном |
| 2 | `02_CHARACTER_REFERENCE` | [hf_20260821_131258_1ac61c5a-517e-448f-885c-061d2c8daa85.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_131258_1ac61c5a-517e-448f-885c-061d2c8daa85.png) | ТОЛЬКО лицо и телосложение |

### SH009 · Кольцо цепляется · генерируем 5 сек, в монтаж 3 сек

| № | Роль | Файл в репозитории | Что Grok берёт |
|--:|---|---|---|
| 1 | `01_START_FRAME` | [hf_20260821_151052_7d3af4de-390c-4bdb-909e-967b62d202e2.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_151052_7d3af4de-390c-4bdb-909e-967b62d202e2.png) | рука тянет кольцо с рыбкой |

### SH010 · Табличка гаснет · генерируем 5 сек, в монтаж 3 сек

| № | Роль | Файл в репозитории | Что Grok берёт |
|--:|---|---|---|
| 1 | `01_START_FRAME` | [hf_20260821_154004_268becae-893c-4a8a-8b21-b20b1efc4151.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_154004_268becae-893c-4a8a-8b21-b20b1efc4151.png) | Прохор боком, табличка в глубине |
| 2 | `02_LOCATION_REFERENCE` | [hf_20260821_134237_7c9c1518-7f6b-49d0-9d89-29b78805c5cd.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_134237_7c9c1518-7f6b-49d0-9d89-29b78805c5cd.png) | архитектура и свет коридора |

### SH011 · Свет по глазам · генерируем 4 сек, в монтаж 2 сек

| № | Роль | Файл в репозитории | Что Grok берёт |
|--:|---|---|---|
| 1 | `01_START_FRAME` | [hf_20260821_152015_c03d6217-6e67-4d7e-8c74-f7ac6b9e09c0.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_152015_c03d6217-6e67-4d7e-8c74-f7ac6b9e09c0.png) | полоса света по глазам |
| 2 | `02_CHARACTER_REFERENCE` | [hf_20260821_131258_1ac61c5a-517e-448f-885c-061d2c8daa85.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_131258_1ac61c5a-517e-448f-885c-061d2c8daa85.png) | ТОЛЬКО лицо и телосложение |

---

## СЦЕНА 04 — порог

### SH012 · Щель. Утро · генерируем 5 сек, в монтаж 3 сек

| № | Роль | Файл в репозитории | Что Grok берёт |
|--:|---|---|---|
| 1 | `01_START_FRAME` | [hf_20260821_151228_4a0182f5-0c45-4cd4-a4ec-668d760e4b31.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_151228_4a0182f5-0c45-4cd4-a4ec-668d760e4b31.png) | щель, силуэт ребёнка, молоко |

### SH013 · Экран телефона · генерируем 4 сек, в монтаж 2 сек

| № | Роль | Файл в репозитории | Что Grok берёт |
|--:|---|---|---|
| 1 | `01_START_FRAME` | [hf_20260821_153144_d534ed8f-bebf-442d-bb6c-8dfdc631aff5.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_153144_d534ed8f-bebf-442d-bb6c-8dfdc631aff5.png) | телефон, пустая кровать |

### SH014 · Резинка на ручке · генерируем 4 сек, в монтаж 2 сек

| № | Роль | Файл в репозитории | Что Grok берёт |
|--:|---|---|---|
| 1 | `01_START_FRAME` | [hf_20260821_152015_8e9bf3b6-3c2d-4927-a39f-20d5ad5a2996.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_152015_8e9bf3b6-3c2d-4927-a39f-20d5ad5a2996.png) | ладонь на ручке, резинка |

---

## Как скачать файл с GitHub

Открыть ссылку → кнопка **Download raw file** справа над картинкой.
Переименовывать не обязательно: важен порядок добавления, а не имя.

## Один файл на несколько шотов

| Файл | Где используется |
|---|---|
| [hf_20260821_131258_1ac61c5a-517e-448f-885c-061d2c8daa85.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_131258_1ac61c5a-517e-448f-885c-061d2c8daa85.png) | SH002, SH008, SH011 — референс лица |
| [hf_20260821_134237_7c9c1518-7f6b-49d0-9d89-29b78805c5cd.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_134237_7c9c1518-7f6b-49d0-9d89-29b78805c5cd.png) | SH005, SH010 — референс коридора |
| [hf_20260821_151228_b1fcec11-fc39-4905-a393-b3f80050a6ad.png](https://github.com/OlivkaWest/project-e-series/blob/claude/e-series-project-structure-1ol4sr/incoming/REFERENCE_DUMP/hf_20260821_151228_b1fcec11-fc39-4905-a393-b3f80050a6ad.png) | SH001 финал и SH003 старт |

Скачивать их повторно не нужно — грузятся из одного места.