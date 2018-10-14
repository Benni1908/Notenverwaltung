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




class main:

    def insert_stud(self):
        with conn:
            # stud = Student('Benni', 'Eli', '396904')
            self.vorname = self.vorname_entry.get()
            self.nachname = self.nachname_entry.get()
            self.matrnr = self.matrnr_entry.get()

            # stud = Student(vorname, nachname, matrnr)
            c.execute("INSERT INTO notenliste VALUES (:vorname,:nachname,:matrnr)",
                      {'vorname': self.vorname, 'nachname': self.nachname, 'matrnr': self.matrnr})
            print('done')

    def get_studs_by_name(self, name):
        c.execute("SELECT * FROM notenliste WHERE nachname=:nachname", {'nachname': name})
        return c.fetchall()

    def remove_stud(self):
        with conn:
            self.vorname = self.vorname_entry.get()
            self.nachname = self.nachname_entry.get()
            answer = tkinter.messagebox.askquestion('U serious?', 'You really wanna delete this motherfucker?')
            if answer == 'yes':
                c.execute("DELETE from notenliste WHERE vorname = :vorname AND nachname = :nachname",
                          {'vorname': self.vorname, 'nachname': self.nachname})
                print('gelöscht')

    def search(self):
        studs = self.get_studs_by_name('Simon')
        print(studs)

    def printName(self):
        print("Chello my name is Bucky!")

    def __init__(self, frame):
        self.frame = frame
        main = LabelFrame(root, text='hi')
        main.grid()

        self.vorname_label = Label(self.frame, text="Vorname:")
        self.vorname_label.grid(row=0, column=0, sticky=W)
        self.vorname_entry = Entry(self.frame)
        self.vorname_entry.grid(row=0, column=1)

        self.nachname_label = Label(self.frame, text="Nachname:")
        self.nachname_label.grid(row=1, column=0, sticky=W)
        self.nachname_entry = Entry(self.frame)
        self.nachname_entry.grid(row=1, column=1)

        self.matrnr_label = Label(self.frame, text="Matrikelnummer:")
        self.matrnr_label.grid(row=2, column=0, sticky=W)
        self.matrnr_entry = Entry(self.frame)
        self.matrnr_entry.grid(row=2, column=1)

        self.button_save = Button(self.frame, text="Save", command=self.insert_stud)
        self.button_save.grid()
        self.button_search = Button(self.frame, text="Search", command=self.search)
        self.button_search.grid()
        self.button_delete = Button(self.frame, text="Delete", command=self.remove_stud)
        self.button_delete.grid()
        self.button1 = Button(self.frame, text="Print my name", command=self.printName)
        self.button1.grid()


# studs = get_studs_by_name('Simon')
# print(studs)

main1 = main(root)




# **** Status Bar ****

# status = Label(root, text="Ausgewählte Tabelle:" + vorname_entry.get(), bd=1, relief=SUNKEN, anchor=W)
# status.pack(side=BOTTOM, fill=X)



root.mainloop()