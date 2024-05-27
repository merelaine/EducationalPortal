class Teacher:
    def __init__(self, id, surname, name, lastname,email,password,phone):
        self.id = id
        self.surname = surname
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.phone = phone

    def __dict__(self):
        return {
            'id': self.id,
            'surname': self.surname,
            'name': self.name,
            'lastname': self.lastname,
            'email': self.email,
            'password': self.password,
            'phone': self.phone
        }

    def __str__(self):
        return f"Преподаватель: {self.surname} {self.name} {self.lastname}, Email: {self.email}, Телефон: {self.phone}"

    def __eq__(self, other):
        if isinstance(other, Teacher):
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

    def get_number_of_courses(self, courses):
        count = 0
        for course in courses:
            if course.teacher == self:
                count += 1
        return count