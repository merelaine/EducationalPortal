from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class StudentTable(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String)
    name = Column(String)
    lastname = Column(String)
    email = Column(String)
    password = Column(String)
    phone = Column(String)

class TeacherTable(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    surname = Column(String)
    name = Column(String)
    lastname = Column(String)
    email = Column(String)
    password = Column(String)
    phone = Column(String)


class StudentCourse(Base):
    __tablename__ = 'student_course'
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

class CourseTable(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    duration = Column(Integer)
    price = Column(Integer)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship("TeacherTable")
    students = relationship("StudentTable", secondary="student_course")

class TopicTable(Base):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    theory = Column(String)
    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship("CourseTable")

class TaskTable(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    type = Column(String)
    answer = Column(String)
    topic_id = Column(Integer, ForeignKey('topics.id'))
    topic = relationship("TopicTable")

class StudentTaskTable(Base):
    __tablename__ = 'student_tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship("StudentTable")
    task_id = Column(Integer, ForeignKey('tasks.id'))
    task = relationship("TaskTable")
    score = Column(Integer)
    time = Column(Integer)
    date = Column(String)