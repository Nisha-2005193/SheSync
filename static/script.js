let time = 25 * 60;  // 25 minutes in seconds
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
