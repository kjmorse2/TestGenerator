"""File I/O helper service."""

from pathlib import Path
from typing import List


class FileService:
    def list_files(self, directory: str) -> List[str]:
        p = Path(directory)
        if not p.exists() or not p.is_dir():
            return []
        return [str(x) for x in p.iterdir() if x.is_file()]

    def read_text(self, path: str) -> str:
        return Path(path).read_text(encoding="utf-8")

    def write_text(self, path: str, content: str):
        Path(path).write_text(content, encoding="utf-8")

