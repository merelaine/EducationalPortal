from models.student import Student
from models.teacher import Teacher
class Course:
    def __init__(self, id, name, description, duration,price,teacher: Teacher,students: list[Student]):
        self.id = id
        self.name = name
        self.description = description
        self.duration = duration
        self.price = price
        self.teacher = teacher
        self.students = students

    def __str__(self):
        return f"Курс: {self.name}, Описание: {self.description}, Длительность: {self.duration}, Цена: {self.price}, Преподаватель: {self.teacher}"

    def __eq__(self, other):
        if isinstance(other, Course):
            return (
                    self.id == other.id
                    and self.name == other.name
                    and self.description == other.description
                    and self.duration == other.duration
                    and self.price == other.price
                    and self.teacher == other.teacher
                    and self.students == other.students
            )
        return False