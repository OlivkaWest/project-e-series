# INTEGRATIONS — адаптеры сервисов

**Принцип: фейковых интеграций здесь нет.** Если у сервиса нет доступного API
или у нас нет ключа — лежит интерфейс, документация и статус `NOT_CONNECTED`.

Приоритет доступа: **официальный API → официальный SDK → поддерживаемый MCP →
ручной экспорт → браузерная автоматизация.** Обход CAPTCHA и ограничений сервисов
не выполняется ни при каких условиях.

## Статусы

| Сервис | Статус | Путь доступа | Что нужно |
|---|---|---|---|
| **higgsfield** | ✅ `CONNECTED` | MCP-сервер | ничего, авторизован |
| **elevenlabs** | 🔑 `NEEDS_KEY` | официальный SDK 2.18.0 | `ELEVENLABS_API_KEY` |
| **gemini** | 🔑 `NEEDS_KEY` | официальный SDK `google-genai` 1.48.0 | `GEMINI_API_KEY` |
| **grok** | 🟡 `VIA_HIGGSFIELD` | модели `grok_image`, `grok_video_v15` через MCP | прямой ключ xAI — опционально |
| **kling** | 🟡 `VIA_HIGGSFIELD` | модели `kling3_0`, `kling2_6` через MCP | — |
| **veo** | 🟡 `VIA_HIGGSFIELD` | модель `veo3` через MCP | — |
| **seedance** | ❌ `NOT_CONNECTED` | Volcengine Ark | аккаунт + `ARK_API_KEY` |
| **youtube** | 🔑 `NEEDS_KEY` | YouTube Data API v3 | `YOUTUBE_API_KEY` |

## Общий контракт

Каждый адаптер обязан отдавать одно и то же независимо от сервиса:

```python
from integrations.base import Adapter, JobResult

class SomeAdapter(Adapter):
    name = "some"
    status = "NEEDS_KEY"          # CONNECTED | NEEDS_KEY | NOT_CONNECTED | VIA_HIGGSFIELD
    def preflight(self) -> dict:  ...   # доступность и стоимость, без запуска
    def submit(self, spec) -> str: ...  # вернуть job_id
    def result(self, job_id) -> JobResult: ...
```

Смысл: если контракт MCP или SDK поменяется, правится один файл, а не весь pipeline.
