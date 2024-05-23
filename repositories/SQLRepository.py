from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, class_mapper
from repository import Repository
from models import *

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


student_course = Table('student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

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


class SQLRepository(Repository):
    def __init__(self):
        super().__init__()
        self.table_mapping = {
            Student: StudentTable,
            Teacher: TeacherTable,
            Course: CourseTable,
            Topic: TopicTable,
            Task: TaskTable,
            Student_Task: StudentTaskTable
        }
        self.engine = create_engine("sqlite:///database.db")
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add(self, item):
        session = self.Session()

        item_class = item.__class__
        table_class = self.table_mapping.get(item_class)

        if table_class:
            mapper = class_mapper(table_class)
            attributes = {key: getattr(item, key) for key in mapper.columns.keys() if key != 'id'}
            table_instance = table_class(**attributes)
            session.add(table_instance)
            session.commit()
            session.close()
        else:
            raise ValueError("Unsupported item type")

    def remove(self, item_id, item_class):
        session = self.Session()
        table_class = self.table_mapping.get(item_class)
        result = session.query(table_class).filter_by(id=item_id).first()
        if result:
            session.delete(result)
            session.commit()
            session.close()
        else:
            raise ValueError(f"{item_class.__name__} not found")

    def get(self, item_id, item_class):
        session = self.Session()
        table_class = self.table_mapping.get(item_class)
        result = session.query(table_class).filter_by(id=item_id).first()
        session.close()
        return result

    def get_all(self, item_class):
        session = self.Session()
        table_class = self.table_mapping.get(item_class)
        result = session.query(table_class).all()
        session.close()
        return result

    def update(self, item):
        session = self.Session()
        item_class = item.__class__
        table_class = self.table_mapping.get(item_class)
        result = session.query(table_class).filter_by(id=item.id).first()
        if result:
            for key in item.__dict__.keys():
                if key != 'id' and hasattr(result, key):
                    setattr(result, key, getattr(item, key))
            session.commit()
            session.close()
        else:
            raise ValueError(f"{item_class.__name__} not found")

if __name__ == '__main__':
    sqlrepo = SQLRepository()
    stud = Student(1,'lk','g','уg','f','345','3568776')
    sqlrepo.add(stud)
    print(sqlrepo.get_all(stud.__class__))
    sqlrepo.remove(5,Student)