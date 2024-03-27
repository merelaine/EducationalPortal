from .repository import Repository

class StudTaskRepository(Repository):
    def __init__(self):
        self.studtasks = {}

    def add(self, task):
        self.studtasks[task.id] = task

    def get(self, task_id):
        return self.studtasks.get(task_id)

    def update(self, task):
        if task.id in self.studtasks:
            self.studtasks[task.id] = task
        else:
            print(f"Ошибка: Отправленного ответа с id {task.id} не существует")

    def remove(self, task):
        if task.id in self.studtasks:
            del self.studtasks[task.id]
        else:
            print(f"Ошибка: Отправленного ответа с id {task.id} не существует")

    def get_all(self):
        return list(self.studtasks.values())