# Pipeline — производственные скрипты

| Скрипт | Что делает |
|---|---|
| `generate_images.py` | Master frames по промптам эпизода → `season-01/episode-XXX/assets/` |
| `generate_video.py` | Image-to-video по шот-листу → `season-01/episode-XXX/renders/` |
| `generate_voice.py` | Реплики из `VOICE.md` → аудиофайлы |
| `assemble_episode.py` | Сборка таймлайна из `EDIT.md` → `output/` |
| `publish.py` | Выгрузка и метаданные по площадкам |

Все скрипты на этом этапе — каркас: они разбирают проектные документы и печатают план работ.
Вызовы генеративных API подключаются после утверждения пилота (CHECKPOINT 9).

Ключи берутся из переменных окружения, см. `.env.example`. Ключи в репозиторий не попадают.
