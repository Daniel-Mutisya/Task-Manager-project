#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ipdb;


if __name__ == '__main__':
    
   engine = create_engine('sqlite:///task_manager.db')
   Session = sessionmaker(bind=engine)
   session = Session()

   from models import Manager, Task, Comment 


   User1 = Manager(username="Jack", email="jacksmontel@gmail.com")
   User2= Manager(username="Washington", email="washingtonbaily@gmail.com")

   Task1 = Task(title="Communication", description="Send out emails", status="Pending", due_date="Tomorrow")
   Task2 = Task(title="Dispatch", description="Dispatch universal health cards", status="In progress", due_date="Tomorrow")


   ipdb.set_trace()