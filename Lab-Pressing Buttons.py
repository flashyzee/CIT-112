"""
Date : April 2024
Author : Zion Adedipe
Purpose : Show how to display text based information in
windows on the screen

Name : time.py
"""

from tkinter import *
from datetime import datetime

timestr = 0

def onClick():
    global timestr
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    timestr.set("It's" + current_time)

def main():
    global timestr
    window = Tk()
    window.geometry("300x100")
    window.title("Time Messages")
    timeStr = StringVar()
    timeStr.set("What Time is it Anyway?")
    
    label = Label(window, textvariable = timeStr, font=("Helvetica", 13))
    label.pack(side=TOP)

    button = Button(window, text="Time", command=onClick)
    button.pack(side=BOTTOM)

    mainloop()

main()