"""Placeholder for QAbstractTableModel subclasses used in the app."""


class TableModels:
    """Collection placeholder for table models."""

    def __init__(self):
        self.models = {}

    def register(self, name, model):
        self.models[name] = model

    def get(self, name):
        return self.models.get(name)

