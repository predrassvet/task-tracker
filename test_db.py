import pytest
import db
from db import add_task_to_db, init_db, get_all_tasks, count_tasks, mark_done

def test_add_task_to_db(tmp_path, monkeypatch):
    database = tmp_path / "task.db"
    monkeypatch.setattr(db, "DB_PATH", database)
    init_db()
    add_task_to_db("test", "09-12-2020")
    tasks = get_all_tasks()
    assert count_tasks() == 1
    assert tasks[0][1] == 'test'

def test_mark_done(tmp_path, monkeypatch):
    database = tmp_path / "task.db"
    monkeypatch.setattr(db, "DB_PATH", database)
    init_db()
    add_task_to_db("test", "09-12-2020")
    mark_done(1)
    tasks = get_all_tasks()
    print(tasks)
    assert tasks[0][3] == True