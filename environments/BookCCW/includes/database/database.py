import os
import json

class DatabaseObj:
    def __init__(self, filename="", link="", content=""):
        self.filename = filename
        self.link = link
        self.content = content

    def __str__(self):
        return "<DatabaseObj: .filename=" + self.filename + " .link=" + self.link + ".content=" + self.content +" >"

class Database:
    def __init__(self, path):
        self.base_path = path
        self.install_db()

    def set_base_path(self, new_path):
        self.base_path = new_path
        self.install_db()

    def install_db(self):
        if not os.path.exists(self.base_path):
            try:
                os.makedirs(self.base_path, exist_ok=True)
            except OSError as error:
                print("Directory can not be created")

    def expand_db(self, new_dir):
       if not os.path.exists(self.base_path + new_dir):
            try:
                os.makedirs(self.base_path + new_dir, exist_ok=True)
            except OSError as error:
                print("Directory can not be created")
    
    def save_file(self, db_obj):
        with open(db_obj.filename, 'w', encoding='utf-8') as file:
            obj = {"link" : db_obj.link,
                "content": db_obj.content}
            
            json.dump(obj, file, ensure_ascii=False, indent=4)

    def save_robots_file(self, filename, text):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)

    def load_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            obj = json.load(file)
        
        return DatabaseObj(filename, obj["link"], obj["content"])
    
    def load_robots_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()

    def load_dirs(self, directory):
        objs = []

        for file_or_dir in os.listdir(self.base_path + '/' + directory):
            if os.path.isfile(self.base_path + '/' + file_or_dir):
                objs.append(self.load_file(file_or_dir))

        return objs

    def load_dir_texts(self, directory):
        objs = []

        for file_or_dir in os.listdir(self.base_path + '/' + directory):
            if os.path.isfile(self.base_path + '/' + directory + '/' + file_or_dir):
                objs.append([self.load_robots_file(self.base_path + '/' + directory + '/' + file_or_dir), self.base_path + '/' + directory + '/' + file_or_dir])

        return objs


    def list_dirs(self):
        dirs = []

        for file_or_dir in os.listdir(self.base_path):
            if os.path.isdir(self.base_path + '/' +  file_or_dir):
                dirs.append(file_or_dir)
        
        return dirs