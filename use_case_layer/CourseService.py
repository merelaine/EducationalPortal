from models import *
from repositories import *

class CourseService:
    def __init__(self,course_repo:CourseRepository,stud_repo:StudentRepository,teacher_repo:TeacherRepository):
        self.course_repo = course_repo
        self.stud_repo = stud_repo
        self.teacher_repo = teacher_repo

    def create_course(self,name: str, description:str, duration:int,price:float,teacher):
        courses = self.course_repo.get_all()

        if len(courses) > 0:
            last_id = courses[-1].id + 1
        else:
            last_id = 0

        if isinstance(teacher,Teacher):
            teacher_id = teacher.id
        elif teacher is None:
            teacher_id = None
        else:
            return 'Set teacher or None'
        new_course = Course(last_id,name,description,duration,price,teacher_id,[])
        self.course_repo.add(new_course)

        return True

    def add_student_to_course(self,student:Student,course:Course):
        if course.enroll_student(student, self.course_repo.get_all()):
            selected_course = self.course_repo.get(course.id)
            selected_course.students.add(student.id)
            return True
        else:
            return False

    def add_teacher_to_course(self,teacher:Teacher,course:Course):
        if course.assign_teacher(teacher,self.course_repo.get_all()):
            selected_course = self.course_repo.get(course.id)
            selected_course.teacher.add(teacher.id)
            return True
        else:
            return False
