from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from typing import List, Optional

app = FastAPI()

def init_db():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        completed BOOLEAN DEFAULT 0
    )''')
    conn.commit()
    conn.close()

init_db()

class Task(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

@app.post("/items")
def create_task(task: Task):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, completed) VALUES (?, ?, ?)",
        (task.title, task.description, task.completed),
    )
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return {"id": task_id, **task.dict()}

@app.get("/items", response_model=List[Task])
def get_tasks():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    return [
        {"id": row[0], "title": row[1], "description": row[2], "completed": bool(row[3])}
        for row in rows
    ]

@app.get("/items/{item_id}")
def get_task(item_id: int):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (item_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"id": row[0], "title": row[1], "description": row[2], "completed": bool(row[3])}

@app.put("/items/{item_id}")
def update_task(item_id: int, task: Task):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET title = ?, description = ?, completed = ? WHERE id = ?",
        (task.title, task.description, task.completed, item_id),
    )
    conn.commit()
    updated_rows = cursor.rowcount
    conn.close()
    if updated_rows == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"id": item_id, **task.dict()}

@app.delete("/items/{item_id}")
def delete_task(item_id: int):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (item_id,))
    conn.commit()
    deleted_rows = cursor.rowcount
    conn.close()
    if deleted_rows == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
