import tkinter
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    my_label["text"] = "Timer"
    canvas.itemconfig(timer_text, text="00:00")
    my_label_1.config(text="")




# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        my_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        my_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        my_label.config(text="Work", fg=GREEN)

    return reps
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        if reps == 2:
            my_label_1.config(text="✓")
        elif reps == 4:
            my_label_1.config(text="✓✓")
        elif reps == 8:
            my_label_1.config(text="✓✓✓")

    # ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Project")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

my_label = tkinter.Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
my_label.grid(column=1, row=0)

my_label_1 = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14))
my_label_1.grid(column=1, row=3)


button_1 = tkinter.Button(text="Start", command=start_timer)
button_1.grid(column=0, row=2)

button_1 = tkinter.Button(text="Restart", command=reset_timer)
button_1.grid(column=2, row=2)

window.mainloop()