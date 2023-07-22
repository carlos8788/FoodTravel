import tkinter as tk
from view.tkinter_map import TkinterMapView
class Body:
    def __init__(self, main_frame, PRIMARY_COLOR, THIRD_COLOR):

        self.THIRD_COLOR = THIRD_COLOR

        self.frame_body = tk.Frame(main_frame, background=PRIMARY_COLOR)
        self.frame_body.grid_rowconfigure(0, weight=1)
        self.frame_body.grid(row=1, column=0, sticky="nsew")

        self.frame_body_left = tk.Frame(self.frame_body, width=200, background=PRIMARY_COLOR)
        self.frame_body_left(self.frame_body_left)
        self.frame_body_left.grid(row=0, column=0, sticky="nsew")

        self.frame_body_center = tk.Frame(self.frame_body)
        self.frame_body_center.grid_rowconfigure(0, weight=1)
        self.frame_body_center.grid(row=0, column=1, sticky="nsew")

        self.frame_body_right = tk.Frame(self.frame_body, width=200, background=PRIMARY_COLOR)
        self._config_frame_body(self.frame_body_right)
        self.frame_body_right.grid(row=0, column=2, sticky="nsew")

        # Button left
        self.boton_anterior = tk.Button(
            self.frame_body_left,
            text="<",
            command=self._prev_frame,
            borderwidth=0,
            relief="ridge",
            font='Arial 35',
            background=PRIMARY_COLOR,
            activebackground=PRIMARY_COLOR,
        )
        self.boton_anterior.grid(row=0, column=0)

        # Button right
        self.boton_siguiente = tk.Button(
            self.frame_body_right,
            text=">",
            command=self._next_frame,
            borderwidth=0,
            relief="ridge",
            font='Arial 35',
            background=PRIMARY_COLOR,
            activebackground=PRIMARY_COLOR,

        )
        self.boton_siguiente.grid(row=0, column=0)

        ## FRAMES
        frame1 = tk.Frame(self.frame_body_center, width=1200, height=600, background=PRIMARY_COLOR)
        self._config_frame_body(frame1)
        self.map_view = TkinterMapView(frame1, tk)

        frame2 = tk.Frame(self.frame_body_center, width=1200, height=600, bg="green")
        self._config_frame_body(frame2)
        etiqueta2 = tk.Label(frame2, text="Contenido del frame 2")
        etiqueta2.grid(row=1, column=1)

        frame3 = tk.Frame(self.frame_body_center, width=1200, height=600, bg="blue")
        self._config_frame_body(frame3)
        etiqueta3 = tk.Label(frame3, text="Contenido del frame 3")
        etiqueta3.grid(row=1, column=1)

        self.frames = [frame1, frame2, frame3]
        self.current_frame = self.frames[self.current_frame_index]
        self.current_frame.grid(row=1, column=1, sticky="nsew")

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
        self.current_frame_footer.grid(row=2, column=0, sticky="nsew", pady=5)

    def _prev_frame(self):
        self.current_frame.grid_remove()
        self.current_frame_footer.grid_remove()
        self.current_frame_index = (self.current_frame_index - 1) % len(self.frames)

        self.current_frame = self.frames[self.current_frame_index]
        self.current_frame.grid(row=0, column=0, sticky="nsew")
        self.current_frame_footer = self.frames_footer[self.current_frame_index]
        self.current_frame_footer.grid(row=2, column=0, sticky="nsew", pady=5)


