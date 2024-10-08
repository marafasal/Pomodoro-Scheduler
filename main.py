import math
from tkinter import *
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
show=None
window=Tk()
window.title("My_scheduler")
window.config(padx=100,pady=50,bg=YELLOW)

def restart_count():
    global reps
    window.after_cancel(show)
    canvass.itemconfig(timer_text,text="00:00")
    reps=0

def clickme():

    work_sec=WORK_MIN*60
    long_break=work_sec*LONG_BREAK_MIN
    short_break=work_sec*SHORT_BREAK_MIN
    global reps
    reps+=1
    if reps%8==0:
        counter(long_break)
        timerLabel.config(text="long break", fg=GREEN,bg=YELLOW,font=("courier",18,"normal"))
    elif reps%2==0:
        counter(short_break)
        timerLabel.config(text="short break",fg=PINK,bg=YELLOW,font=("courier",18,"normal"))
    else:
        counter(work_sec)





def counter(count):
    global show
    mins=math.floor(count/60)
    secs=count%60
    if secs<10:
        secs=f'0{secs}'
    canvass.itemconfig(timer_text,text=f'{mins}:{secs}')
    if count>0:
        show=window.after(1000,counter,count-1)
    else:
        clickme()
        for _ in range (math.floor(reps/2)):
            checklabel.config(text="✅")





canvass=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
photo=PhotoImage(file="tomato.png")
canvass.create_image(100,112,image=photo)
timer_text=canvass.create_text(105,124,text="00:00",font=(FONT_NAME,35,"bold"),fill="white")
canvass.grid(column=1,row=1)


timerLabel=Label(text="Timer",font=(FONT_NAME,35,"bold"),fg="red",bg=YELLOW)
timerLabel.grid(column=1,row=0)
startlabel=Button(text="Start",fg='green',bg=YELLOW,highlightthickness=0,command=clickme)
startlabel.grid(column=0,row=4)
restartlabel=Button(text="Restart",fg='green',bg=YELLOW,highlightthickness=0,command=restart_count)
restartlabel.grid(column=4,row=4)
checklabel=Label(fg='green',bg=YELLOW,highlightthickness=0)
checklabel.grid(column=1,row=5)

window.mainloop()
