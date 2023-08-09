from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PURPLE = "#8C3333"
RED = "#F26849"
DARK_GREEN = "#557A46"
GREEN = "#379B46"
YELLOW = "#F2EE9D"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    window.after_cancel(timer)
    title.config(text="Pomodoro", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    global marks
    check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global reps
    reps += 1
    print(reps)
    if reps == 8:
        count_dow(LONG_BREAK_MIN * 60)
        title.config(text="Descanso", fg=PURPLE)
    elif reps % 2 != 0:
        count_dow(WORK_MIN * 60)
        title.config(text="Trabalho", fg=GREEN)
    elif reps % 2 == 0:
        count_dow(SHORT_BREAK_MIN * 60)
        title.config(text="Pip Stop", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_dow(count):
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_seg = count % 60
    if count_seg < 10:
        count_seg = f"0{count_seg}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seg}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_dow, count - 1)
    else:
        start_time()
        marks = ""
        for _ in range(0, math.floor(reps / 2)):
            marks += "✔"
        check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg=YELLOW)

title = Label(text="Pomodoro", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

button_start = Button(text="Start", font=("arial", 10, "bold"), fg=DARK_GREEN, bg="white", padx=5, borderwidth=0,
                      command=start_time)  # Start the countdown
button_start.grid(column=0, row=2, pady=5)

button_Reset = Button(text="Reset", font=("arial", 10, "bold"), fg=DARK_GREEN, bg="white", padx=5, borderwidth=0,
                      command=reset_time)
button_Reset.grid(column=2, row=2, pady=5)

check = Label(font=("arial", 10, "normal"), bg=YELLOW, fg=GREEN)
check.grid(column=1, row=3)

window.mainloop()
