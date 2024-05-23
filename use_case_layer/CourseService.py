from models import *
from repositories import *
from UoW import unit_of_work

class CourseService:
    def __init__(self,course_repo:CourseRepository,stud_repo:StudentRepository,teacher_repo:TeacherRepository, topic_repo: TopicRepository, task_repo: TaskRepository):
        self.course_repo = course_repo
        self.stud_repo = stud_repo
        self.teacher_repo = teacher_repo
        self.topic_repo = topic_repo
        self.task_repo = task_repo

    def create_course(self, name: str, description: str, duration: int, price: float, teacher_id: int):
        courses = self.course_repo.get_all()

        if len(courses) > 0:
            last_id = courses[-1].id + 1
        else:
            last_id = 0

        course_teacher = self.teacher_repo.get(teacher_id)
        if isinstance(course_teacher,Teacher) or course_teacher is None:
            new_course = Course(last_id,name,description,duration,price,course_teacher,[])
            with unit_of_work() as session:
                self.course_repo = SQLRepository(session)
                self.course_repo.add(new_course)
            return 'Course is created'
        else:
            return 'Set teacher or None'


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

    def create_topic(self, name: str, description: str, theory: str, course_id: Course):
        course = self.course_repo.get(course_id)
        topics = self.topic_repo.get_all()

        if len(topics) > 0:
            last_id = topics[-1].id + 1
        else:
            last_id = 0

        new_topic = Topic(last_id, name, description, theory, course)
        self.topic_repo.add(new_topic)
        return 'Topic is created'

    def create_task(self, name: str, description: str, type: str, answer:str, topic_id: Topic):
        topic = self.topic_repo.get(topic_id)
        tasks = self.task_repo.get_all()

        if len(tasks) > 0:
            last_id = tasks[-1].id + 1
        else:
            last_id = 0

        new_task = Task(last_id, name, description, type, answer, topic)
        self.topic_repo.add(new_task)
        return 'Task is created'

