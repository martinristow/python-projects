from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps
    global check
    window.after_cancel(timer)
    reps = 0
    check = ""
    timer_textt.config(text="Timer")
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    # Re-enable the start button
    start_button.config(state=NORMAL)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global check
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    # Disable the start button once the timer starts
    start_button.config(state=DISABLED)

    if reps % 2 == 0:
        check += "✔"
        check_marks.config(text=check)

    if reps % 8 == 0:
        timer_textt.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_textt.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_textt.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Image Name
image = "tomato.png"
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=image)
canvas.create_image(100, 112, image=tomato_img)

# Timer Number
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer Text Label
timer_textt = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_textt.grid(column=1, row=0)

# Start Button
start_button = Button(text="Start", bg="white", width=6, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", bg="white", width=6, highlightthickness=0, command=timer_reset)
reset_button.grid(column=2, row=2)

# Check Marks Label
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()
