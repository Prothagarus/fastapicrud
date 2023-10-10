# //fastAPI\crud_todo\schemas.py
from typing import List, Optional
from pydantic import BaseModel,Field
from datetime import datetime

# Create ToDo Schema (Pydantic Model)
class ToDoCreate(BaseModel):
    task: str
class ToDoTask(BaseModel):
    task: str
class ToDoTaskList(BaseModel):
    tasklist: List[ToDoTask]

# Complete ToDo Schema (Pydantic Model)
class ToDo(BaseModel):
    id: Optional[int]
    task: str
    startdate: Optional[datetime] = Field(None)
    enddate: Optional[datetime] = Field(None)
    class Config:
        from_attributes = True


class ToDoList(BaseModel):
    dolist: List[ToDo]
