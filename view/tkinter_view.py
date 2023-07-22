import tkinter as tk
import customtkinter as ctk

from view.components.header import Header
class MainWindow:
    def __init__(self, ubicacion_view, destino_view):
        self.ubicacion_view = ubicacion_view
        self.destino_view = destino_view
        self.frames = []
        self.frames_footer = []

        self.current_frame_index = 0
        self.app()

    def app(self):
        #VARIABLES
        self.WIDTH = 1600
        self.HEIGHT = 850
        self.PRIMARY_COLOR = '#525869'
        self.SECONDARY_COLOR = '#f5f5f5'
        self.THIRD_COLOR = '#4682b4'
        self.PRIMARY_FONT = ('Arial Baltic', 20, 'bold')
        self.SECONDARY_FONT = ('Arial Baltic', 20)


        #ROOT
        self.root = tk.Tk()
        self.root.configure(background=self.PRIMARY_COLOR)
        self.root.title("Aplicación de Destinos Culinarios")
        self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.root.resizable(False, False)

        self.main_frame = tk.Frame(self.root, background=self.PRIMARY_COLOR)
        self.main_frame.grid(row=0, column=0, sticky="nsew", columnspan=3)


        ### HEADER
        self.header = Header(
            self.main_frame,
            self.PRIMARY_COLOR,
            self.PRIMARY_FONT,
            self.SECONDARY_COLOR,
            self.WIDTH)


        ### BODY


        ## FOOTER



        self.root.mainloop()

    ## CONFIG FRAMES



