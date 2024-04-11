from repositories.repository import Repository
from models import *
import xml.etree.ElementTree as ET
import os
import xmltodict

class XMLRepository(Repository):
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def GetFullPath(self):
        return self.path + f"\\{self.name}"

    def add(self, item):
        pass

    def remove(self, item):
        pass

    def get(self, id):
        items = self.get_all()

        for item in items:
            if item.id == id:
                return item

    def get_all(self):
        pass

    def update(self, item):
        pass