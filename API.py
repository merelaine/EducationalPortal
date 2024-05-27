from flask import Flask, request, jsonify, render_template, redirect, url_for
from models import Course, Student, Teacher, Topic, Task
from repositories import *
from use_case_layer.CourseService import CourseService
from use_case_layer.StudentService import StudentService
from use_case_layer.TeacherService import TeacherService
from use_case_layer.UoW import unit_of_work
import json

app = Flask(__name__)

course_repo = CourseRepository()
student_repo = StudentRepository()
teacher_repo = TeacherRepository()
topic_repo = TopicRepository()
task_repo = TaskRepository()

course_service = CourseService(course_repo, student_repo, teacher_repo, topic_repo, task_repo)
student_service = StudentService(student_repo)
#teacher_service = TeacherService(teacher_repo)

with unit_of_work() as session:
    repo = SQLRepository()
teacher_service = TeacherService(repo)


@app.route('/')
def index():
    return '''
    <h1>Добро пожаловать!</h1>
    <p><a href="/teachers">Учителя</a></p>
    <p><a href="/courses">Курсы</a></p>
    <p><a href="/students">Студенты</a></p>
    '''

@app.route('/teachers', methods=['GET'])
def get_all_teachers():
    teachers = teacher_service.get_all_teachers()
    serialized_teachers = [teacher.serialize() for teacher in teachers]
    return json.dumps(serialized_teachers)

@app.route('/teachers', methods=['POST'])
def create_teacher():
    data = request.json
    surname = data['surname']
    name = data['name']
    lastname = data['lastname']
    email = data['email']
    password = data['password']
    phone = data['phone']

    teacher_service.create_teacher(surname, name, lastname, email, password, phone)
    return 'Teacher is created'

@app.route('/students')
def get_all_students():
    students = student_service.get_all_students()
    serialized_students = [student.serialize() for student in students]
    return render_template('all_students.html', students=serialized_students)


@app.route('/students/new', methods=['GET', 'POST'])
def create_student():
    if request.method == 'POST':
        surname = request.form['surname']
        name = request.form['name']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']

        result = student_service.create_student(surname, name, lastname, email, password, phone)

        if result == 'Student is created':
            return redirect(url_for('get_all_students'))
        else:
            return 'Student is not created. E-mail is not unique.'

    return render_template('create_student.html')

@app.route('/courses')
def courses():
    return 'Это страница для курсов'

if __name__ == '__main__':
    app.run()