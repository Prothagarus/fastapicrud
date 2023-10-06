#//fastAPI\crud_todo\schemas.py
from typing import List
from pydantic import BaseModel
 
# Create ToDo Schema (Pydantic Model)
class ToDoCreate(BaseModel):
    task: str
 
# Complete ToDo Schema (Pydantic Model)
class ToDo(BaseModel):
    id: int
    task: str
    
    class Config:
        orm_mode = True

class ToDoList(BaseModel):
    dolist: List[ToDo]

