from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
import sqlite3
import string
import random

app = FastAPI()

def init_db():
    conn = sqlite3.connect("shorturl.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short_id TEXT UNIQUE NOT NULL,
            full_url TEXT NOT NULL,
            visits INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

init_db()

class URLRequest(BaseModel):
    url: HttpUrl

class URLStats(BaseModel):
    short_id: str
    full_url: str
    visits: int

def generate_short_id(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.post("/shorten")
def create_short_url(request: URLRequest):
    short_id = generate_short_id()
    conn = sqlite3.connect("shorturl.db")
    cursor = conn.cursor()

    while True:
        cursor.execute("SELECT 1 FROM urls WHERE short_id = ?", (short_id,))
        if cursor.fetchone() is None:
            break
        short_id = generate_short_id()

    cursor.execute(
        "INSERT INTO urls (short_id, full_url) VALUES (?, ?)",
        (short_id, str(request.url)),  # Преобразование HttpUrl в строку
    )
    conn.commit()
    conn.close()

    return {"short_url": f"http://127.0.0.1:8001/{short_id}"}

@app.get("/{short_id}")
def redirect_to_full_url(short_id: str):
    conn = sqlite3.connect("shorturl.db")
    cursor = conn.cursor()
    cursor.execute("SELECT full_url, visits FROM urls WHERE short_id = ?", (short_id,))
    result = cursor.fetchone()

    if result is None:
        raise HTTPException(status_code=404, detail="Short URL not found")

    full_url, visits = result
    cursor.execute(
        "UPDATE urls SET visits = ? WHERE short_id = ?",
        (visits + 1, short_id),
    )
    conn.commit()
    conn.close()

    return {"redirect_to": full_url}

@app.get("/stats/{short_id}", response_model=URLStats)
def get_url_stats(short_id: str):
    conn = sqlite3.connect("shorturl.db")
    cursor = conn.cursor()
    cursor.execute("SELECT short_id, full_url, visits FROM urls WHERE short_id = ?", (short_id,))
    result = cursor.fetchone()
    conn.close()

    if result is None:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return {"short_id": result[0], "full_url": result[1], "visits": result[2]}