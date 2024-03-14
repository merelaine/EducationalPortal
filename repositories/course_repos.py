from .repository import Repository

class CourseRepository(Repository):
    def __init__(self):
        self.courses = {}

    def add(self, course):
        self.courses[course.id] = course

    def get(self, course_id):
        return self.courses.get(course_id)

    def update(self, course):
        if course.id in self.courses:
            self.courses[course.id] = course
        else:
            print(f"Ошибка: Курс с id {course.id} не существует")

    def remove(self, course):
        if course.id in self.courses:
            del self.courses[course.id]
        else:
            print(f"Ошибка: Курс с id {course.id} не существует")

    def get_all(self):
        return list(self.courses.values())