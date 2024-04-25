from models import *
from repositories import *

class StudentService:
    def __init__(self,stud_repo:StudentRepository):
        self.stud_repo = stud_repo

    def create_student(self, surname: str, name: str, lastname: str,email: str,password: str,phone: str):
        students = self.stud_repo.get_all()

        if len(students) > 0:
            last_id = students[-1].id + 1
        else:
            last_id = 0

        new_stud = Student(last_id,surname, name, lastname,email,password,phone)
        if new_stud.check_unique_email(students):
            self.stud_repo.add(new_stud)
            return 'Student is created'
        else:
            return 'Student is not created. E-mail is not unique.'