from repositories import *
from models import *

if __name__ == '__main__':
    repo = StudentRepository()

    new_student = Student(id=1, surname='Ivanov', name='Ivan', lastname='Ivanovich', email='ivan@gmail.com', password='123',
                        phone='123456')
    repo.add(new_student)
    print("Добавлен новый студент:", new_student)

    new_student = Student(id=2, surname='Petrov', name='Ivan', lastname='Ivanovich', email='ivan@gmail.com',
                          password='123',
                          phone='123456')
    repo.add(new_student)
    print("Добавлен новый студент:", new_student)

    retrieved_student = repo.get(1)
    print("Получен студент:", retrieved_student)

    updated_student = Student(id=1, surname='Ivanov', name='Petr', lastname='Ivanovich', email='ivan@gmail.com', password='123',
                                phone='123456')
    repo.update(updated_student)
    print("Обновлена информация о студенте:", updated_student)

    repo.remove(updated_student)
    print("Удален студент с id", 1)

    all_students = repo.get_all()
    print("Список всех студентов:")
    for student in all_students:
        print(student)

