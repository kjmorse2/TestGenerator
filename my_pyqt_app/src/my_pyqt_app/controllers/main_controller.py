"""Controller connecting main window signals to application actions."""


class MainController:
    def __init__(self, main_window, services=None):
        self.main_window = main_window
        self.services = services or {}

    def setup(self):
        # Connect signals here. Keep minimal to avoid PyQt top-level imports.
        pass

