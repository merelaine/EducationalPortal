class Topic:
    def __init__(self, id, name, description,theory,course):
        self.id = id
        self.name = name
        self.description = description
        self.theory = theory
        self.course = course

    def __str__(self):
        return f"Тема: {self.name}, Описание: {self.description}, Курс: {self.course}"
