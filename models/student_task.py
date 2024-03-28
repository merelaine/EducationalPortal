from datetime import datetime
class Student_Task:
    def __init__(self, id, student,task,score,time,date):
        self.id = id
        self.student = student
        self.task = task
        self.score=score
        self.time = time
        self.date = date

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
                    and self.date == other.date
            )
        return False

    #Ответ на задание должен быть проверен в течение 5 дней.
    def check_score_by_time(self):
        current_date = datetime.now().date()
        submission_date = self.date

        if self.score is not None and (current_date - submission_date).days <= 5:
            return "Ответ на задание был проверен в течение 5 дней после отправки."
        else:
            return "Ответ на задание не проверен за 5 дней."
