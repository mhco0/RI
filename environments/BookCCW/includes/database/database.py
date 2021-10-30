class DatabaseFile:
    def __init__(self):
        self.fileName = ""


class Database:
    def __init__(self):
        self.cur_path = ""

    def set_path(self, new_path):
        self.cur_path = new_path