from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, class_mapper, Session
from .repository import Repository
from models import *
from models.DBmodels import StudentTable,TeacherTable,StudentCourse,CourseTable,TopicTable,TaskTable,StudentTaskTable

Base = declarative_base()

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
        #self.session = session

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


