"""Application entrypoint: starts the QApplication and main window.

Imports of PyQt are performed inside runtime functions so tests and linters
won't fail on systems without PyQt installed.
"""

import sys


def main(argv=None):
    """Start the QApplication and show the main window."""
    argv = argv or sys.argv
    try:
        from PyQt6.QtWidgets import QApplication
    except Exception:
        print("PyQt6 not installed. Install PyQt6 to run the GUI.")
        return 1

    from .app import AppWindow

    app = QApplication(argv)
    win = AppWindow()
    win.show()
    app.exec()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

