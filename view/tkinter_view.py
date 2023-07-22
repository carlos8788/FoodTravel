import tkinter as tk
import customtkinter as ctk
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
        #VARIABLES
        self.WEITH = 1600
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
        self.root.geometry(f"{self.WEITH}x{self.HEIGHT}")
        self.root.resizable(False, False)

        self.main_frame = tk.Frame(self.root, background=self.PRIMARY_COLOR)
        self.main_frame.grid(row=0, column=0, sticky="nsew", columnspan=3)


        ### HEADER
        self.frame_header = tk.Frame(self.main_frame, background=self.PRIMARY_COLOR)
        self.frame_header.grid(row=0, column=0, sticky="ew", pady=20, columnspan=3)
        self.frame_header.grid_rowconfigure(0, weight=1, minsize=50,)
        self.frame_header.grid_columnconfigure(0, weight=1, minsize=self.WEITH)

        self.label = tk.Label(
            self.frame_header,
            text="Acá va el titulo principal",
            background=self.PRIMARY_COLOR,
            font=self.PRIMARY_FONT,
            foreground=self.SECONDARY_COLOR
        )
        self.label.grid(row=0, column=0, columnspan=3, sticky='ew')


        ### BODY
        self.frame_body = tk.Frame(self.main_frame, background=self.PRIMARY_COLOR)
        self.frame_body.grid_rowconfigure(0, weight=1)
        self.frame_body.grid(row=1, column=0, sticky="nsew")

        self.frame_body_left = tk.Frame(self.frame_body, width=200, background=self.PRIMARY_COLOR)
        self.frame_body_left.grid_propagate(False)
        self.frame_body_left.grid_columnconfigure(0, weight=1)
        self.frame_body_left.grid_rowconfigure(0, weight=1)
        self.frame_body_left.grid(row=0, column=0, sticky="nsew")

        self.frame_body_center = tk.Frame(self.frame_body)
        self.frame_body_center.grid_rowconfigure(0, weight=1)
        self.frame_body_center.grid(row=0, column=1, sticky="nsew")

        self.frame_body_right = tk.Frame(self.frame_body, width=200, background=self.PRIMARY_COLOR)
        self.frame_body_right.grid_propagate(False)
        self.frame_body_right.grid_columnconfigure(0, weight=1)
        self.frame_body_right.grid_rowconfigure(0, weight=1)
        self.frame_body_right.grid(row=0, column=2, sticky="nsew")

        #Button left
        self.boton_anterior = tk.Button(
            self.frame_body_left,
            text="<",
            command=self._prev_frame,
            borderwidth=0,
            relief="ridge",
            font='Arial 35',
            background=self.PRIMARY_COLOR,
            activebackground=self.PRIMARY_COLOR,
        )
        self.boton_anterior.grid(row=0, column=0)

        #Button right
        self.boton_siguiente = tk.Button(
            self.frame_body_right,
            text=">",
            command=self._next_frame,
            borderwidth=0,
            relief="ridge",
            font='Arial 35',
            background=self.PRIMARY_COLOR,
            activebackground=self.PRIMARY_COLOR,

        )
        self.boton_siguiente.grid(row=0, column=0)

        ## FRAMES
        frame1 = tk.Frame(self.frame_body_center, width=1200, height=600, background=self.PRIMARY_COLOR)
        frame1.grid_propagate(False)
        frame1.grid_rowconfigure(0, weight=1)
        frame1.grid_columnconfigure(0, weight=1)

        frame2 = tk.Frame(self.frame_body_center, width=1200, height=600, bg="green")
        frame2.grid_propagate(False)
        frame2.grid_rowconfigure(0, weight=1)
        frame2.grid_columnconfigure(0, weight=1)
        etiqueta2 = tk.Label(frame2, text="Contenido del frame 2")
        etiqueta2.grid(row=1, column=1)

        frame3 = tk.Frame(self.frame_body_center, width=1200, height=600, bg="blue")
        self._config_frame_body(frame3)
        etiqueta3 = tk.Label(frame3, text="Contenido del frame 3")
        etiqueta3.grid(row=1, column=1)

        self.frames = [frame1, frame2, frame3]
        self.current_frame = self.frames[self.current_frame_index]
        self.current_frame.grid(row=1, column=1, sticky="nsew")

        ## FOOTER

        self.frame_footer = tk.Frame(self.main_frame, background=self.PRIMARY_COLOR)
        self.frame_footer.grid(row=2, column=0, sticky="ew", pady=10, columnspan=3)
        self.frame_footer.grid_rowconfigure(0, weight=1, minsize=50, )
        self.frame_footer.grid_columnconfigure(0, weight=1, minsize=self.WEITH)

        # FOOTER FRAME 1
        footer1 = tk.Frame(self.frame_footer, background=self.PRIMARY_COLOR)

        self.button1 = tk.Button(
            footer1,
            text="Footer1",
            background=self.THIRD_COLOR,
            font= self.SECONDARY_FONT,
            foreground=self.SECONDARY_COLOR,
            borderwidth=0,
            relief='ridge',
        )
        self.button1.bind("<Enter>", self._change_to_red)
        self.button1.bind("<Leave>", self._change_to_original)

        self.button1.grid(row=0, column=0, padx=(275,100))

        self.button2 = tk.Button(
            footer1,
            text="Footer1",
            background=self.THIRD_COLOR,
            font=self.SECONDARY_FONT,
            foreground=self.SECONDARY_COLOR,
            borderwidth=0,
            relief='ridge',
        )
        self.button2.bind("<Enter>", self._change_to_red)
        self.button2.bind("<Leave>", self._change_to_original)

        self.button2.grid(row=0, column=1, padx=(100, 100))

        self.button3 = tk.Button(
            footer1,
            text="Footer1",
            background=self.THIRD_COLOR,
            font=self.SECONDARY_FONT,
            foreground=self.SECONDARY_COLOR,
            borderwidth=0,
            relief='ridge',
        )
        self.button3.bind("<Enter>", self._change_to_red)
        self.button3.bind("<Leave>", self._change_to_original)

        self.button3.grid(row=0, column=2, padx=(100, 100))

        self.button4 = tk.Button(
            footer1,
            text="Footer1",
            background=self.THIRD_COLOR,
            font=self.SECONDARY_FONT,
            foreground=self.SECONDARY_COLOR,
            borderwidth=0,
            relief='ridge',
        )
        self.button4.bind("<Enter>", self._change_to_red)
        self.button4.bind("<Leave>", self._change_to_original)

        self.button4.grid(row=0, column=3, padx=(100, 100))

        # FOOTER FRAME 2
        footer2 = tk.Frame(self.frame_footer, background=self.PRIMARY_COLOR)
        footer2.grid_rowconfigure(0, weight=1)
        footer2.grid_columnconfigure(0, weight=1)


        label2 = tk.Label(footer2, text="Footer2", background=self.PRIMARY_COLOR)
        label2.grid(row=0, column=0, columnspan=3)

        footer3 = tk.Frame(self.frame_footer, background=self.PRIMARY_COLOR)
        footer3.grid_rowconfigure(0, weight=1)
        footer3.grid_columnconfigure(0, weight=1)


        label3 = tk.Label(footer3, text="Footer3", background=self.PRIMARY_COLOR)
        label3.grid(row=0, column=0, columnspan=3)

        self.frames_footer = [footer1, footer2, footer3]
        self.current_frame_footer = footer1
        self.current_frame_footer.grid(row=2, column=0, sticky="nsew")

        self.map_view = TkinterMapView(frame1, tk)

        self.root.mainloop()

    ## CONFIG FRAMES

    def _config_frame_body(self, frame_config):
        frame_config.grid_propagate(False)
        frame_config.grid_rowconfigure(0, weight=1)
        frame_config.grid_columnconfigure(0, weight=1)

    def _next_frame(self):
        self.current_frame.grid_remove()
        self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)
        self.current_frame = self.frames[self.current_frame_index]
        self.current_frame.grid(row=0, column=0, sticky="nsew")

        self.current_frame_footer.grid_remove()
        self.current_frame_footer = self.frames_footer[self.current_frame_index]
        self.current_frame_footer.grid(row=2, column=0, sticky="nsew",pady=5)

    def _prev_frame(self):
        self.current_frame.grid_remove()
        self.current_frame_footer.grid_remove()
        self.current_frame_index = (self.current_frame_index - 1) % len(self.frames)

        self.current_frame = self.frames[self.current_frame_index]
        self.current_frame.grid(row=0, column=0, sticky="nsew")
        self.current_frame_footer = self.frames_footer[self.current_frame_index]
        self.current_frame_footer.grid(row=2, column=0, sticky="nsew", pady=5)


    def _change_to_red(self, event):
        event.widget['background'] = '#191970'

    def _change_to_original(self, event):
        event.widget['background'] = self.THIRD_COLOR

