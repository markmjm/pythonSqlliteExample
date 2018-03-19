import sqlite3


class DatabaseConnection:
    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self):
        self.connection = sqlite3.connect(self.host)
        return self.connection

    # Exception_type, Exception_Value, Exception_TraceBac
    def __exit__(self, exc_type, exc_val, exc_tb):
        if (exc_type is not None or exc_val is not None or exc_tb is not None):
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
