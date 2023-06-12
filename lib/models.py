#!usr
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship,backref

Base = declarative_base()
if __name__ == '__main__':
    engine = create_engine('sqlite:///task_manager.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


task_manager= Table(
    "task_manager", 
    Base.metadata,
    Column('task_id', ForeignKey('tasks.id'), primary_key=True),
    Column('manager_id', ForeignKey('managers.id'), primary_key=True),
    extend_existing=True,
)


class Manager(Base):
    __tablename__ = 'managers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    comments= relationship('Comment', backref= backref('manager'))
    tasks = relationship('Task',secondary=task_manager,back_populates='managers')

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    status = Column(String)
    due_date = Column(DateTime)
    comments= relationship('Comment', backref= backref('task'))
    managers = relationship('Manager',secondary=task_manager,back_populates='tasks')


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    created_at = Column(DateTime)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    manager_id= Column(Integer, ForeignKey('managers.id'))



    




 