class Teacher:
    def __init__(self, id, surname, name, lastname,email,password,phone):
        self.id = id
        self.surname = surname
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.phone = phone

    def __str__(self):
        return f"Преподаватель: {self.surname} {self.name} {self.lastname}, Email: {self.email}, Телефон: {self.phone}"