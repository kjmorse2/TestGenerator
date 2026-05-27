"""Basic tests for services."""

from my_pyqt_app.services.file_service import FileService
from my_pyqt_app.services.database_service import DatabaseService
import tempfile


def test_file_service_read_write(tmp_path):
    fs = FileService()
    p = tmp_path / "x.txt"
    fs.write_text(str(p), "hello")
    assert fs.read_text(str(p)) == "hello"


def test_database_service_connect():
    db = DatabaseService(dsn=None)
    assert not db.is_connected()
    db.connect()
    assert db.is_connected()
    db.close()
    assert not db.is_connected()

