
from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

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

    conn.close()

    return render_template("index.html", tasks=tasks, mood=mood)

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

    # Remove previous mood for today
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

if __name__ == "__main__":
    app.run(debug=True)
