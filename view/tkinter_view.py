import tkinter as tk
from view.components.header import Header
from view.components.body import Body
import view.config as cf
class MainWindow:
    def __init__(self, ubicacion_view, destino_view):
        self.ubicacion_view = ubicacion_view
        self.destino_view = destino_view

        self.app()

    def app(self):

        #ROOT
        self.root = tk.Tk()
        self.root.configure(background=cf.PRIMARY_COLOR)
        self.root.title("Aplicación de Destinos Culinarios")
        self.root.geometry(f"{cf.WIDTH}x{cf.HEIGHT}")
        self.root.resizable(False, False)

        self.main_frame = tk.Frame(self.root, background=cf.PRIMARY_COLOR)
        self.main_frame.grid(row=0, column=0, sticky="nsew", columnspan=3)


        ### HEADER
        self.header = Header(
            self.main_frame,
            )


        ### BODY
        self.body = Body(
            self.main_frame,
            self.ubicacion_view,
            self.destino_view
        )

        ## FOOTER



        self.root.mainloop()

    ## CONFIG FRAMES

    

