import tkinter as tk

from view.tkinter_map import TkinterMapView

class MainWindow:
    def __init__(self, ubicacion_view, destino_view):
        self.ubicacion_view = ubicacion_view
        self.destino_view = destino_view
        self.frames = []
        self.frames_footer = []

        self.current_frame_index = 0
        self.app()

    def app(self):
        self.root = tk.Tk()
        self.root.title("Aplicación de Destinos Culinarios")
        self.WEITH = 1600
        self.HEIGHT = 800
        self.root.geometry(f"{self.WEITH}x{self.HEIGHT}")
        self.root.resizable(False, False)

        self.main_frame = tk.Frame(self.root)
        self.main_frame.grid(row=0, column=0, sticky="nsew", columnspan=3)

        ### HEADER
        self.frame_header = tk.Frame(self.main_frame, bg='green')
        self.frame_header.grid(row=0, column=0, sticky="ew", pady=20, columnspan=3)
        self.frame_header.grid_rowconfigure(0, weight=1, minsize=50,)
        self.frame_header.grid_columnconfigure(0, weight=1, minsize=self.WEITH)
        self.label = tk.Label(self.frame_header, text="Acá va el titulo principal", )
        self.label.grid(row=0, column=0, columnspan=3, sticky='ew')


        ### BODY
        self.frame_body = tk.Frame(self.main_frame)
        self.frame_body.grid_rowconfigure(0, weight=1)
        self.frame_body.grid(row=1, column=0, sticky="nsew")

        self.frame_body_left = tk.Frame(self.frame_body, width=200)
        self.frame_body_left.grid_propagate(False)
        self.frame_body_left.grid_columnconfigure(0, weight=1)
        self.frame_body_left.grid_rowconfigure(0, weight=1)
        self.frame_body_left.grid(row=0, column=0, sticky="nsew")

        self.frame_body_center = tk.Frame(self.frame_body)
        self.frame_body_center.grid_rowconfigure(0, weight=1)
        self.frame_body_center.grid(row=0, column=1, sticky="nsew")

        self.frame_body_right = tk.Frame(self.frame_body, width=200)
        self.frame_body_right.grid_propagate(False)
        self.frame_body_right.grid_columnconfigure(0, weight=1)
        self.frame_body_right.grid_rowconfigure(0, weight=1)
        self.frame_body_right.grid(row=0, column=2, sticky="nsew")

        self.boton_anterior = tk.Button(self.frame_body_left, text="Anterior", command=self.prev_frame)
        self.boton_anterior.grid(row=0, column=0)

        self.boton_siguiente = tk.Button(self.frame_body_right, text="Siguiente", command=self.next_frame)
        self.boton_siguiente.grid(row=0, column=0)

        ## FOOTER
        self.frame_footer = tk.Frame(self.main_frame)
        self.frame_footer.grid(row=2, column=0, sticky="ew", pady=20, columnspan=3)
        self.frame_footer.grid_rowconfigure(0, weight=1, minsize=50, )
        self.frame_footer.grid_columnconfigure(0, weight=1, minsize=self.WEITH)

        footer1 = tk.Frame(self.frame_footer)
        footer1.grid_rowconfigure(0, weight=1)
        footer1.grid_columnconfigure(0, weight=1)

        label1 = tk.Label(footer1, text="Footer1")
        label1.grid(row=0, column=0, columnspan=3)

        footer2 = tk.Frame(self.frame_footer)
        footer2.grid_rowconfigure(0, weight=1)
        footer2.grid_columnconfigure(0, weight=1)


        label2 = tk.Label(footer2, text="Footer2")
        label2.grid(row=0, column=0, columnspan=3)

        footer3 = tk.Frame(self.frame_footer)
        footer3.grid_rowconfigure(0, weight=1)
        footer3.grid_columnconfigure(0, weight=1)


        label3 = tk.Label(footer3, text="Footer3")
        label3.grid(row=0, column=0, columnspan=3)

        ## FRAMES
        frame1 = tk.Frame(self.frame_body_center, width=1200, height=600)
        frame1.grid_propagate(False)
        frame1.grid_rowconfigure(0, weight=1)
        frame1.grid_columnconfigure(0, weight=1)
        etiqueta1 = tk.Label(frame1, text="Contenido del frame 1")
        etiqueta1.grid(row=1, column=1)

        frame2 = tk.Frame(self.frame_body_center, width=1200, height=600, bg="green")
        frame2.grid_propagate(False)
        frame2.grid_rowconfigure(0, weight=1)
        frame2.grid_columnconfigure(0, weight=1)
        etiqueta2 = tk.Label(frame2, text="Contenido del frame 2")
        etiqueta2.grid(row=1, column=1)

        frame3 = tk.Frame(self.frame_body_center, width=1200, height=600, bg="blue")
        frame3.grid_propagate(False)
        frame3.grid_rowconfigure(0, weight=1)
        frame3.grid_columnconfigure(0, weight=1)
        etiqueta3 = tk.Label(frame3, text="Contenido del frame 3")
        etiqueta3.grid(row=1, column=1)

        self.frames = [frame1, frame2, frame3]
        self.current_frame = self.frames[self.current_frame_index]
        self.current_frame.grid(row=1, column=1, sticky="nsew")

        self.frames_footer = [footer1, footer2, footer3]
        self.current_frame_footer = footer1
        self.current_frame_footer.grid(row=2, column=0, sticky="nsew")

        self.map_view = TkinterMapView(frame1, tk)

        self.root.mainloop()

    def next_frame(self):
        self.current_frame.grid_remove()
        self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)
        self.current_frame = self.frames[self.current_frame_index]
        self.current_frame.grid(row=0, column=0, sticky="nsew")

        self.current_frame_footer.grid_remove()
        self.current_frame_footer = self.frames_footer[self.current_frame_index]
        self.current_frame_footer.grid(row=2, column=0, sticky="nsew")

    def prev_frame(self):
        self.current_frame.grid_remove()
        self.current_frame_footer.grid_remove()
        self.current_frame_index = (self.current_frame_index - 1) % len(self.frames)

        self.current_frame = self.frames[self.current_frame_index]
        self.current_frame.grid(row=0, column=0, sticky="nsew")
        self.current_frame_footer = self.frames_footer[self.current_frame_index]
        self.current_frame_footer.grid(row=2, column=0, sticky="nsew")
