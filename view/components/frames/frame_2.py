from tkinter import Frame, Button, Label, Canvas
from PIL import Image, ImageTk
from pathlib import Path
import os


class Frame2:
        def __init__(self, PRIMARY_COLOR, THIRD_COLOR, SECONDARY_FONT, SECONDARY_COLOR, frame_root, _config_frame_body) -> None:
            self.PRIMARY_COLOR = PRIMARY_COLOR
            self.THIRD_COLOR = THIRD_COLOR
            self.SECONDARY_COLOR = SECONDARY_COLOR
            self.SECONDARY_FONT = SECONDARY_FONT
            self.frame_root = frame_root
            self._config_frame_body = _config_frame_body
            self.frame2 = Frame(self.frame_root, width=800, height=500, background='red',)
            self._config_frame_body(self.frame2)
            footer1 = Frame(self.frame2, background=self.PRIMARY_COLOR)

            footer1.grid(row=1, column=0, columnspan=3, sticky='nsew')

            self.button1 = Button(
                footer1,
                text="A",
                background=self.THIRD_COLOR,
                font=self.SECONDARY_FONT,
                foreground=self.SECONDARY_COLOR,
                borderwidth=0,
                relief='ridge',
                width=16
            )
            self.button1.bind("<Enter>", self._change_to_red)
            self.button1.bind("<Leave>", self._change_to_original)

            self.button1.grid(row=0, column=0, padx=(65, 20), pady=50)

            self.button2 = Button(
                footer1,
                text="B",
                background=self.THIRD_COLOR,
                font=self.SECONDARY_FONT,
                foreground=self.SECONDARY_COLOR,
                borderwidth=0,
                relief='ridge',
                width=16
            )
            self.button2.bind("<Enter>", self._change_to_red)
            self.button2.bind("<Leave>", self._change_to_original)

            self.button2.grid(row=0, column=1, padx=(20, 20))

            self.button3 = Button(
                footer1,
                text="C",
                background=self.THIRD_COLOR,
                font=self.SECONDARY_FONT,
                foreground=self.SECONDARY_COLOR,
                borderwidth=0,
                relief='ridge',
                width=16
            )
            self.button3.bind("<Enter>", self._change_to_red)
            self.button3.bind("<Leave>", self._change_to_original)

            self.button3.grid(row=0, column=2, padx=(20, 20))
            #
            # self.button4 = Button(
            #     footer1,
            #     text="Footer1",
            #     background=self.THIRD_COLOR,
            #     font=self.SECONDARY_FONT,
            #     foreground=self.SECONDARY_COLOR,
            #     borderwidth=0,
            #     relief='ridge',
            # )
            # self.button4.bind("<Enter>", self._change_to_red)
            # self.button4.bind("<Leave>", self._change_to_original)
            #
            # self.button4.grid(row=0, column=3, padx=(50, 50))

        def _change_to_red(self, event):
            event.widget['background'] = '#191970'

        def _change_to_original(self, event):
            event.widget['background'] = self.THIRD_COLOR

        def get_frame(self):
            return self.frame2