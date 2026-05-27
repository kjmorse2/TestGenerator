"""A minimal database service placeholder.

This file intentionally contains a light-weight interface so tests can mock
or replace it easily.
"""


class DatabaseService:
    def __init__(self, dsn: str | None = None):
        self.dsn = dsn
        self._connected = False

    def connect(self):
        # In real app, open connection to DB. Here it's a no-op.
        self._connected = True

    def is_connected(self) -> bool:
        return self._connected

    def close(self):
        self._connected = False

