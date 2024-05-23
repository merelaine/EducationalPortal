from models import *
from repositories import *
from UoW import unit_of_work


class TeacherService:
    def __init__(self, t_repo):
        self.t_repo = t_repo

    def create_teacher(self, surname: str, name: str, lastname: str, email: str, password: str, phone: str):
        teachers = self.t_repo.get_all()

        if len(teachers) > 0:
            last_id = teachers[-1].id + 1
        else:
            last_id = 0

        new_teacher = Teacher(last_id, surname, name, lastname, email, password, phone)
        self.t_repo.add(new_teacher)
        return 'Teacher is created'
