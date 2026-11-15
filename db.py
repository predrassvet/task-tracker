from collections.abc import Iterator 
import sqlite3
def init_db() -> None:
    conn = sqlite3.connect('task.db')
    cur = conn.cursor()
    cur.execute(''' CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY, task_name TEXT NOT NULL, deadline TEXT NOT NULL, done BOOLEAN DEFAULT False)''' )
    conn.commit()
    conn.close()

def add_task_to_db(task_name: str, deadline: str) -> None:
    conn = sqlite3.connect('task.db')
    cur = conn.cursor()
    cur.execute(" INSERT INTO tasks (task_name, deadline) VALUES (?, ?)",(task_name, deadline))
    conn.commit()
    conn.close()

def get_all_tasks() -> list:
    conn = sqlite3.connect('task.db')
    cur = conn.cursor()
    cur.execute(" SELECT * FROM tasks")
    rows = cur.fetchall() 
    conn.close()
    return rows

def mark_done(task_id: int) -> None:
    conn = sqlite3.connect('task.db')
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET done = True WHERE tasks.id = (?)", (task_id, ))
    conn.commit()
    conn.close()

def delete_task(task_id: int) -> None:
    conn = sqlite3.connect('task.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id = ?", (task_id, ))
    conn.commit()
    conn.close()

def iter_task() -> Iterator[tuple]:
    conn = sqlite3.connect('task.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    for task in cur:
        yield task
    conn.close()

def iter_undone_tasks() -> Iterator[tuple]:
    conn = sqlite3.connect('task.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE done != 1")
    for task in cur:
        yield task
    conn.close()

def count_tasks() ->int:
    conn = sqlite3.connect("task.db")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM tasks")
    count = cur.fetchone()
    conn.close()   
    return count[0]


if __name__ == "__main__":
    n = iter_task()
    for i in n:
        print(i)
    for i in n:
        print(i)
    j = iter_undone_tasks()
    for i in j:
        print(i)
    h = count_tasks()
    print(h)