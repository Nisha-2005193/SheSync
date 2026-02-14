from datetime import datetime,timedelta
from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# -------- DATABASE SETUP FOR VERCEL --------
DATABASE = os.getenv("DATABASE_PATH", "/tmp/database.db")

# -------- DATABASE CONNECTION --------
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Initialize database on startup
def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        
        c.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_text TEXT NOT NULL,
            is_completed INTEGER DEFAULT 0,
            date TEXT
        )
        """)
        
        c.execute("""
        CREATE TABLE IF NOT EXISTS moods (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mood TEXT,
            date TEXT
        )
        """)
        
        c.execute("""
        CREATE TABLE IF NOT EXISTS cycle (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            last_period_date TEXT,
            cycle_length INTEGER
        )
        """)
        
        conn.commit()
        conn.close()

init_db()

# -------- HOME --------
@app.route("/")
def index():
    conn = get_db_connection()
    today = str(datetime.today().date())

    # Fetch tasks & mood
    tasks = conn.execute(
        "SELECT * FROM tasks WHERE date = ?",
        (today,)
    ).fetchall()

    mood = conn.execute(
        "SELECT * FROM moods WHERE date = ?",
        (today,)
    ).fetchone()

    # Mood suggestion
    suggestion = None
    if mood:
        mood_value = mood["mood"].strip().lower()
        if "stressed" in mood_value:
            suggestion = "Take a 5-minute breathing break 🌿"
        elif "happy" in mood_value:
            suggestion = "You’re glowing today ✨ Try completing your toughest task!"
        elif "sad" in mood_value:
            suggestion = "Be gentle with yourself 💜 Do one small easy task."
        elif "calm" in mood_value:
            suggestion = "Perfect energy for planning ahead 📒"

    # Cycle logic
    cycle_info = conn.execute(
        "SELECT * FROM cycle ORDER BY id DESC LIMIT 1"
    ).fetchone()

    cycle_phase = None
    recommended_hours = None
    hydration_alert = False

    if cycle_info:
        last_period = datetime.strptime(cycle_info["last_period_date"], "%Y-%m-%d")
        cycle_length = int(cycle_info["cycle_length"])
        days_since = (datetime.today() - last_period).days
        day_in_cycle = days_since % cycle_length

        if day_in_cycle <= 5:
            cycle_phase = "Menstrual Phase 🌸 – Focus on rest and light tasks."
            recommended_hours = "1–2 hours"
            hydration_alert = True
        elif day_in_cycle <= 13:
            cycle_phase = "Follicular Phase 🌿 – Great time to start new projects!"
            recommended_hours = "3–4 hours"
        elif day_in_cycle <= 16:
            cycle_phase = "Ovulation Phase ✨ – Best for communication & collaboration."
            recommended_hours = "3–5 hours"
        else:
            cycle_phase = "Luteal Phase 🌙 – Good time for planning and organizing."
            recommended_hours = "2–3 hours"

    conn.close()

    # ✅ Define daily_hydration_alert here
    daily_hydration_alert = True  # always show the daily reminder

    return render_template(
        "index.html",
        tasks=tasks,
        mood=mood,
        cycle_phase=cycle_phase,
        suggestion=suggestion,
        recommended_hours=recommended_hours,
        hydration_alert=hydration_alert,
        daily_hydration_alert=daily_hydration_alert
    )


# -------- ADD TASK --------
@app.route("/add_task", methods=["POST"])
def add_task():
    task_text = request.form["task"]
    today = str(datetime.today().date())

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO tasks (task_text, date) VALUES (?, ?)",
        (task_text, today)
    )
    conn.commit()
    conn.close()

    return redirect("/")

# -------- DELETE TASK --------
@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )
    conn.commit()
    conn.close()

    return redirect("/")

# -------- SAVE MOOD --------
@app.route("/save_mood", methods=["POST"])
def save_mood():
    selected_mood = request.form["mood"]
    today = str(datetime.today().date())

    conn = get_db_connection()

    conn.execute(
        "DELETE FROM moods WHERE date = ?",
        (today,)
    )

    conn.execute(
        "INSERT INTO moods (mood, date) VALUES (?, ?)",
        (selected_mood, today)
    )

    conn.commit()
    conn.close()

    return redirect("/")

# -------- SAVE CYCLE --------
@app.route("/save_cycle", methods=["POST"])
def save_cycle():
    last_period = request.form["last_period"]
    cycle_length = request.form["cycle_length"]

    conn = get_db_connection()

    conn.execute("DELETE FROM cycle")

    conn.execute(
        "INSERT INTO cycle (last_period_date, cycle_length) VALUES (?, ?)",
        (last_period, cycle_length)
    )
# inside index() before conn.close()
    daily_hydration_alert = True  # always show daily water reminder

    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
