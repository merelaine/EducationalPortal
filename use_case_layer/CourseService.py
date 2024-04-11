from models import *
from repositories import *

class CourseService:
    def __init__(self,course_repo:CourseRepository,stud_repo:StudentRepository,teacher_repo:TeacherRepository):
        self.course_repo = course_repo
        self.stud_repo = stud_repo
        self.teacher_repo = teacher_repo

    def create_course(self, name: str, description: str, duration: int, price: float, course_teacher):
        courses = self.course_repo.get_all()

        if len(courses) > 0:
            last_id = courses[-1].id + 1
        else:
            last_id = 0

        if isinstance(course_teacher,Teacher):
            teacher_id = course_teacher.id
        elif course_teacher is None:
            teacher_id = None
        else:
            return 'Set teacher or None'
        new_course = Course(last_id,name,description,duration,price,teacher_id,[])
        self.course_repo.add(new_course)

        return 'Course is created'

    def add_student_to_course(self, student_to_add: Student, course_to_add: Course):
        if course_to_add.enroll_student(student_to_add, self.course_repo.get_all()):
            selected_course = self.course_repo.get(course_to_add.id)
            selected_course.students.add(student_to_add.id)
            return 'Student is added'
        else:
            return 'Student is not added'

    def add_teacher_to_course(self, teacher_to_add: Teacher, course_to_add: Course):
        if course_to_add.assign_teacher(teacher_to_add, self.course_repo.get_all()):
            selected_course = self.course_repo.get(course_to_add.id)
            selected_course.teacher.add(teacher_to_add.id)
            return 'Teacher is added'
        else:
            return 'Teacher is not added'
