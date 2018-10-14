from tkinter import *
import sqlite3
import tkinter.messagebox
from tkinter import ttk, VERTICAL, HORIZONTAL, N, S, E, W
from tkinter.scrolledtext import ScrolledText
import queue
import logging
import signal

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

conn = sqlite3.connect('notenliste.db')

c = conn.cursor()


# c.execute("""CREATE TABLE notenliste (
#             Vorname text,
#             Nachname text,
#             Matrnr text
#             )""")


class QueueHandler(logging.Handler):
    """Class to send logging records to a queue
    It can be used from different threads
    The ConsoleUi class polls this queue to display records in a ScrolledText widget
    """

    # Example from Moshe Kaplan: https://gist.github.com/moshekaplan/c425f861de7bbf28ef06
    # (https://stackoverflow.com/questions/13318742/python-logging-to-tkinter-text-widget) is not thread safe!
    # See https://stackoverflow.com/questions/43909849/tkinter-python-crashes-on-new-thread-trying-to-log-on-main-thread

    def __init__(self, log_queue):
        super().__init__()
        self.log_queue = log_queue

    def emit(self, record):
        self.log_queue.put(record)


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
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

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


class ConsoleUi:
    """Poll messages from a logging queue and display them in a scrolled text widget"""

    def __init__(self, frame):
        self.frame = frame
        # Create a ScrolledText wdiget
        self.scrolled_text = ScrolledText(frame, state='disabled', height=12)
        self.scrolled_text.grid(row=0, column=0, sticky="nsew")
        self.scrolled_text.configure(font='TkFixedFont')
        self.scrolled_text.tag_config('INFO', foreground='black')
        self.scrolled_text.tag_config('DEBUG', foreground='gray')
        self.scrolled_text.tag_config('WARNING', foreground='orange')
        self.scrolled_text.tag_config('ERROR', foreground='red')
        self.scrolled_text.tag_config('CRITICAL', foreground='red', underline=1)
        # Create a logging handler using a queue
        # self.log_queue = queue.Queue()
        # self.queue_handler = QueueHandler(self.log_queue)
        formatter = logging.Formatter('%(asctime)s:\n  %(message)s')
        self.file_handler = logging.FileHandler('test.log')
        self.file_handler.setFormatter(formatter)
        logger.addHandler(self.file_handler)
        # logging.basicConfig(datefmt='%m-%d %H:%M')
        # self.queue_handler.setFormatter(formatter)
        # logger.addHandler(self.queue_handler)
        # Start polling messages from the queue
        # self.frame.after(100, self.poll_log_queue)

    def display(self, record):
        msg = self.queue_handler.format(record)
        self.scrolled_text.configure(state='normal')
        self.scrolled_text.insert(END, msg + '\n', record.levelname)
        self.scrolled_text.configure(state='disabled')
        # Autoscroll to the bottom
        self.scrolled_text.yview(END)

    def poll_log_queue(self):
        # Check every 100ms if there is a new message in the queue to display
        while True:
            try:
                record = self.log_queue.get(block=False)
            except queue.Empty:
                break
            else:
                self.display(record)
        self.frame.after(100, self.poll_log_queue)


# **** Main ****

