
from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy.orm import declarative_base as Base

base = Base()


# Define ToDo class from Base
class ToDo(base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True,autoincrement=True)
    task = Column(String(256))
    startdate = Column(DateTime,nullable=True)
    enddate = Column(DateTime,nullable=True)
class ToDoTask(base):
    __tablename__ = "todotask"
    id = Column(Integer, primary_key=True,autoincrement=True)
    task = Column(String(256))