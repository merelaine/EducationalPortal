class Course:
    def __init__(self, id, name, description,duration,price,teacher,students):
        self.id = id
        self.name = name
        self.description = description
        self.duration = duration
        self.price = price
        self.teacher = teacher
        self.students = students

    def __str__(self):
        return f"Курс: {self.name}, Описание: {self.description}, Длительность: {self.duration}, Цена: {self.price}, Преподаватель: {self.teacher}"