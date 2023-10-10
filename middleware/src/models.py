
from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy.orm import declarative_base as Base

base = Base()


# Define ToDo class from Base
class ToDo(base):
    __tablename__ = "todoQuery"
    id = Column(Integer, primary_key=True,autoincrement=True)
    task = Column(String(256))
    startdate = Column(String,nullable=True)
    enddate = Column(String,nullable=True)
    todoid = Column(Integer,nullable=True)
class ToDoTask(base):
    __tablename__ = "todotask"
    id = Column(Integer, primary_key=True,autoincrement=True)
    task = Column(String(256))
class ToDoSave(base):
    __tablename__ = "todosave"
    id = Column(Integer, primary_key=True,autoincrement=True)
    task = Column(String(256))
    startdate = Column(String,nullable=True)
    enddate = Column(String,nullable=True)
    todoid =  Column(Integer,nullable=True)