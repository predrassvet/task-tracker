import pytest
import db
from db import add_task_to_db, init_db, get_all_tasks, count_tasks, mark_done, delete_task, iter_undone_tasks

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

def test_delete_task(tmp_path, monkeypatch):
    database = tmp_path / "task.db"
    monkeypatch.setattr(db, "DB_PATH", database)
    init_db()
    add_task_to_db("name", "09-12-2024")
    delete_task(1)
    assert count_tasks() == 0

def test_iter_undone_tasks(tmp_path, monkeypatch):
    database = tmp_path / "task.db"
    monkeypatch.setattr(db, "DB_PATH", database)
    init_db()
    add_task_to_db("work", "09-10-1997")
    add_task_to_db("read", "09-10-997")
    add_task_to_db("relax", "09-10-1897")
    mark_done(2)
    g = []
    for task in iter_undone_tasks():
        g.append(task[1])
    assert len(g) == 2
    assert "read" not in g
    