"""Application-level setup and main window factory.

This module defines `AppWindow` which is a small QMainWindow subclass.
Imports of PyQt are kept inside functions to allow static checks when PyQt
is not available.
"""


class AppWindow:
    """A minimal wrapper around QMainWindow.

    To avoid import-time errors when PyQt isn't available, the real Qt class
    is acquired in __init__ at runtime.
    """

    def __init__(self):
        try:
            from PyQt6.QtWidgets import QMainWindow, QLabel
            from PyQt6.QtCore import Qt
        except Exception:
            # Provide a simple fallback for environments without PyQt installed.
            class _Dummy:
                def show(self):
                    print("(dummy) AppWindow.show() called - PyQt6 not installed")

            self._win = _Dummy()
            return

        class _MainWindow(QMainWindow):
            def __init__(self):
                super().__init__()
                self.setWindowTitle("my_pyqt_app")
                label = QLabel("Welcome to my_pyqt_app")
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.setCentralWidget(label)

        self._win = _MainWindow()

    def show(self):
        return self._win.show()

    # Expose useful methods as needed
    def setWindowTitle(self, title):
        if hasattr(self._win, "setWindowTitle"):
            self._win.setWindowTitle(title)

