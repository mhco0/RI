class DatabaseFile:
    fileName

    def __init__(self):
        self.fileName = ""


class Database:
    path

    def __init__(self):
        self.path = ""

    def set_path(self, new_path):
        self.path = new_path