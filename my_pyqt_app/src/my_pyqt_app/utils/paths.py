"""Utility helpers for file-system paths used by the app."""

from pathlib import Path


def project_root() -> Path:
    # Return path to the package root (two levels up from this file)
    return Path(__file__).resolve().parents[2]


def resources_dir() -> Path:
    return project_root() / "resources"

