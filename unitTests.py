import unittest
from models.student import Student
from models.task import Task
from models.student_task import Student_Task
from models.course import Course
from datetime import datetime,timedelta

class TestStudentTask(unittest.TestCase):
    class TestCourse(unittest.TestCase):

        def test_assign_teacher_success(self):
            teacher = Student(1, "Иванов", "Иван", "Иванович", "ivan@example.com", "password123", "123456789")
            course = Course(1, "Math Course", "Mathematics basics", "3 months", 100, None, [])
            all_courses = [course]

            self.assertTrue(course.assign_teacher(teacher, all_courses))# Присваиваем преподавателя успешно

        def test_assign_teacher_exceed_limit(self):
            teacher = Student(1, "Иванов", "Иван", "Иванович", "ivan@example.com", "password123", "123456789")
            course1 = Course(1, "Math Course", "Mathematics basics", "3 months", 100, teacher, [])
            course2 = Course(2, "Physics Course", "Physics fundamentals", "4 months", 120, teacher, [])
            course3 = Course(3, "Chemistry Course", "Chemistry principles", "3.5 months", 110, teacher, [])
            course4 = Course(4, "Biology Course", "Biology essentials", "2.5 months", 90, None, [])
            all_courses = [course1, course2, course3, course4]

            new_teacher = Student(2, "Петров", "Петр", "Петрович", "petr@example.com", "password456", "987654321")

            self.assertFalse(
                course4.assign_teacher(new_teacher, all_courses))  # Превышен лимит курсов для преподавателя

        def test_enroll_student_success(self):
            student = Student(1, "Иванов", "Иван", "Иванович", "ivan@example.com", "password123", "123456789")
            course = Course(1, "Math Course", "Mathematics basics", "3 months", 100, None, [])

            course.enroll_student(student)

            self.assertIn(student, course.students)  # Студент успешно записан на курс

        def test_enroll_student_exceed_limit(self):
            student = Student(1, "Иванов", "Иван", "Иванович", "ivan@example.com", "password123", "123456789")
            course = Course(1, "Math Course", "Mathematics basics", "3 months", 100, None, [
                Student(i, f"Student{i}", "Test", "Lastname", f"student{i}@example.com", "password", "123456789") for i
                in range(6)])

            course.enroll_student(student)

            self.assertNotIn(student, course.students)

    def test_check_score_by_time_within_5_days(self):
        current_date = datetime.now().date()
        submission_date = current_date - timedelta(days=3)  # задание было отправлено 3 дня назад
        student = Student(id=1, surname='Ivanov', name='Ivan', lastname='Ivanovich', email='ivan@gmail.com', password='123',
                        phone='123456')
        task = Task(id=1,name='task1', description='description', type='make an enum type',answer='answer',topic=1,teacher=1)
        student_task = Student_Task(1, student, task, 80, "2 hours", submission_date)

        expected_output = "Ответ на задание был проверен в течение 5 дней после отправки."
        self.assertEqual(student_task.check_score_by_time(), expected_output)

    def test_check_score_by_time_exceeds_5_days(self):
        current_date = datetime.now().date()
        submission_date = current_date - timedelta(days=7)  # задание было отправлено 7 дней назад
        student = Student(id=1, surname='Ivanov', name='Ivan', lastname='Ivanovich', email='ivan@gmail.com',
                          password='123',
                          phone='123456')
        task = Task(id=1, name='task1', description='description', type='make an enum type', answer='answer', topic=1,
                    teacher=1)
        student_task = Student_Task(2, student, task, 90, "1 hour", submission_date)

        expected_output = "Ответ на задание не проверен за 5 дней."
        self.assertEqual(student_task.check_score_by_time(), expected_output)


class TestStudent(unittest.TestCase):

    def test_check_unique_email_duplicate(self):
        student1 = Student(1, "Иванов", "Иван", "Иванович", "ivan@example.com", "password123", "123456789")
        student2 = Student(2, "Петров", "Петр", "Петрович", "ivan@example.com", "password456", "987654321")
        students_list = [student1, student2]

        self.assertFalse(student2.check_unique_email(students_list))  # Проверяем наличие дубликата email

    def test_check_unique_email_unique(self):
        student1 = Student(1, "Иванов", "Иван", "Иванович", "ivan@example.com", "password123", "123456789")
        student2 = Student(2, "Петров", "Петр", "Петрович", "petr@example.com", "password456", "987654321")
        students_list = [student1, student2]

        self.assertTrue(student2.check_unique_email(students_list))  # Проверяем уникальность email

if __name__ == '__main__':
    unittest.main()