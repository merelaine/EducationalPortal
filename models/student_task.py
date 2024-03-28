from models.student import Student
from models.task import Task
class Student_Task:
    def __init__(self, id, student: Student,task: Task,score,time):
        self.id = id
        self.student = student
        self.task = task
        self.score=score
        self.time = time

    def __str__(self):
        return f"Студент: {self.student}, Задание: {self.task}, Оценка: {self.score}, Время выполнения: {self.time}"

    def __eq__(self, other):
        if isinstance(other, Student_Task):
            return (
                    self.id == other.id
                    and self.student == other.student
                    and self.task == other.task
                    and self.score == other.score
                    and self.time == other.time
            )
        return False
