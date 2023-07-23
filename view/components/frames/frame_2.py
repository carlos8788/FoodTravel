from tkinter import Frame, Label


class Frame2:
    def __init__(self, frame_body, config_frame) -> None:
        self.frame_body_center = frame_body
        self._config_frame_body = config_frame
        self.frame2 = Frame(self.frame_body_center,
                       width=1200, height=600, bg="green")
        self._config_frame_body(self.frame2)
        # frame2.grid(row=0, column=0)
        etiqueta2 = Label(self.frame2, text="Contenido del frame 2")
        etiqueta2.grid(row=1, column=1)

    def get_frame(self):
        return self.frame2
