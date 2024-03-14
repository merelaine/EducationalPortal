class Student_Task:
    def __init__(self, id, student,task,score,time):
        self.id = id
        self.student = student
        self.task = task
        self.score=score
        self.time = time

    def __str__(self):
        return f"Студент: {self.student}, Задание: {self.task}, Оценка: {self.score}, Время выполнения: {self.time}"