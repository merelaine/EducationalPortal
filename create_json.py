from repositories import *
from models import *

if __name__ == '__main__':
    stud_repo = StudentRepository()
    json_repo = JSONRepository("data.json")
    teacher_repo = TeacherRepository()
    course_repo = CourseRepository()


    new_student = Student(id=1, surname='Ivanov', name='Ivan', lastname='Ivanovich', email='ivan@gmail.com', password='123',
                        phone='123456')
    stud_repo.add(new_student)
    new_student = Student(id=2, surname='Petrov', name='Ivan', lastname='Ivanovich', email='pivan@gmail.com',
                          password='123',
                          phone='123456')
    stud_repo.add(new_student)

    new_t = Teacher(id=1, surname='Petrov', name='Ivan', lastname='Petrovich', email='pi@gmail.com',
                          password='123',
                          phone='123456')
    teacher_repo.add(new_t)

    new_c = Course(id=1, name='Course1', description='desc', duration=50, price=20000, teacher=1, students=[new_student])
    course_repo.add(new_c)

    json_repo.add(stud_repo.get_all())
    json_repo.add(teacher_repo.get_all())
    #json_repo.add(course_repo.get_all())


    #data_to_save = {
    #    "students": [student.__dict__ for student in stud_repo.get_all()],
    #    "teachers": [teacher.__dict__ for teacher in teacher_repo.get_all()],
    #    "courses": [course.__dict__ for course in course_repo.get_all()]
    #}
    #json_repo.add(data_to_save)