from .repository import Repository

class TaskRepository(Repository):
    def __init__(self):
        self.tasks = {}

    def add(self, task):
        self.tasks[task.id] = task

    def get(self, task_id):
        return self.tasks.get(task_id)

    def update(self, task):
        if task.id in self.tasks:
            self.tasks[task.id] = task
        else:
            print(f"Ошибка: Задание с id {task.id} не существует")

    def remove(self, task):
        if task.id in self.tasks:
            del self.tasks[task.id]
        else:
            print(f"Ошибка: Задание с id {task.id} не существует")

    def get_all(self):
        return list(self.tasks.values())