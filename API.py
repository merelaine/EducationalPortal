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
def create_teacher():
    data = request.get_json()
    surname = data['surname']
    name = data['name']
    lastname = data['lastname']
    email = data['email']
    password = data['password']
    phone = data['phone']

    result = teacher_service.create_teacher(surname, name, lastname, email, password, phone)
    return jsonify({"message": result})

@app.route('/courses')
def courses():
    # Здесь будет логика для работы с курсами
    return 'Это страница для курсов'

@app.route('/students')
def students():
    # Здесь будет логика для работы со студентами
    return 'Это страница для студентов'

if __name__ == '__main__':
    app.run()