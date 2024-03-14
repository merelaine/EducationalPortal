from .repository import Repository

class StudentRepository(Repository):
    def __init__(self):
        self.students = {}

    def add(self, student):
        self.students[student.id] = student

    def get(self, student_id):
        return self.students.get(student_id)

    def update(self, student):
        if student.id in self.students:
            self.students[student.id] = student
        else:
            print(f"Ошибка: Студент с id {student.id} не существует")

    def remove(self, student):
        if student.id in self.students:
            del self.students[student.id]
        else:
            print(f"Ошибка: Студент с id {student.id} не существует")

    def get_all(self):
        return list(self.students.values())

