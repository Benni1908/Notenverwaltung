import tkinter as tk

fenster=tk.Tk()

rahmen=tk.LabelFrame(fenster, bd=2, text='Das ist der Rahmen')
rahmen.pack(padx=10, pady=10)

text=tk.Label(rahmen, text="Im Rahmen")
text.pack()

button=tk.Button(fenster, text="Nicht im Rahmen")
button.pack()

fenster.mainloop()