from tkinter import *
import sqlite3 as sq
import datetime

def leftClick(event):
    day = dayT.get
    print(day)

window = Tk()
window.title("Compound Tracker")

window.geometry('800x600+0+0')

header = Label(window, text="Compound Tracker for Weightlifting", font=("arial", 30, "bold"), fg="black").pack()

L1 = Label(window, text="Compound Lift", font=("arial", 18)).place(x=10, y=100)

L2 = Label(window, text="Day (dd)", font=("arial", 18)).place(x=10, y=150)

L3 = Label(window, text="Month (mm)", font=("arial", 18)).place(x=10, y=200)

L4 = Label(window, text="Year (yyyy)", font=("arial", 18)).place(x=10, y=250)

L5 = Label(window, text="Max Weight (KG)", font=("arial", 18)).place(x=10, y=300)

L6 = Label(window, text="Reps", font=("arial", 18)).place(x=10, y=350)

compound = {'Bench', 'Squat', 'Deadlift', 'OVH'}

compd = OptionMenu(window, *compound)
compd.place(x=220, y=105)

dayT = Entry(window)
frame = Button(window, width=10, height=10)
frame.pack()
frame.bind("<Button-1>", leftClick)

dayT.place(x=220, y=155)
monthT = Entry(window, textvariable='month')
monthT.place(x=220, y=205)
yearT = Entry(window, textvariable='year')
yearT.place(x=220, y=255)
weightT = Entry(window, textvariable='weight')
weightT.place(x=220, y=305)
repT = Entry(window, textvariable='reps')
repT.place(x=220, y=355)

window.mainloop()
