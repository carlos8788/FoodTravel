
import tkinter as tk
import view.config as cf
class Header:
    def __init__(self, main_frame):
        self.frame_header = tk.Frame(main_frame, background=cf.PRIMARY_COLOR)
        self.frame_header.grid(row=0, column=0, sticky="ew", pady=20, columnspan=3)
        self.frame_header.grid_rowconfigure(0, weight=1, minsize=50,)
        self.frame_header.grid_columnconfigure(0, weight=1, minsize=cf.WIDTH)

        self.label = tk.Label(
            self.frame_header,
            text="Acá va el titulo principal",
            background=cf.PRIMARY_COLOR,
            font=cf.PRIMARY_FONT,
            foreground=cf.SECONDARY_COLOR,
            justify=tk.CENTER
        )
        self.label.grid(row=0, column=0, columnspan=3)