class Task:
    def __init__(self, id, name, description, type, answer,topic,teacher):
        self.id = id
        self.name = name
        self.description = description
        self.type = type
        self.answer = answer
        self.topic = topic
        self.teacher = teacher

    def __str__(self):
        return f"Курс: {self.name}, Описание: {self.description}, Тип: {self.type}, Тема: {self.topic}, Преподаватель: {self.teacher}"