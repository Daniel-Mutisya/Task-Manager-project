#!usr/bin/env python3
from sqlalchemy import create_engine,insert
from sqlalchemy.orm import sessionmaker
from models import Task, Manager, Comment, task_manager
from datetime import datetime
import random
if __name__== '__main__':
  engine = create_engine('sqlite:///task_manager.db')
  Session = sessionmaker(bind=engine)
  session = Session()
  session.query(Task).delete()
  session.query(Manager).delete()
  session.query(Comment).delete()
def seeds_data():
    managers = [
    Manager(name="manager1", email='manager1@example.com'),
    Manager(name='manager2', email='manager@example.com'),
    Manager(name='manager3', email='manager@example.com')
    ]
    session.add_all(managers)

    tasks = [
        Task(title='Task 1', description='Description of Task 1', status='done!', due_date=datetime.now()),
        Task(title='Task 2', description='Description of Task 2', status='postponed', due_date=datetime.now())
    ]
    session.add_all(tasks)
    comments= [
       Comment(content='This task is very difficult',created_at=datetime.now(), task_id= random.randint(1,2),manager_id= random.randint(1,3)),
       Comment(content='To be delivered',created_at=datetime.now(), task_id= random.randint(1,2),manager_id= random.randint(1,3)),
       Comment(content='Successfully achieved objectives',created_at=datetime.now(), task_id= random.randint(1,2),manager_id= random.randint(1,3)),
       Comment(content='I like it',created_at=datetime.now(), task_id= random.randint(1,2),manager_id= random.randint(1,3)),
    ]

    session.add_all(comments)
    combinations= set()
    for _ in range (5):
       task_id= random.randint(1,2)
       manager_id= random.randint(1,3)
       if (task_id, manager_id) in combinations:
          continue
       combinations.add((task_id, manager_id))
       task_manager_data={'task_id': task_id, 'manager_id': manager_id}
       statement= insert(task_manager).values(task_manager_data)
       session.execute(statement)
       session.commit()
    session.commit()
    session.close()

seeds_data()