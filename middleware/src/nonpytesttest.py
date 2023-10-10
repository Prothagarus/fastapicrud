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

