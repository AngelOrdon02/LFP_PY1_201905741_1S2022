from tkinter import *
from tkinter import messagebox

# Vistas
#from views.dashboardView import DashboardView

# Instancias
#view_dashboardView = DashboardView()

class ReportsView:

    @staticmethod
    def __call__():
        import views.dashboardView
        view_dashboardView = views.dashboardView.DashboardView()

        #self.window = window
        
        window = Tk()

        window.title("Bienvenido a mi APP")

        '''window.geometry("640x360")
        window.resizable(0, 0)
        window.eval('tk::PlaceWindow . center')'''

        # ------------------------------
        w = 640 # width for the Tk root
        h = 360 # height for the Tk root

        # get screen width and height
        ws = window.winfo_screenwidth() # width of the screen
        hs = window.winfo_screenheight() # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)

        # set the dimensions of the screen 
        # and where it is placed
        window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        window.resizable(0, 0)
        # ------------------------------

        # Configuracion del grid
        window.columnconfigure(0, weight=2, minsize=50)
        window.columnconfigure(1, weight=5)
        window.columnconfigure(2, weight=2, minsize=50)

        window.rowconfigure(0, weight=3, minsize=50)
        window.rowconfigure(1, weight=2, minsize=50)
        window.rowconfigure(2, weight=1, minsize=50)
        window.rowconfigure(3, weight=1, minsize=50)

        # Cuerpo
        # Titulo
        welcome_label = Label(window, text="Tablero", font=("Arial", 24))
        welcome_label.grid(column=1, row=0, padx=5, pady=5)

        # Botones
        analyzer_button = Button(window, text="Analizador", font=("Arial", 14), command=lambda: clicked1())
        analyzer_button.grid(column=1, row=1, padx=5, pady=5)

        reports_button = Button(window, text="Reportes", font=("Arial", 14), command=lambda: clicked2())
        reports_button.grid(column=1, row=2, padx=5, pady=5)

        # Salir
        exit_button = Button(window, text="Salir", font=("Arial", 14), command=lambda: exit())
        exit_button.grid(column=2, row=0, sticky=NE, padx=5, pady=5)

        def clicked1():
            pass

        def clicked2():
            #print(hola)
            pass
        
        def exit():
            messagebox.showinfo('Mensaje', 'Gracias por utilizar el programa.')
            window.destroy()
        window.mainloop()
