import tkinter as tk
from .frames.frame_1 import Frame1
from .frames.frame_2 import Frame2
from .frames.frame_3 import Frame3
import view.config as cf


class Body:
    def __init__(self, main_frame, ubicacion_view, destino_view):
        self.frames = []
        self.frames_footer = []
        self.current_frame_index = 0

        self.ubicacion_view = ubicacion_view
        self.destino_view = destino_view

        self.frame_body = tk.Frame(main_frame, background=cf.PRIMARY_COLOR)
        self.frame_body.grid_rowconfigure(0, weight=1)
        self.frame_body.grid(row=1, column=0, sticky="nsew")

        self.frame_body_left = tk.Frame(self.frame_body, width=100, background=cf.PRIMARY_COLOR)
        _config_frame_body(self.frame_body_left)
        self.frame_body_left.grid(row=0, column=0, sticky="nsew")

        self.frame_body_center = tk.Frame(self.frame_body)
        self.frame_body_center.grid_rowconfigure(0, weight=1)
        self.frame_body_center.grid(row=0, column=1, sticky="nsew")

        self.frame_body_right = tk.Frame(self.frame_body, width=100, background=cf.PRIMARY_COLOR)
        _config_frame_body(self.frame_body_right)
        self.frame_body_right.grid(row=0, column=2, sticky="nsew")

        # Button left
        self.btn_prev = tk.Button(
            self.frame_body_left,
            text="<",
            command=self._prev_frame,
            borderwidth=0,
            relief="ridge",
            font='Arial 35',
            background=cf.PRIMARY_COLOR,
            activebackground=cf.PRIMARY_COLOR,
        )
        self.btn_prev.grid(row=0, column=0)

        # Button right
        self.btn_next = tk.Button(
            self.frame_body_right,
            text=">",
            command=self._next_frame,
            borderwidth=0,
            relief="ridge",
            font='Arial 35',
            background=cf.PRIMARY_COLOR,
            activebackground=cf.PRIMARY_COLOR,

        )
        self.btn_next.grid(row=0, column=0)

        # FRAMES

        frame1 = Frame1(
            self.frame_body_center,
            _config_frame_body,
            self.ubicacion_view,
            self.destino_view
        )

        frame2 = Frame2(
            self.frame_body_center,
            _config_frame_body
        )
        frame3 = Frame3(
            self.frame_body_center,
        )

        self.frames = [frame1.get_frame(), frame2.get_frame(), frame3.get_frame()]
        self.current_frame = self.frames[self.current_frame_index]
        self.current_frame.grid(row=0, column=0, sticky="nsew")

    def _next_frame(self):
        self.current_frame.grid_remove()
        self.current_frame_index = (self.current_frame_index + 1) % len(self.frames)
        self.current_frame = self.frames[self.current_frame_index]
        self.current_frame.grid(row=0, column=0, sticky="nsew")

    def _prev_frame(self):
        self.current_frame.grid_remove()
        self.current_frame_index = (self.current_frame_index - 1) % len(self.frames)
        self.current_frame = self.frames[self.current_frame_index]
        self.current_frame.grid(row=0, column=0, sticky="nsew")


def _config_frame_body(frame_config):
    frame_config.grid_propagate(False)
    frame_config.grid_rowconfigure(0, weight=1)
    frame_config.grid_columnconfigure(0, weight=1)