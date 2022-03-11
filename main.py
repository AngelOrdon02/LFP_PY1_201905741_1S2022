'''
Angel Geovanny Ordón Colchaj
201905741
'''
from tkinter import *

window = Tk()

window.title("Bienvenido a mi APP")

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 3):
        frame = Frame(
            master=window,
            relief=RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)

        label = Label(master=frame, text=f"Row {i}\n Column {j}")
        label.pack(padx=5, pady=5)

window.mainloop()