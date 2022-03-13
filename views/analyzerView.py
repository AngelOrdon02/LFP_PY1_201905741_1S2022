from tkinter import *
import tkinter.scrolledtext as scrolledtext

# Vistas
#from views.dashboardView import DashboardView

# Instancias
#view_dashboardView = DashboardView()

class AnalyzerView:

    @staticmethod
    def __call__():
        import views.dashboardView
        view_dashboardView = views.dashboardView.DashboardView()
        #views.dashboardView.DashboardView()

        #self.window = window
        
        window = Tk()

        window.title("Bienvenido a mi APP")

        # ------------------------------
        w = 800 # width for the Tk root
        h = 600 # height for the Tk root

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
        window.columnconfigure(0, weight=2, minsize=100)
        window.columnconfigure(1, weight=5)
        window.columnconfigure(2, weight=2, minsize=100)

        window.rowconfigure(0, weight=1, minsize=50)
        window.rowconfigure(1, weight=1, minsize=50)
        window.rowconfigure(2, weight=1, minsize=50)
        window.rowconfigure(3, weight=5, minsize=50)
        window.rowconfigure(4, weight=1, minsize=50)

        # Cuerpo
        # Titulo
        welcome_label = Label(window, text="Analizador", font=("Arial", 24))
        welcome_label.grid(column=1, row=1, sticky=W, padx=5, pady=5)

        # Texto
        txt = scrolledtext.ScrolledText(window, undo=True)
        txt['font'] = ('consolas', '12')
        #txt.pack(expand=True, fill='both')
        #text = Text()
        txt.grid(column=1, row=3, sticky=NSEW, padx=5, pady=5)

        # Botones
        return_button = Button(window, text="Regresar", font=("Arial", 14), command=lambda: return_view())
        return_button.grid(column=0, row=0, sticky=NW, padx=5, pady=5)

        upload_button = Button(window, text="Subir", font=("Arial", 14), command=lambda: clicked2())
        upload_button.grid(column=1, row=2, sticky=E, padx=5, pady=5)

        analyzer_button = Button(window, text="Analizar", font=("Arial", 14), command=lambda: analyzer())
        analyzer_button.grid(column=1, row=4, sticky=NE, padx=5, pady=5)

        save_button = Button(window, text="Guardar", font=("Arial", 14), command=lambda: save())
        save_button.grid(column=2, row=4, sticky=NE, padx=5, pady=5)

        def return_view():
            window.destroy()
            hola = "hola"
            view_dashboardView(hola)
            pass

        def clicked2():
            #print(hola)
            pass

        def save():
            pass

        def analyzer():
            pass
        
        '''def exit():
            messagebox.showinfo('Mensaje', 'Gracias por utilizar el programa.')
            window.destroy()'''
        window.mainloop()
