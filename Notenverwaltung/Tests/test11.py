from tkinter import *

root = Tk()

photo = PhotoImage(file="myface.png")  # oder path angeben
label = Label(root, image=photo)
label.pack

root.mainloop()