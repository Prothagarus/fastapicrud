from typing import List
import pytest
import unittest
from main import create_todo, update_todo_list, get_session
from models import ToDo
from database import SessionLocal


def oneentry():
    entry: ToDo = {"id": None, "task": "active"}
    return entry


def manyentries():
    entry: List[ToDo] = [{"id": None, "task": "task1"}, {"id": None, "task": "task2"}]
    return entry


def manyentriesupdate():
    entry: List[ToDo] = [
        {"id": "2", "task": "updatetask1"},
        {"id": "3", "task": "updatetask12"},
    ]
    return entry


def test_insert_one(oneentry):
    create_todo(oneentry)
    assert 1 == 1


def test_upsert_many(manyentries):
    update_todo_list(manyentries)


def test_upsert_many_update(manyentriesupdate):
    update_todo_list(manyentriesupdate)


test_insert_one(oneentry=oneentry())

test_upsert_many(manyentries=manyentries())

test_upsert_many_update(manyentriesupdate=manyentriesupdate())
