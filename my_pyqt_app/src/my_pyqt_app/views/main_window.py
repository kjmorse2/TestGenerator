"""Module containing a MainWindow widget skeleton."""


def create_main_window():
    try:
        from PyQt6.QtWidgets import QMainWindow, QLabel
        from PyQt6.QtCore import Qt
    except Exception:
        # Return a simple dummy object when PyQt is not installed
        class Dummy:
            def show(self):
                print("(dummy) MainWindow.show() called")

        return Dummy()

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Main Window")
            self.setCentralWidget(QLabel("Main window content"))

    return MainWindow()

