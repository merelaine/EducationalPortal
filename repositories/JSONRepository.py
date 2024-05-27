import json
from .repository import Repository
from models import *

class JSONRepository(Repository):
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.file_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add(self, items):
        for item in items:
            obj = {item.__class__.__name__ + '': item.__dict__()}

            # Use a unique key for each item
            key = f"{item.__class__.__name__}_{id(item)}"
            self.data[key] = obj

        self.save_data()

    def remove(self, item):
        if item in self.data:
            self.data.remove(item)
            self.save_data()

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
                self.save_data()