class Main:

    def insert_stud(self):
        with conn:
            # stud = Student('Benni', 'Eli', '396904')
            self.vorname = self.vorname_entry.get()
            self.nachname = self.nachname_entry.get()
            self.matrnr = self.matrnr_entry.get()

            # stud = Student(vorname, nachname, matrnr)
            c.execute("INSERT INTO notenliste VALUES (:vorname,:nachname,:matrnr)",
                      {'vorname': self.vorname, 'nachname': self.nachname, 'matrnr': self.matrnr})
            logger.log(logging.DEBUG, 'saved')
            logger.log(logging.ERROR, 'saved')
            logger.log(logging.INFO, 'saved')
            logger.log(logging.CRITICAL, 'saved')
            logger.log(logging.WARNING, 'saved')

    def get_studs_by_name(self, name):
        c.execute("SELECT * FROM notenliste WHERE nachname=:nachname", {'nachname': name})
        return c.fetchall()

    def remove_stud(self):
        with conn:
            self.vorname = self.vorname_entry.get()
            self.nachname = self.nachname_entry.get()
            self.matrnr = self.matrnr_entry.get()
            answer = tkinter.messagebox.askquestion('U serious?', 'You really wanna delete ' + self.matrnr + '?')
            if answer == 'yes':
                c.execute("DELETE from notenliste WHERE vorname = :vorname AND nachname = :nachname AND matrnr = :matrnr",
                          {'vorname': self.vorname, 'nachname': self.nachname, 'matrnr': self.matrnr})
                logger.error(self.nachname + ', ' + self.vorname + ' (' + self.matrnr + ') wurde gelöscht')

    def search(self):
        studs = self.get_studs_by_name('Eli')
        print(studs)

    def printName(self):
        print("Chello my name is Bucky!")
        logger.log(logging.ERROR, 'test: ' + main1.getName())
        logging.basicConfig(level=logging.ERROR)
        logger.warning('hallo')
        qwert = ConsoleUi(self.console)
        qwerty = qwert.scrolled_text

        qwerty.insert(END, 'hi', )

    def __init__(self, frame):
        self.frame = frame
        # self.vertical_pane = ttk.PanedWindow(self.frame, orient=VERTICAL)
        # self.vertical_pane.grid(row=0, column=0, sticky="nsew")
        # self.frame.columnconfigure(0, weight=1)
        # self.frame.rowconfigure(0, weight=1)

        self.horizontal_pane = ttk.PanedWindow(self.frame, orient=HORIZONTAL)
        # self.vertical_pane.add(self.horizontal_pane, weight=1)
        # self.horizontal_pane.columnconfigure(0, weight=1)
        self.horizontal_pane.grid(sticky="nsew")
        self.horizontal_pane.columnconfigure(0, weight=1)
        self.horizontal_pane.rowconfigure(0, weight=1)
        self.horizontal_pane.columnconfigure(1, weight=10)

        self.main = ttk.Labelframe(self.horizontal_pane, text='hi')
        self.horizontal_pane.add(self.main, weight=1)
        self.main.grid(row=0, column=0, sticky="nsew")
        # self.main.columnconfigure(1, weight=1)
        self.main.rowconfigure(3, weight=1, minsize=20)
        self.main.columnconfigure(0, weight=0, minsize=50)
        self.main.columnconfigure(1, weight=1, minsize=50)
        self.main.rowconfigure(4, weight=1, minsize=20)

        self.vorname_label = ttk.Label(self.main, text="Vorname:")
        self.vorname_label.grid(row=0, column=0, sticky=W)
        self.vorname_entry = ttk.Entry(self.main, width=25)
        self.vorname_entry.grid(row=0, column=1, sticky=(W, E))

        self.nachname_label = ttk.Label(self.main, text="Nachname:")
        self.nachname_label.grid(row=1, column=0, sticky=W)
        self.nachname_entry = ttk.Entry(self.main, width=25)
        self.nachname_entry.grid(row=1, column=1, sticky=(W, E))

        self.matrnr_label = ttk.Label(self.main, text="Matrikelnummer:")
        self.matrnr_label.grid(row=2, column=0, sticky=W)
        self.matrnr_entry = ttk.Entry(self.main, width=25)
        self.matrnr_entry.grid(row=2, column=1, sticky="ew")

        button_save = ttk.Button(self.main, text="Save", command=self.insert_stud)
        button_save.grid(column=0, row=3, sticky="nsew")
        button_search = ttk.Button(self.main, text="Search", command=self.search)
        button_search.grid(column=0, row=4, sticky="nsew")
        button_delete = ttk.Button(self.main, text="Delete", command=self.remove_stud)
        button_delete.grid(column=1, row=3, sticky="nsew")
        button1 = ttk.Button(self.main, text="Print my name", command=self.printName)
        button1.grid(column=1, row=4, sticky="nsew")

        self.console = ttk.Labelframe(self.horizontal_pane, text='Console')
        self.console.grid(column=1, row=0, sticky="nsew")
        self.console.columnconfigure(0, weight=1)
        self.console.rowconfigure(0, weight=10)
        ConsoleUi(self.console)

    def getName(self):
        asdf = self.vorname_entry.get()
        return asdf


# studs = get_studs_by_name('Simon')
# print(studs)

main1 = Main(root)

# **** Status Bar ****


blabla = main1.getName()

status = Label(main1.frame, text="Ausgewählte Tabelle:" + blabla, bd=1, relief=SUNKEN, anchor=W)
status.grid(row=1, column=0, sticky="nsew")
status.rowconfigure(0, weight=1)
status.columnconfigure(0, weight=1)

root.mainloop()
