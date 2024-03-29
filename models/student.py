class Student:
    def __init__(self, id, surname, name, lastname,email,password,phone):
        self.id = id
        self.surname = surname
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.phone = phone

    def __str__(self):
        return f"Студент: {self.surname} {self.name} {self.lastname}, Email: {self.email}, Телефон: {self.phone}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return (
                    self.id == other.id
                    and self.surname == other.surname
                    and self.name == other.name
                    and self.lastname == other.lastname
                    and self.email == other.email
                    and self.password == other.password
                    and self.phone == other.phone
            )
        return False

    def check_unique_email(self, students_list):
        for student in students_list:
            if student.email == self.email and student.id != self.id:
                return False
        return True

    def get_course_count(self, courses):
        count = 0
        for course in courses:
            if self in course.students:
                count += 1
        return count
