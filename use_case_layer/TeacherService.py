from models import *
from repositories import *
from use_case_layer.UoW import unit_of_work

class TeacherService:
    def __init__(self, t_repo):
        self.t_repo = t_repo

    def create_teacher(self, surname: str, name: str, lastname: str, email: str, password: str, phone: str):
        new_teacher = Teacher(1, surname, name, lastname, email, password, phone)
        with unit_of_work() as session:
            self.t_repo = SQLRepository()
            self.t_repo.add(new_teacher)
        return 'Teacher is created'

    def get_all_teachers(self):
        with unit_of_work() as session:
            self.t_repo = SQLRepository()
            teachers = self.t_repo.get_all(Teacher)
            return teachers
