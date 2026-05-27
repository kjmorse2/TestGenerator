"""User settings container and persistence helpers."""

from dataclasses import dataclass, asdict
import json
from typing import Any


@dataclass
class UserSettings:
    theme: str = "light"
    last_opened: str | None = None

    def to_json(self) -> str:
        return json.dumps(asdict(self))

    @staticmethod
    def from_json(data: str) -> "UserSettings":
        d = json.loads(data)
        return UserSettings(**d)

