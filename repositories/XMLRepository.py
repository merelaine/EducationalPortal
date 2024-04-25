from models import *
import xml.etree.ElementTree as ET

class XMLRepository():
    def __init__(self, file_path):
        self.file_path = file_path
        self.data_list = []

    def read_data(self, **class_repo):
        tree = ET.parse(self.file_path)
        root = tree.getroot()

        for element in root:
            tag = element.tag
            if tag in class_repo:
                model_obj = self.xml_to_model(tag, element, class_repo)
                class_repo[tag].add(model_obj)

    def xml_to_model(self, tag, element, class_repo):
        if tag == "Student":
            return self.xml_to_student(element)
        elif tag == "Teacher":
            return self.xml_to_teacher(element)
        elif tag == "Course":
            return self.xml_to_course(element,class_repo['Teacher'])
        elif tag == "Topic":
            return self.xml_to_topic(element,class_repo['Course'])
        elif tag == "Task":
            return self.xml_to_task(element,class_repo['Topic'])
        elif tag == "StudentTask":
            return self.xml_to_studtask(element,class_repo['Student'],class_repo['Task'])

    @staticmethod
    def xml_to_student(xml_element):
        id_element = xml_element.find("id")
        surname_element = xml_element.find("surname")
        name_element = xml_element.find("name")
        lastname_element = xml_element.find("lastname")
        email_element = xml_element.find("email")
        password_element = xml_element.find("password")
        phone_element = xml_element.find("phone")

        student = Student(int(id_element.text),surname_element.text,name_element.text,lastname_element.text,email_element.text,password_element.text,phone_element.text)

        return student

    @staticmethod
    def xml_to_teacher(xml_element):
        id_element = xml_element.find("id")
        surname_element = xml_element.find("surname")
        name_element = xml_element.find("name")
        lastname_element = xml_element.find("lastname")
        email_element = xml_element.find("email")
        password_element = xml_element.find("password")
        phone_element = xml_element.find("phone")

        teacher = Teacher(int(id_element.text),surname_element.text,name_element.text,lastname_element.text,email_element.text,password_element.text,phone_element.text)

        return teacher

    @staticmethod
    def xml_to_course(xml_element,repo):
        id_element = xml_element.find("id")
        name_element = xml_element.find("name")
        description_element = xml_element.find("description")
        duration_element = xml_element.find("duration")
        price_element = xml_element.find("price")
        teacher_element = xml_element.find("teacher")

        course = Course(int(id_element.text), name_element.text, description_element.text, duration_element.text, float(price_element.text),repo.get(int(teacher_element.text)))

        return course

    @staticmethod
    def xml_to_topic(xml_element,repo):
        id_element = xml_element.find("id")
        name_element = xml_element.find("name")
        description_element = xml_element.find("description")
        theory_element = xml_element.find("theory")
        course_element = xml_element.find("course")

        topic = Topic(int(id_element.text),name_element.text,description_element.text,theory_element.text,repo.get(int(course_element.text)))

        return topic

    @staticmethod
    def xml_to_task(xml_element,repo):
        id_element = xml_element.find("id")
        name_element = xml_element.find("name")
        description_element = xml_element.find("description")
        type_element = xml_element.find("type")
        answer_element = xml_element.find("answer")
        topic_element = xml_element.find("topic")

        task = Task(int(id_element.text), name_element.text,description_element.text,type_element.text,answer_element.text,repo.get(int(topic_element.text)))

        return task

    @staticmethod
    def xml_to_studtask(xml_element,srepo,trepo):
        id_element = xml_element.find("id")
        stud_element = xml_element.find("student")
        task_element = xml_element.find("task")
        score_element = xml_element.find("score")
        time_element = xml_element.find("time")
        date_element = xml_element.find("date")

        studtask = Student_Task(int(id_element.text),srepo.get(int(stud_element.text)),trepo.get(int(task_element.text)),int(score_element.text),int(time_element.text),date_element.text)

        return studtask

    def save_to_xml(self):
        root_element = ET.Element("data_list")

        for data in self.data_list:
            if isinstance(data, Student):
                root_element.append(self.student_to_xml(data))
            elif isinstance(data, Course):
                root_element.append(self.course_to_xml(data))
            elif isinstance(data, Teacher):
                root_element.append(self.teacher_to_xml(data))
            elif isinstance(data, Topic):
                root_element.append(self.topic_to_xml(data))
            elif isinstance(data, Task):
                root_element.append(self.task_to_xml(data))
            elif isinstance(data, Student_Task):
                root_element.append(self.studtask_to_xml(data))

        tree = ET.ElementTree(root_element)
        tree.write(self.file_path)

    def student_to_xml(self, student):
        student_element = ET.Element("Student")
        id_element = ET.SubElement(student_element, "id")
        id_element.text = str(student.id)
        surname_element = ET.SubElement(student_element, "surname")
        surname_element.text = student.surname
        name_element = ET.SubElement(student_element, "name")
        name_element.text = student.name
        lastname_element = ET.SubElement(student_element, "lastname")
        lastname_element.text = student.lastname
        email_element = ET.SubElement(student_element, "email")
        email_element.text = student.email
        password_element = ET.SubElement(student_element, "password")
        password_element.text = student.password
        phone_element = ET.SubElement(student_element, "phone")
        phone_element.text = student.phone
        return student_element

    def teacher_to_xml(self, teacher):
        teacher_element = ET.Element("Teacher")
        id_element = ET.SubElement(teacher_element, "id")
        id_element.text = str(teacher.id)
        surname_element = ET.SubElement(teacher_element, "surname")
        surname_element.text = teacher.surname
        name_element = ET.SubElement(teacher_element, "name")
        name_element.text = teacher.name
        lastname_element = ET.SubElement(teacher_element, "lastname")
        lastname_element.text = teacher.lastname
        email_element = ET.SubElement(teacher_element, "email")
        email_element.text = teacher.email
        password_element = ET.SubElement(teacher_element, "password")
        password_element.text = teacher.password
        phone_element = ET.SubElement(teacher_element, "phone")
        phone_element.text = teacher.phone
        return teacher_element

    def course_to_xml(self, course):
        course_element = ET.Element("Teacher")
        id_element = ET.SubElement(course_element, "id")
        id_element.text = str(course.id)
        name_element = ET.SubElement(course_element, "name")
        name_element.text = course.name
        description_element = ET.SubElement(course_element, "description")
        description_element.text = course.description
        duration_element = ET.SubElement(course_element, "duration")
        duration_element.text = course.duration
        price_element = ET.SubElement(course_element, "price")
        price_element.text = str(course.price)
        teacher_element = ET.SubElement(course_element, "teacher")
        teacher_element.text = str(course.teacher.id)
        studs_element = ET.SubElement(course_element,"students")

        return course_element

    def topic_to_xml(self, topic):
        topic_element = ET.Element("Topic")
        id_element = ET.SubElement(topic_element, "id")
        id_element.text = str(topic.id)
        name_element = ET.SubElement(topic_element, "name")
        name_element.text = topic.name
        description_element = ET.SubElement(topic_element, "description")
        description_element.text = topic.description
        theory_element = ET.SubElement(topic_element, "theory")
        theory_element.text = topic.theory
        course_element = ET.SubElement(topic_element, "course")
        course_element.text = str(topic.course.id)
        return topic_element

    def task_to_xml(self, task):
        task_element = ET.Element("Task")
        id_element = ET.SubElement(task_element, "id")
        id_element.text = str(task.id)
        name_element = ET.SubElement(task_element, "name")
        name_element.text = task.name
        description_element = ET.SubElement(task_element, "description")
        description_element.text = task.description
        type_element = ET.SubElement(task_element, "type")
        type_element.text = task.type
        answer_element = ET.SubElement(task_element, "answer")
        answer_element.text = task.answer
        topic_element = ET.SubElement(task_element, "course")
        topic_element.text = str(task.topic.id)
        return task_element

    def studtask_to_xml(self, studtask):
        studtask_elem = ET.Element("StudentTask")
        id_element = ET.SubElement(studtask_elem, "id")
        id_element.text = str(studtask.id)
        stud_element = ET.SubElement(studtask_elem, "student")
        stud_element.text = str(studtask.student.id)
        task_element = ET.SubElement(studtask_elem, "task")
        task_element.text = str(studtask.task.id)
        score_element = ET.SubElement(studtask_elem, "score")
        score_element.text = str(studtask.score)
        time_element = ET.SubElement(studtask_elem, "time")
        time_element.text = str(studtask.time)
        date_element = ET.SubElement(studtask_elem, "date")
        date_element.text = str(studtask.date)
        return studtask_elem