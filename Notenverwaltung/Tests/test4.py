from tkinter import *

root = Tk()


# def hi():
#     var = entry_1.get()
#     print(var)


label_1 = Label(root, text="name")
label_2 = Label(root, text="password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)

# btn = Button(root, text="Print var", command=hi)
# btn.grid()

root.mainloop()
