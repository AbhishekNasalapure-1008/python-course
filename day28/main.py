from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None

def reset_timer()
    pass

def start_timer()
    pass


windows=Tk()
windows.title("Pomodoro")
windows.config(padx=100, pady=50, bg=YELLOW)

def count_down(count):
    global reps
    count_min=math.floor(count/60)
    count_sec=int(count%60)

    if count_sec==0:
    count_sec="00"

    if int(count_sec)<10:
        count_sec=int(count_sec)
        count_sec=f"0{count_sec}"

    if count_min==0 and int(count_sec)==0:
        reps+=1

    canvas.itemconfig
    
