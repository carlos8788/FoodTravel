from tkinter import Label, Button, PhotoImage
import view.config as cf
import webbrowser
from pathlib import Path
import os
from PIL import Image, ImageTk
class Footer:
    def __init__(self, main_frame):
        self.main_frame = main_frame
        self.BASE = Path(__file__).resolve().parent
        print(self.BASE)
        self.label = Label(
            self.main_frame,
            text="By carlos8788",
            font=cf.SECONDARY_FONT,
            foreground='black',
            background=cf.PRIMARY_COLOR
        )
        self.label.grid(row=3, column=0)

        image = Image.open(os.path.join(self.BASE, 'frames', 'img', 'github.png'))
        image = image.resize((50, 50), Image.LANCZOS)
        self.github_logo = ImageTk.PhotoImage(image)


        self.github_button = Button(
            self.main_frame,
            text="By carlos8788",
            command=self.open_github,
            image=self.github_logo,
            borderwidth=0,
            relief='ridge',
            background=cf.PRIMARY_COLOR,
            cursor='hand2'
        )
        self.github_button.grid(row=2, column=0)

    def open_github(self):
        webbrowser.open_new_tab(
            "https://github.com/carlos8788")  # Abre el enlace de tu github en un nuevo tab del navegador por defecto


