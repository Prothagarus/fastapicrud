# //fastAPI\crud_todo\schemas.py
from typing import List, Optional
from pydantic import BaseModel


# Create ToDo Schema (Pydantic Model)
class ToDoCreate(BaseModel):
    task: str


# Complete ToDo Schema (Pydantic Model)
class ToDo(BaseModel):
    id: Optional[int]
    task: str

    class Config:
        from_attributes = True


class ToDoList(BaseModel):
    dolist: List[ToDo]
