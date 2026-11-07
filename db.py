import sqlite3
def db_init() -> None:
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

def get_all_tasks() -> None:
    conn = sqlite3.connect('task.db')
    cur = conn.cursor()
    cur.execute(" SELECT * FROM tasks")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()
 
if __name__ == "__main__":
    db_init()
    add_task_to_db("gg", "09.21")
    get_all_tasks()
