import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

# TASKS TABLE
c.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_text TEXT NOT NULL,
    is_completed INTEGER DEFAULT 0,
    date TEXT
)
""")

# MOODS TABLE
c.execute("""
CREATE TABLE IF NOT EXISTS moods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mood TEXT,
    date TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully 💜")
