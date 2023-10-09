from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base as Base

base = Base()


# Define ToDo class from Base
class ToDo(base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    task = Column(String(256))
