import json
from .repository import Repository

class JSONRepository(Repository):
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = self._load_data()

    def _load_data(self):
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_data(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add(self, item):
        self.data.append(item)
        self._save_data()

    def remove(self, item):
        if item in self.data:
            self.data.remove(item)
            self._save_data()

    def get(self, item_id):
        for item in self.data:
            if item.get('id') == item_id:
                return item
        return None

    def get_all(self):
        return self.data

    def update(self, updated_item):
        for index, item in enumerate(self.data):
            if item.get('id') == updated_item.get('id'):
                self.data[index] = updated_item
                self._save_data()