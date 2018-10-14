from tkinter import *
import sqlite3
from student import Student
import tkinter.messagebox
from tkinter import ttk


conn = sqlite3.connect('notenliste.db')

c = conn.cursor()

# c.execute("""CREATE TABLE notenliste (
#             Vorname text,
#             Nachname text,
#             Matrnr text
#             )""")


def insert_stud():
    with conn:
        # stud = Student('Benni', 'Eli', '396904')
        vorname = vorname_entry.get()
        nachname = nachname_entry.get()
        matrnr = matrnr_entry.get()

        # stud = Student(vorname, nachname, matrnr)
        c.execute("INSERT INTO notenliste VALUES (:vorname,:nachname,:matrnr)",
                  {'vorname': vorname, 'nachname': nachname, 'matrnr': matrnr})
        print('done')

def get_studs_by_name(name):
    c.execute("SELECT * FROM notenliste WHERE nachname=:nachname", {'nachname': name})
    return c.fetchall()

def remove_stud():
    with conn:
        vorname = vorname_entry.get()
        nachname = nachname_entry.get()
        # matrnr = matrnr_entry.get()
        c.execute("DELETE from notenliste WHERE vorname = :vorname AND nachname = :nachname",
                  {'vorname': vorname, 'nachname': nachname})

def search():
    studs = get_studs_by_name('Simon')
    print(studs)

def doNothing():
    print("ok ok I won't...")

def close():
    answer = tkinter.messagebox.askquestion('U serious?', 'You really wanna quit?')
    if answer == 'yes':
        root.quit()

root = Tk()
root.title('Notenverwaltung')
root.geometry("1000x500")
root.minsize(width=500, height=200)

# **** Main Menu ****

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=doNothing)
subMenu.add_command(label="New...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=close)
subMenu.add_checkbutton(label='check')

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=doNothing)

# **** Main ****


main = LabelFrame(root, text='hi')
main.pack(side=TOP, fill=X)

vorname_label = Label(main, text="Vorname:")
vorname_label.grid(row=0, column=0, sticky=W)
vorname_entry = Entry(main)
vorname_entry.grid(row=0, column=1)

nachname_label = Label(main, text="Nachname:")
nachname_label.grid(row=1, column=0, sticky=W)
nachname_entry = Entry(main)
nachname_entry.grid(row=1, column=1)

matrnr_label = Label(main, text="Matrikelnummer:")
matrnr_label.grid(row=2, column=0, sticky=W)
matrnr_entry = Entry(main)
matrnr_entry.grid(row=2, column=1)

button_save = Button(main, text="Save", command=insert_stud)
button_save.grid()
button_search = Button(main, text="Search", command=search)
button_search.grid()
button_delete = Button(main, text="Delete", command=remove_stud)
button_delete.grid()

# studs = get_studs_by_name('Simon')
# print(studs)

def printName():
    print("Chello my name is Bucky!")
button1 = Button(main, text="Print my name", command=printName)
button1.grid()

# **** Status Bar ****

status = Label(root, text="Ausgewählte Tabelle:" + vorname_entry.get(), bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)



root.mainloop()