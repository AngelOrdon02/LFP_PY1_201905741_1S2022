'''
Angel Geovanny Ordón Colchaj
201905741
'''
from tkinter import *

# Vistas
from views.dashboardView import DashboardView

# Instancias
view_dashboardView = DashboardView()

class Main:
    def __init__(self, window):
        self.window = window

        #window = Tk()

        self.window.title("Bienvenido a mi APP")
        #self.window.geometry("300x200")
        #self.window.eval('tk::PlaceWindow . center')
        #self.window.resizable(0, 0)

        # ------------------------------
        w = 300 # width for the Tk root
        h = 200 # height for the Tk root

        # get screen width and height
        ws = self.window.winfo_screenwidth() # width of the screen
        hs = self.window.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # set the dimensions of the screen 
        # and where it is placed
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.window.resizable(0, 0)
        # ------------------------------

        # Configuracion del grid
        self.window.columnconfigure(0, weight=2)
        self.window.columnconfigure(1, weight=5)
        self.window.columnconfigure(2, weight=2)

        self.window.rowconfigure(0, weight=3, minsize=50)
        self.window.rowconfigure(1, weight=2, minsize=50)
        self.window.rowconfigure(2, weight=1, minsize=50)

        # Cuerpo
        # Titulo
        self.welcome_label = Label(self.window, text="Bienvenido", font=("Arial", 24))
        self.welcome_label.grid(column=1, row=0, padx=5, pady=5)

        # Boton
        getin_button = Button(window, text="Entrar", font=("Arial", 14), command=lambda: dashboardView())
        getin_button.grid(column=1, row=1, padx=5, pady=5)

        def dashboardView():
            self.window.destroy()
            hola = "hola"
            view_dashboardView(hola)

if __name__ == "__main__":
    window = Tk()
    app = Main(window)
    window.mainloop()
