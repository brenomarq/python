import tkinter as tk
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
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer() -> None:
    global timer
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer() -> None:
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    elif reps == 8:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
        reps = 0
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
        marks = reps // 2
        check_mark.config(text="✔" * marks)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count: int) -> None:
    global timer
    count_min = count // 60 if count // 60 >= 10 else f"0{count // 60}"
    count_sec = count % 60 if count % 60 >= 10 else f"0{count % 60}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tk.Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_btn = tk.Button(text="Start", command=start_timer,width=10, height=2, highlightthickness=0)
start_btn.grid(column=0, row=3)

reset_btn = tk.Button(text="Reset", command=reset_timer,width=10, height=2, highlightthickness=0)
reset_btn.grid(column=2, row=3)

check_mark = tk.Label(text="", font=(FONT_NAME, 15, "bold"),bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=4)

window.mainloop()
