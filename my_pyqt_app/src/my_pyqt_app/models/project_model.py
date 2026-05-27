"""A simple project model representing a collection of files and metadata."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class ProjectModel:
    name: str = "Untitled"
    files: List[str] = field(default_factory=list)

    def add_file(self, path: str):
        if path not in self.files:
            self.files.append(path)

    def remove_file(self, path: str):
        if path in self.files:
            self.files.remove(path)

