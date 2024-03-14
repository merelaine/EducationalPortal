from .repository import Repository

class TeacherRepository(Repository):
    def __init__(self):
        self.teachers = {}

    def add(self, teacher):
        self.teachers[teacher.id] = teacher

    def get(self, teacher_id):
        return self.teachers.get(teacher_id)

    def update(self, teacher):
        if teacher.id in self.teachers:
            self.teachers[teacher.id] = teacher
        else:
            print(f"Ошибка: Преподаватель с id {teacher.id} не существует")

    def remove(self, teacher):
        if teacher.id in self.teachers:
            del self.teachers[teacher.id]
        else:
            print(f"Ошибка: Преподаватель с id {teacher.id} не существует")

    def get_all(self):
        return list(self.teachers.values())