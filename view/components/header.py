
import tkinter as tk
class Header:
    def __init__(self, main_frame, PRIMARY_COLOR, PRIMARY_FONT, SECONDARY_COLOR, WIDTH):
        self.frame_header = tk.Frame(main_frame, background=PRIMARY_COLOR)
        self.frame_header.grid(row=0, column=0, sticky="ew", pady=20, columnspan=3)
        self.frame_header.grid_rowconfigure(0, weight=1, minsize=50,)
        self.frame_header.grid_columnconfigure(0, weight=1, minsize=WIDTH)

        self.label = tk.Label(
            self.frame_header,
            text="Acá va el titulo principal",
            background=PRIMARY_COLOR,
            font=PRIMARY_FONT,
            foreground=SECONDARY_COLOR
        )
        self.label.grid(row=0, column=0, columnspan=3, sticky='ew')