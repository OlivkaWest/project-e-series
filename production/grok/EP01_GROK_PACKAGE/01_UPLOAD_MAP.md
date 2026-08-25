# UPLOAD MAP — что грузить в Grok на каждом шоте

Правило: минимальный сильный набор. Если стартовый кадр уже содержит локацию
и предмет — отдельный референс локации не нужен.

| Shot | Файлы для загрузки | Порядок |
|---|---|---|
| SH001 | START_FRAME · END_FRAME | 1 → 2 |
| SH002 | START_FRAME · CHARACTER_REFERENCE | 1 → 2 |
| SH003 | START_FRAME · END_FRAME | 1 → 2 |
| SH004 | START_FRAME | 1 |
| SH005 | START_FRAME · LOCATION_REFERENCE | 1 → 2 |
| SH006 | START_FRAME | 1 |
| SH007 | START_FRAME | 1 |
| SH008 | START_FRAME · CHARACTER_REFERENCE | 1 → 2 |
| SH009 | START_FRAME | 1 |
| SH010 | START_FRAME · LOCATION_REFERENCE | 1 → 2 |
| SH011 | START_FRAME · CHARACTER_REFERENCE | 1 → 2 |
| SH012 | START_FRAME | 1 |
| SH013 | START_FRAME | 1 |
| SH014 | START_FRAME | 1 |

## Роли файлов

| Файл | Что Grok должен из него взять |
|---|---|
| `START_FRAME.png` | композицию, ракурс, свет, цвет, позу и реквизит первого кадра |
| `END_FRAME.png` | состояние, к которому шот обязан прийти |
| `CHARACTER_REFERENCE.png` | **только** лицо, голову, возраст, щетину, телосложение |
| `LOCATION_REFERENCE.png` | архитектуру, материалы и свет коридора |

`CHARACTER_REFERENCE.png` — это принятый turnaround. Из него берётся **только
идентичность**. Поза, студийный фон, свет и нашивка на спине оттуда не берутся:
нашивка на спине — производственный брак листа, в кадры не наследуется.
