from pathlib import Path
import os
from tkinter import Toplevel, Label
from PIL import Image, ImageTk
import requests
from io import BytesIO

class PopupImage:
    def __init__(self, root, img):
        # self.img =
        self.dialog = None
        self.root = root
        self.BASE = Path(__file__).resolve().parent
        if img[0:5] == 'https':
            self.img = img
        else:
            self.img = os.path.join(self.BASE, 'components', 'frames', img)
        self.get_dialog()
    def get_dialog(self, event=None):
        if self.dialog is not None:
            return

        self.dialog = Toplevel()
        self.dialog.protocol("WM_DELETE_WINDOW", self.on_dialog_close)

        # image = Image.open(self.img)

        if self.img.startswith('https'):
            response = requests.get(self.img)
            image = Image.open(BytesIO(response.content))
        else:
            image = Image.open(self.img)

        photo = ImageTk.PhotoImage(image)

        photo = ImageTk.PhotoImage(image)

        background_label = Label(self.dialog, image=photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.dialog.geometry("400x400")
        x, y = self.root.winfo_pointerxy()
        self.dialog.geometry("+%d+%d" % (x, y))

        self.dialog.mainloop()

    def on_dialog_close(self):

        self.dialog.destroy()
        self.dialog = None