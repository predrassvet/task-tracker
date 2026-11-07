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

if __name__ == "__main__":
    init_db()
    #add_task_to_db("gg", "09.21")
    test = get_all_tasks()
    for task in test:
        print(task)
    #mark_done(5)
    #delete_task(4)
