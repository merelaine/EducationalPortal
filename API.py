from flask import Flask, request, jsonify
from models import Course, Student, Teacher, Topic, Task
from repositories import CourseRepository, StudentRepository, TeacherRepository, TopicRepository, TaskRepository
from use_case_layer.CourseService import CourseService
from use_case_layer.StudentService import StudentService
from use_case_layer.TeacherService import TeacherService

app = Flask(__name__)

course_repo = CourseRepository()
student_repo = StudentRepository()
teacher_repo = TeacherRepository()
topic_repo = TopicRepository()
task_repo = TaskRepository()

course_service = CourseService(course_repo, student_repo, teacher_repo, topic_repo, task_repo)
student_service = StudentService(student_repo)
teacher_service = TeacherService(teacher_repo)

@app.route('/')
def index():
    return '''
    <h1>Добро пожаловать!</h1>
    <p><a href="/teachers">Учителя</a></p>
    <p><a href="/courses">Курсы</a></p>
    <p><a href="/students">Студенты</a></p>
    '''

@app.route('/teachers', methods=['POST'])
def teachers():
    return 'Это страница для учителей'

@app.route('/courses')
def courses():
    return 'Это страница для курсов'

@app.route('/students')
def students():
    return 'Это страница для студентов'

if __name__ == '__main__':
    app.run()