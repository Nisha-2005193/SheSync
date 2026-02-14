<img width="1280" height="640" alt="img" src="https://github.com/user-attachments/assets/37aee461-9934-4e37-965b-e1a89bbb4bc7" />


SheSync 🎯

Built with the goal of redefining student productivity through balance, mindfulness, and structured focus.

Team Name: HackHer Hive

Team Members
- Member 1: Shreemayee-LBS college of engineering
- Member 2: Nisha-LBS college of engineering

### Hosted Project Link
https://she-sync-lhya.vercel.app/

### Project Description
SheSync is a smart productivity and wellness app designed to help female students balance academics and self-care in one place. It combines task management, mood tracking, study timers, daily wellness checks, and period awareness to support both productivity and wellbeing. SheSync encourages mindful habits while keeping daily goals organized and manageable. 💜

### The Problem statement
Students often focus heavily on academics while neglecting:
### The Solution
[How are you solving it?]

---

## Technical Details
SheSync merges task management with wellness tracking in a minimal, student-friendly platform.

It allows users to:

Organize daily tasks

Track mood patterns

Maintain hydration goals

Monitor sleep & workout habits

Use a 25-minute focus timer

Receive period-aware wellness reminders

This creates a balanced productivity ecosystem, not just a to-do list.

### Technologies/Components Used

**For Software:**
- Languages used: Python

HTML
CSS
JavaScript
SQL (SQLite)
- Frameworks used: (Python Web Framework)
- Libraries used:sqlite3
                 datetime 
- Tools used: VS Code
              Git & GitHub
              DB Browser for SQLite
              Chrome Browser


## Features

List the key features of your project:
- Feature 1: : Smart Task Manager
Users can:
Add tasks
Delete tasks
Store tasks in database
- Feature 2: Mood Tracker
Select daily mood
Stores mood in database
Displays personalized wellness suggestion
- Feature 3: Menstrual Cycle Tracker
User enters last period date
User enters cycle length
App calculates current phase
Displays phase-based insight
- Feature 4:Cycle-Based Study Recommendation
Automatically suggests recommended study hours
Adjusts productivity guidance based on menstrual phase

- Feature 4:Hydration Alert
During menstrual phase, shows hydration reminder
Encourages rest & balanced workload
---

## Implementation

### For Software:

#### Installation
```bash
git clone <your-repo-link>
cd SheSync
```bash
pip install flask
```bash
python init_db.py
```

#### Run
```bash
python app.py
```


---

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)

<img width="1920" height="1080" alt="Screenshot 2026-02-14 071949" src="https://github.com/user-attachments/assets/57da31fd-a069-404f-ba6c-f73bdaf688c2" />

<img width="1920" height="1080" alt="Screenshot 2026-02-14 071933" src="https://github.com/user-attachments/assets/dbd99613-e601-41db-ac2d-bbee6dad022f" />


<img width="1920" height="1080" alt="Screenshot 2026-02-14 071816" src="https://github.com/user-attachments/assets/823e39df-770b-48e0-8f1f-c4154f09586c" />

<img width="1920" height="1080" alt="Screenshot 2026-02-14 071446" src="https://github.com/user-attachments/assets/782a5f51-af5b-4ed2-90bc-eab7726b7ff2" />

<img width="1920" height="1080" alt="Screenshot 2026-02-14 071433" src="https://github.com/user-attachments/assets/cf462950-e2bf-4eb1-8615-2f3acd26e1d5" />

<img width="1920" height="1080" alt="Screenshot 2026-02-14 071410" src="https://github.com/user-attachments/assets/ddf83220-db87-4a1b-afc7-4f97936679f0" />

<img width="1920" height="1020" alt="Screenshot 2026-02-14 071348" src="https://github.com/user-attachments/assets/de861f7d-37d6-4888-b730-a59612e2f918" />


#### Diagrams

**Application Workflow:**

![flwss](https://github.com/user-attachments/assets/001fa9ed-cc5a-4c69-a3b9-a13f769f0188)

---


---


##### Endpoints


#### App Flow Diagram

![flwss](https://github.com/user-attachments/assets/c8ecf14d-e464-4424-8600-df4837a3f9fb)


#### Installation Guide
Perfect! Here’s a **concise installation guide** for **SheSync (Flask Web App)** that you can use in your README or project documentation.

---

## **SheSync Installation Guide**

### **1️⃣ Prerequisites**

* Python 3.8+ installed on your system
* Git (optional, if cloning from GitHub)
* SQLite (comes bundled with Python)

---

### **2️⃣ Clone the Repository**

```bash
git clone https://github.com/Nisha-2005193/SheSync.git
cd SheSync
```

---

### **3️⃣ Set Up Virtual Environment (Recommended)**

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

---

### **4️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

---

### **5️⃣ Initialize Database**

```bash
python
>>> from app import create_db  # if using a create_db function
>>> create_db()
>>> exit()
```

> Or if you have `database_setup.py`:

```bash
python database_setup.py
```

---

### **6️⃣ Run the App**

```bash
python app.py
```

* Open your browser and go to: `http://127.0.0.1:5000`

---

```bash
python app.py --debug
```

---

## Project Demo

### Video
https://drive.google.com/drive/folders/1yhV6ah88Uynxz8u5JFUwAltKffAZX8_G?usp=sharing

## AI Tools Used (Optional - For Transparency Bonus)

  GitHub Copilot ,ChatGPT

**Purpose:**
Debugging assistance for async functions
Code review and optimization suggestions

**Key Prompts Used:**
Frontend & UI: Designed Pomodoro timer, water tracker, cycle insights, and wellness tips with interactive alerts.

Backend & DB: Built Flask routes for tasks, mood, and cycle tracking; used SQLite to store and fetch daily data.

Alerts & JS: Implemented hourly water reminders, Pomodoro countdown, and dynamic message displays with JavaScript

**Human Contributions:**
- Architecture design and planning
- Custom business logic implementation
- Integration and testing
- UI/UX design decisions
---

## Team Contributions

- Shreemayee: Frontend development
- Nisha: Backend development, Database design

---

## License

MIT License
---


