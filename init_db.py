import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_text TEXT NOT NULL,
    is_completed INTEGER,
    date TEXT
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS moods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mood TEXT,
    date TEXT
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS wellness (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    workout_done INTEGER,
    sleep_done INTEGER,
    water_count INTEGER,
    date TEXT
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS period (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    last_period_date TEXT
)
''')

conn.commit()
conn.close()

print("Database and tables created successfully 👑")
