from models.student import Student

class Course:
    def __init__(self, id, name, description, duration,price,teacher,students: list[Student]):
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

    def assign_teacher(self, new_teacher,all_courses):
        # Бизнес-правило: Преподаватель не может быть прикреплен более, чем к 3 курсам
        if new_teacher.get_number_of_courses(all_courses) >= 3:
            print("Ошибка: Преподаватель уже прикреплен к 3 курсам")
            return False
        self.teacher = new_teacher
        return True

    def enroll_student(self, new_student,all_courses):
        if new_student.get_course_count(all_courses) <= 5:
            self.students.append(new_student)
            print(f"Студент {new_student.name} успешно записан на курс: {self.name}")
            return True
        else:
            print(f"Ошибка: Студент {new_student.name} уже записан на максимальное количество курсов.")
            return False