import tkinter as tk
class Footer:
    def __init__(self, main_frame, PRIMARY_COLOR, SECONDARY_COLOR, SECONDARY_FONT, WIDTH, THIRD_COLOR):
        self.main_frame = main_frame
        self.PRIMARY_COLOR = PRIMARY_COLOR
        self.SECONDARY_COLOR =  SECONDARY_COLOR
        self.SECONDARY_FONT = SECONDARY_FONT
        self.WIDTH = WIDTH
        self.THIRD_COLOR = THIRD_COLOR

        self.frame_footer = tk.Frame(self.main_frame, background=self.PRIMARY_COLOR)
        self.frame_footer.grid(row=2, column=0, sticky="ew", pady=10, columnspan=3)
        self.frame_footer.grid_rowconfigure(0, weight=1, minsize=50, )
        self.frame_footer.grid_columnconfigure(0, weight=1, minsize=self.WIDTH)

        # FOOTER FRAME 1
        

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

         # FOOTER
        self.frames_footer = [footer1, footer2, footer3]
        self.current_frame_footer = footer1
        self.current_frame_footer.grid(row=2, column=0, sticky="nsew")



    