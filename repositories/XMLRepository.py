from repositories.repository import Repository
from models import *
import xml.etree.ElementTree as ET
import os

class XMLRepository(Repository):
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def get_full_path(self):
        return os.path.join(self.path, self.name)

    def get_root(self):
        try:
            tree = ET.parse(self.get_full_path())
            root = tree.getroot()
        except FileNotFoundError:
            return 'File was not found'

        return root

    def add(self, item):
        root = self.get_root()

        items = self.get_all()
        items.append(item)

        tree = ET.ElementTree(root)
        tree.write(self.get_full_path())

    def remove(self, item):
        root = self.get_root()

        items = self.get_all()
        items = [i for i in items if i.id != item.id]

        tree = ET.ElementTree(root)
        tree.write(self.get_full_path())

    def get(self, id):
        items = self.get_all()

        for item in items:
            if item.id == id:
                return item

    def get_all(self):
        items = []
        tree = ET.parse(self.get_full_path())
        root = tree.getroot()
        for elem in root.findall("./*"):
            item = self.create_item_from_element(elem)
            items.append(item)

        return items

    def update(self, item):
        root = self.get_root()

        items = self.get_all()
        for i, current_item in enumerate(items):
            if current_item.id == item.id:
                items[i] = item
            break
        tree = ET.ElementTree(root)
        tree.write(self.get_full_path())

    def create_item_from_element(self, elem):
        if elem.tag == 'course':
            id = int(elem.get('id'))
            name = elem.find('name').text
            description = elem.find('description').text
            duration = int(elem.find('duration').text)
            price = float(elem.find('price').text)
            teacher = elem.find('teacher').text
            students = []
            students = []
            for student_elem in elem.findall('student'):
                student_id = int(student_elem.get('id'))
                student_name = student_elem.find('name').text

                student = Student(student_id, student_name)
                students.append(student)
            return Course(id, name, description, duration, price, teacher)
