'''
Angel Geovanny Ordón Colchaj
201905741
'''
from tkinter import *

window = Tk()

window.title("Bienvenido a mi APP")
window.geometry("300x200")
window.eval('tk::PlaceWindow . center')
window.resizable(0, 0)

'''for i in range(3):
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
        label.pack(padx=5, pady=5)'''

# Configuracion del grid
window.columnconfigure(0, weight=2)
window.columnconfigure(1, weight=5)
window.columnconfigure(2, weight=2)

window.rowconfigure(0, weight=3, minsize=50)
window.rowconfigure(1, weight=2, minsize=50)
window.rowconfigure(2, weight=1, minsize=50)

# Cuerpo
# Titulo
welcome_label = Label(window, text="Bienvenido", font=("Arial", 24))
welcome_label.grid(column=1, row=0, padx=5, pady=5)

# Boton
entry_button = Button(window, text="Entrar", font=("Arial", 14))
entry_button.grid(column=1, row=1, padx=5, pady=5)


window.mainloop()