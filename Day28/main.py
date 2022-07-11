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
SECONDS_IN_MINUTE = 60
MILISEC_IN_SECONDS = 1000
reps = 0
timer = None

# ---------------------------- SETTINGS MANAGER ------------------------------- #





# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer, reps

    # Stop and reset timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="25:00")

    # Set initial text to title
    title_text.config(text="Timer")

    # Reset reps
    reps = 0

    # Reset check marks
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    # Get times in seconds
    work_time = WORK_MIN * SECONDS_IN_MINUTE
    short_break_time = SHORT_BREAK_MIN * SECONDS_IN_MINUTE
    long_break_time = LONG_BREAK_MIN * SECONDS_IN_MINUTE

    if reps % 8 == 0:
        # Start new countdown
        count_down(long_break_time)
        # Configure title text
        title_text.config(foreground=RED, text="Long break!")
    elif reps % 2 == 0:
        # Start new countdown
        count_down(short_break_time)
        # Configure title text
        title_text.config(foreground=PINK, text="Short break!")
    else:
        # Start new countdown
        count_down(work_time)
        # Configure title text
        title_text.config(foreground=GREEN, text="Work time!")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # Get times in minutes and seconds
    count_minute = math.floor(count / SECONDS_IN_MINUTE)
    count_seconds = count % SECONDS_IN_MINUTE

    # Format seconds as "00"
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")

    # Recursively call this function to continue count down
    if count > 0:
        global timer
        timer = window.after(MILISEC_IN_SECONDS, count_down, count - 1)
    else:
        start_timer()

        # Logic behind checkmarks
        marks = "✔"
        work_sessions = math.floor(reps / 2)  # Total work sessions
        for _ in range(work_sessions):  # For each work session done, add a mark
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Create canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)


# Display tomato image
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
# Display timer text
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))

# Pack canvas
canvas.grid(column=1, row=1)


# Title text
title_text = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_text.grid(column=1, row=0)


# Start button
start_button = Button(text="Start", font=(FONT_NAME, 15, "bold"), highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

# Reset button
reset_button = Button(text="Reset", font=(FONT_NAME, 15, "bold"), highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

# Checkmarks
check_marks = Label(background=YELLOW, foreground=GREEN)
check_marks.grid(column=1, row=3)

# Work time setter
work_time_setter = Entry(width=10, background=GREEN, highlightbackground=YELLOW, foreground="black")
work_time_setter.insert(index=END, string="Work time")
work_time_setter.grid(column=2, row=4)

# Short break setter
short_break_setter = Entry(width=10, background=GREEN, highlightbackground=YELLOW, foreground="black")
short_break_setter.insert(index=END, string="Short break time")
short_break_setter.grid(column=2, row=5)

# Long break setter
short_break_setter = Entry(width=10, background=GREEN, highlightbackground=YELLOW, foreground="black")
short_break_setter.insert(index=END, string="Long break time")
short_break_setter.grid(column=2, row=6)


window.mainloop()
