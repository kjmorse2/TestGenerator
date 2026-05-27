"""A small settings dialog scaffold."""


def create_settings_dialog(parent=None):
    try:
        from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel
    except Exception:
        class Dummy:
            def exec(self):
                print("(dummy) settings dialog exec")
                return 0
        return Dummy()

    class SettingsDialog(QDialog):
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setWindowTitle("Settings")
            layout = QVBoxLayout()
            layout.addWidget(QLabel("Settings go here"))
            self.setLayout(layout)

    return SettingsDialog(parent)

