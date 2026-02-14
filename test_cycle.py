import sqlite3
from datetime import datetime

# --- Connect to database in the same folder ---
conn = sqlite3.connect("database.db")  # database.db is in the same folder
conn.row_factory = sqlite3.Row

# --- Get latest cycle info ---
cycle_info = conn.execute("SELECT * FROM cycle ORDER BY id DESC LIMIT 1").fetchone()

cycle_phase = None
recommended_hours = None
hydration_alert = False

if cycle_info:
    last_period = datetime.strptime(cycle_info["last_period_date"], "%Y-%m-%d")
    cycle_length = cycle_info["cycle_length"]
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

# --- Print cycle info ---
print("🌸 Current Cycle Phase:", cycle_phase)
print("📚 Recommended Study Hours:", recommended_hours)
print("💧 Hydration Alert:", hydration_alert)

# --- Get tasks for today ---
today = str(datetime.today().date())
tasks = conn.execute("SELECT * FROM tasks WHERE date = ?", (today,)).fetchall()
print("\n📝 Tasks for today:")
if tasks:
    for t in tasks:
        status = "✔" if t["is_completed"] else "❌"
        print(f"{status} {t['task_text']}")
else:
    print("No tasks yet.")

# --- Get mood for today ---
mood = conn.execute("SELECT * FROM moods WHERE date = ?", (today,)).fetchone()
print("\n😊 Mood for today:")
if mood:
    print(mood["mood"])
else:
    print("No mood recorded today.")

conn.close()
