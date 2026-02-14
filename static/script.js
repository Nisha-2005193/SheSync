let time = 10;  // 10 seconds for testing

let timerInterval = null;

// Update timer display
function updateDisplay() {
    let minutes = Math.floor(time / 60);
    let seconds = time % 60;

    document.getElementById("timer").innerText =
        minutes + ":" + (seconds < 10 ? "0" : "") + seconds;
}

// Start timer
function startTimer() {
    if (!timerInterval) {
        timerInterval = setInterval(() => {
            if (time > 0) {
                time--;
                updateDisplay();
            } else {
                clearInterval(timerInterval);
                timerInterval = null;

                document.getElementById("timerMessage").innerText =
                    "Time’s up! Take a short break 💜";
            }
        }, 1000);
    }
}

// Pause timer
function pauseTimer() {
    clearInterval(timerInterval);
    timerInterval = null;
}

// Reset timer
function resetTimer() {
    pauseTimer();
    time = 25 * 60;
    updateDisplay();
    document.getElementById("timerMessage").innerText = "";
}

// Water counter
function addWater() {
    let count = document.getElementById("waterCount");
    let current = parseInt(count.innerText);

    if (current < 8) {
        count.innerText = current + 1;
    }
}

// Initialize timer display when page loads
updateDisplay();

// Show water reminder
// Show water reminder
function showHourlyReminder() {
    const reminder = document.getElementById("water-reminder");
    if (!reminder) return;

    reminder.style.display = "block";  // show alert
    setTimeout(() => {
        reminder.style.display = "none";  // hide after 10 seconds
    }, 10000); // visible for 10 seconds
}

// First reminder on page load
window.addEventListener("load", showHourlyReminder);

// Repeat every hour (for testing: every 10 seconds)
setInterval(showHourlyReminder, 10 * 1000);  // change 10*1000 → 3600*1000 for 1 hour


// Optional: show once on page load
window.addEventListener("load", showHourlyReminder);


// Trigger first reminder immediately, then every hour
showHourlyReminder();  // optional: first reminder on page load
// Test version: reminder every 10 seconds
setInterval(showHourlyReminder, 10 * 1000);
 // every 60 minutes
