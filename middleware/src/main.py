from datetime import datetime
from typing import List
from fastapi import FastAPI, Query, status, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from database import engine, SessionLocal
from sqlalchemy.orm import Session, declarative_base
import models as models
import schemas as schemas
import uvicorn

declarative_base().metadata.create_all(engine)  # Create the database

# Initialize app
def create_app():

    app = FastAPI(
        title="ToDo Backend",
        description="API backend to save to a sql lite database",
        version="0",
        dependencies=[])
    origins = ["http://localhost:8080","http://localhost:8043","http://localhost:5173"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app
    
app = create_app()


# Helper function to get database session
def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()




@app.get("/")
def root():
    return "todo"


# @app.post("/todo", response_model=schemas.ToDo, status_code=status.HTTP_201_CREATED)
# def create_todo(todo: schemas.ToDoCreate):#, session: Session = Depends(get_session)):
#     session = SessionLocal()
#     tododb = models.ToDoSave(id=None, task=todo["task"], startdate=todo["startdate"], enddate=todo["enddate"],todoid =None)
#     session.add(tododb)
#     session.commit()
#     session.refresh(tododb)
#     return tododb

@app.get("/todo/{id}", response_model=schemas.ToDo)
def read_todo(id: int):  # , session: Session = Depends(get_session)):
    session = SessionLocal()
    todo = session.query(models.ToDo).get(id)  # get item with the given id

    # check if id exists. If not, return 404 not found response
    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return todo

@app.get("/ToDoGet/", response_model=List[schemas.ToDo])
def read_todo():  # , session: Session = Depends(get_session)):
    session = SessionLocal()
   
    todo = session.query(models.ToDo).all()  # get all todo items
    return [schemas.ToDo.model_validate(item) for item in todo]
@app.post("/ToDo_Save/", response_model=List[schemas.ToDo])
def update_todo_list(
    payload: List[schemas.ToDo],  # , session: Session = Depends(get_session)
):
    session = SessionLocal()
    todos = []  # Initialize todos to an empty list
    for item in payload:
        if item["id"] == None and item["todoid"] == None:
            todo = models.ToDoSave(id=None, task=item["task"], startdate=item["startdate"], enddate=item["enddate"], todoid=None)
            session.add(todo)
            session.commit()
            todos.append(todo)
        if item["id"] != None and item["todoid"] == None:
            todo = session.query(models.ToDoSave).filter(models.ToDoSave.id == item["id"]).first()
            todo.task = item["task"]
            todo.startdate = item["startdate"]
            todo.enddate = item["enddate"]
            todo.todoid = item["id"]
            session.commit()
            todos.append(todo)
        if item["id"] == None and item["todoid"] != None:
            todo = session.query(models.ToDoSave).filter(models.ToDoSave.id == item["todoid"]).first()
            todo.task = item["task"]
            todo.startdate = item["startdate"]
            todo.enddate = item["enddate"]
            session.commit()
            todos.append(todo)
    return todos

        # itemexist = (
        #     session.query(models.ToDo).filter(models.ToDo.id == todo["id"]).first()
        # )  # get given id

        # if itemexist == None:
        #     todo = models.ToDoSave(id=None, task=todo["task"],startdate=todo["startdate"],enddate=todo["enddate"],todoid =None)
        #     session.add(todo)
        #     session.commit()

        # # check if id exists. If not, return 404 not found response
        # if itemexist:
        #     itemexist.task = todo["task"]
        #     itemexist.startdate=todo["startdate"]
        #     itemexist.enddate=todo["enddate"]
        #     session.commit()

    return todo

@app.get("/ToDo_DropdownList", response_model=List[schemas.ToDoTask])
def read_todo_list(session: Session = Depends(get_session)):
    todotask_list = session.query(models.ToDoTask).distinct(models.ToDoTask.task).all()  # get distinct todo tasks
    return todotask_list
@app.delete("/todo/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id: int, session: Session = Depends(get_session)):
    # get the given id
    todo = session.query(models.ToDo).get(id)

    # if todo item with given id exists, delete it from the database. Otherwise raise 404 error
    if todo:
        session.delete(todo)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return None


@app.get("/todo", response_model=List[schemas.ToDo])
def read_todo_list(session: Session = Depends(get_session)):
    todo_list = session.query(models.ToDo).all()  # get all todo items

    return todo_list

@app.get("/todo/date", response_model=List[schemas.ToDo])
def read_todo_by_date(startdate: datetime = Query(None), enddate: datetime = Query(None), session: Session = Depends(get_session)):
    if startdate is None or enddate is None:
        raise HTTPException(status_code=400, detail="Both startdate and enddate must be provided")
    todo_list = session.query(models.ToDo).filter(models.ToDo.startdate >= startdate, models.ToDo.enddate <= enddate).all()
    return todo_list

def appcli():
    uvicorn.run(

        app="__main__:app",
        host="127.0.0.1",
        port=8043,
        reload=True
    )
if __name__ =="__main__":
    appcli()