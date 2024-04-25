class Task:
    def __init__(self, id, name, description, type, answer,topic):
        self.id = id
        self.name = name
        self.description = description
        self.type = type
        self.answer = answer
        self.topic = topic

    def __str__(self):
        return f"Курс: {self.name}, Описание: {self.description}, Тип: {self.type}, Тема: {self.topic}"

    def __eq__(self, other):
        if isinstance(other, Task):
            return (
                    self.id == other.id
                    and self.name == other.name
                    and self.description == other.description
                    and self.type == other.type
                    and self.answer == other.answer
                    and self.topic == other.topic
            )
        return False