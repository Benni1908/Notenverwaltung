from tkinter import *

root = Tk()

# def printName():
#     print("Chello my name is Bucky!")
# button1 = Button(root, text="Print my name", command=printName)

def printName(event):
    print("Chello my name is Bucky!")

button1 = Button(root, text="Print my name")
button1.bind("<Button-1>", printName)




button1.pack()

root.mainloop()