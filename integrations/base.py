"""Общий контракт адаптеров. Ни один адаптер не притворяется рабочим."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

Status = Literal["CONNECTED", "NEEDS_KEY", "NOT_CONNECTED", "VIA_HIGGSFIELD"]


class NotConnectedError(RuntimeError):
    """Сервис недоступен. Поднимается явно, вместо тихой заглушки."""


@dataclass
class JobResult:
    job_id: str
    status: Literal["pending", "completed", "failed"]
    urls: list[str] = field(default_factory=list)
    meta: dict[str, Any] = field(default_factory=dict)


class Adapter:
    name: str = "base"
    status: Status = "NOT_CONNECTED"
    docs: str = ""

    def preflight(self) -> dict[str, Any]:
        """Доступность и оценка стоимости. Ничего не запускает."""
        return {"service": self.name, "status": self.status, "docs": self.docs}

    def submit(self, spec: dict[str, Any]) -> str:
        raise NotConnectedError(
            f"{self.name}: статус {self.status}. "
            f"См. integrations/{self.name}/README.md"
        )

    def result(self, job_id: str) -> JobResult:
        raise NotConnectedError(f"{self.name}: статус {self.status}")
