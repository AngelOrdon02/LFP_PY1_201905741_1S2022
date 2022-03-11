from tkinter import *

class DashboardView():

    @staticmethod
    def __call__():
        #self.window = window

        window = Tk()

        window.title("Bienvenido a mi APP")
        window.geometry("300x200")
        window.eval('tk::PlaceWindow . center')
        window.resizable(0, 0)

        # Configuracion del grid
        window.columnconfigure(0, weight=2)
        window.columnconfigure(1, weight=5)
        window.columnconfigure(2, weight=2)

        window.rowconfigure(0, weight=3, minsize=50)
        window.rowconfigure(1, weight=2, minsize=50)
        window.rowconfigure(2, weight=1, minsize=50)

        # Cuerpo
        # Titulo
        welcome_label = Label(window, text="Tablero", font=("Arial", 24))
        welcome_label.grid(column=1, row=0, padx=5, pady=5)

        # Boton
        getin_button = Button(window, text="Entrar", font=("Arial", 14), command=lambda: clicked())
        getin_button.grid(column=1, row=1, padx=5, pady=5)

        def clicked():
            pass      
        window.mainloop()
'''
if __name__ == "__main__":
    window = Tk()
    app = Main(window)
    window.mainloop()'''
