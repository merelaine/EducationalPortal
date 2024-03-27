from repositories import *
from models import *

if __name__ == '__main__':
    stud_repo = StudentRepository()

    new_student = Student(id=1, surname='Ivanov', name='Ivan', lastname='Ivanovich', email='ivan@gmail.com', password='123',
                        phone='123456')
    stud_repo.add(new_student)
    print("Добавлен новый студент:", new_student)

    new_student = Student(id=2, surname='Petrov', name='Ivan', lastname='Ivanovich', email='ivan@gmail.com',
                          password='123',
                          phone='123456')
    stud_repo.add(new_student)
    print("Добавлен новый студент:", new_student)

    retrieved_student = stud_repo.get(2)
    print("Получен студент:", retrieved_student)

    updated_student = Student(id=2, surname='Ivanov', name='Petr', lastname='Ivanovich', email='ivan@gmail.com', password='123',
                                phone='123456')
    stud_repo.update(updated_student)
    print("Обновлена информация о студенте:", updated_student)

    stud_repo.remove(updated_student)
    print("Удален студент с id", 2)

    all_students = stud_repo.get_all()
    print("Список всех студентов:")
    for student in all_students:
        print(student)

    teacher_repo = TeacherRepository()
    teacher = Teacher(id=1,surname='Teacher',name='T',lastname='T',email='a@gmail.com',password='123',phone='123321')

    course_repo = CourseRepository()
    course = Course(id=1,name='Course1',description='Desc1',duration=32,price=100000,teacher=1,students=[stud_repo.get(1)])

    topic_repo = TopicRepository()
    topic = Topic(id=1,name='Topic1',description='desc',theory='cool theory bro',course=1)

    task_repo = TaskRepository()
    task = Task(id=1,name='task1', description='description', type='make an enum type',answer='answer',topic=1,teacher=1)

    studtask_repo = StudTaskRepository()
    studtask = Student_Task(id=1,student=1,task=1,score=5,time=300)

    print('В системе записана следующая попытка ответа на задание: Студент ' + stud_repo.get(1).surname + ' выполнил задание на оценку '+str(studtask.score))