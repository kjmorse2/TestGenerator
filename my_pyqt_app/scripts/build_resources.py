"""Simple resource build script placeholder.

In a real project this might call pyrcc or compile .ui files; here it
just copies placeholders or prints a message.
"""

from pathlib import Path


def build_resources(project_root: str | None = None):
    root = Path(project_root or Path(__file__).resolve().parents[2])
    print(f"Building resources under {root}")


if __name__ == "__main__":
    build_resources()

