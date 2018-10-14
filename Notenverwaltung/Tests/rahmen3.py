import tkinter as Tk


class Hauptfenster(Tk.Frame):
    def __init__(self, master):
        Tk.Frame.__init__(self, master)
        self.pack(expand='yes', fill='both')
        self.Button_open = Tk.Button(self,
                                     text='Ok', bg='green',
                                     border="1", relief='ridge',
                                     command=self.opentop2)
        self.Button_open.pack(expand='true', anchor='n')

    def opentop2(self):
        # Oeffnet Fenster 2
        oeffnen = Fenster2(self)


class Fenster2(Tk.Toplevel):
    def __init__(self, master):
        # Ein Toplevel 2 erstellen
        Tk.Toplevel.__init__(self, master)
        self.Label = Tk.Label(self, text='Ich bin ein Text',
                              width=10, height=2)
        self.Label.pack(expand='true', fill='both', anchor='n')

        self.grab_set()
        self.focus_set()
        self.wait_window()


def _main():
    root = Tk.Tk()
    app = Hauptfenster(root)
    root.mainloop()


if __name__ == '__main__':
    _main()