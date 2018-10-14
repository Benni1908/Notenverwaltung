from tkinter import *
import tkinter.messagebox


root = Tk()

tkinter.messagebox.showinfo('Window Title', 'Monkeys bla bla.')

answer = tkinter.messagebox.askquestion('Question 1', 'Do you like silly faces?')

if answer == 'yes':
    print('8==D~ ')

root.mainloop()