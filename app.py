from datetime import datetime
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# -------- DATABASE CONNECTION --------
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# -------- HOME --------
@app.route("/")
def index():
    conn = get_db_connection()
    today = str(datetime.today().date())

    tasks = conn.execute(
        "SELECT * FROM tasks WHERE date = ?",
        (today,)
    ).fetchall()

    mood = conn.execute(
        "SELECT * FROM moods WHERE date = ?",
        (today,)
    ).fetchone()

    cycle_info = conn.execute(
        "SELECT * FROM cycle ORDER BY id DESC LIMIT 1"
    ).fetchone()

    cycle_phase = None

    if cycle_info:
        last_period = datetime.strptime(
            cycle_info["last_period_date"], "%Y-%m-%d"
        )
        cycle_length = cycle_info["cycle_length"]

        days_since = (datetime.today() - last_period).days
        day_in_cycle = days_since % cycle_length

        if day_in_cycle <= 5:
            cycle_phase = "Menstrual Phase 🌸 – Focus on rest and light tasks."
        elif day_in_cycle <= 13:
            cycle_phase = "Follicular Phase 🌿 – Great time to start new projects!"
        elif day_in_cycle <= 16:
            cycle_phase = "Ovulation Phase ✨ – Best for communication & collaboration."
        else:
            cycle_phase = "Luteal Phase 🌙 – Good time for planning and organizing."

    conn.close()

    return render_template(
        "index.html",
        tasks=tasks,
        mood=mood,
        cycle_phase=cycle_phase
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

    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
