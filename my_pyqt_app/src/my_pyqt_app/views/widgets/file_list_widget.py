"""A custom widget that would show a list of files."""


def create_file_list_widget(parent=None):
    try:
        from PyQt6.QtWidgets import QListWidget
    except Exception:
        class Dummy:
            def __init__(self, parent=None):
                pass
        return Dummy()

    class FileListWidget(QListWidget):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.addItem("/path/to/example.txt")

    return FileListWidget(parent)

