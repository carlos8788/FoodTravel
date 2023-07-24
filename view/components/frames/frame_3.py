import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path
import os
import view.config as cf

class Frame3:
    def __init__(self, main_frame):
        self.main_frame = main_frame
        self.BASE = Path(__file__).resolve().parent
        self.frame = tk.Frame(self.main_frame, width=800, height=450, pady=5, background=cf.PRIMARY_COLOR)
        self.canvas = tk.Canvas(self.frame, width=800, height=450, )
        self.canvas.pack(fill='both', expand=True)
        img = Image.open(os.path.join(self.BASE, 'img/salta.png'))
        self.background_image = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor='nw', image=self.background_image)
        self.canvas.image = self.background_image

        self.button1 = tk.Button(
            self.frame,
            text='Button 1',
            borderwidth=0,
            relief='ridge',
            width=16,
            font=cf.SECONDARY_FONT
        )
        self.button2 = tk.Button(
            self.frame,
            text='Button 2',
            borderwidth=0,
            relief='ridge',
            width=16,
            font=cf.SECONDARY_FONT
        )
        self.button3 = tk.Button(
            self.frame,
            text='Button 3',
            borderwidth=0,
            relief='ridge',
            width=16,
            font=cf.SECONDARY_FONT
        )

        # Add buttons to canvas
        self.canvas.create_window(190, 400, window=self.button1)
        self.canvas.create_window(410, 400, window=self.button2)
        self.canvas.create_window(630, 400, window=self.button3)
    def get_frame(self):
        return self.frame