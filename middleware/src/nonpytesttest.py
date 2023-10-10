from typing import List
import pytest
import unittest
from main import  update_todo_list, get_session
from models import ToDo
from database import SessionLocal
from datetime import datetime
# test =''
# datetime.strftime(test, "%Y-%m-%d %H:%M:%S")
dt= datetime.now()
def oneentry():
    entry: List[ToDo] = [{"id": None, "task": "active","startdate":datetime.now(),"enddate":datetime.now(),"todoid":None}]
    return entry


def manyentries():
    entry: List[ToDo] = [{"id": None, "task": "delay","startdate":datetime.now(),"enddate":datetime.now(),"todoid":None}, {"id": None, "task": "active","startdate":datetime.now(),"enddate":datetime.now(),"todoid":None}]
    return entry


def manyentriesupdate():
    entry: List[ToDo] = [
        {"id": "2", "task": "maint","startdate":datetime.now(),"enddate":datetime.now(),"todoid":None},
        {"id": "3", "task": "maint","startdate":datetime.now(),"enddate":datetime.now(),"todoid":None},
    ]
    return entry
#[{"id":null,"task":"active","startdate":"2023-10-25T04:36:00.000Z","enddate":"2023-10-10T00:36:23.546-04:00","todoid":null},{"id":null,"task":"active","startdate":"2023-10-10T00:37:29.119-04:00","enddate":"2023-10-10T00:37:29.119-04:00","todoid":null},{"id":null,"task":"active","startdate":"2023-10-17T04:37:00.000Z","enddate":"2023-10-10T00:37:29.745-04:00","todoid":null}]

def test_insert_one(oneentry):
    update_todo_list(oneentry)
    assert 1 == 1


def test_upsert_many(manyentries):
    update_todo_list(manyentries)


def test_upsert_many_update(manyentriesupdate):
    update_todo_list(manyentriesupdate)


test_insert_one(oneentry=oneentry())

test_upsert_many(manyentries=manyentries())

test_upsert_many_update(manyentriesupdate=manyentriesupdate())

