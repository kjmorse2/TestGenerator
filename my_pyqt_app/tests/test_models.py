"""Basic tests for models."""

from my_pyqt_app.models.project_model import ProjectModel
from my_pyqt_app.models.user_settings import UserSettings


def test_project_model_add_remove():
    pm = ProjectModel(name="p1")
    pm.add_file("a.txt")
    assert "a.txt" in pm.files
    pm.remove_file("a.txt")
    assert "a.txt" not in pm.files


def test_user_settings_json_roundtrip():
    s = UserSettings(theme="dark", last_opened="/tmp")
    js = s.to_json()
    s2 = UserSettings.from_json(js)
    assert s2.theme == "dark"
    assert s2.last_opened == "/tmp"

