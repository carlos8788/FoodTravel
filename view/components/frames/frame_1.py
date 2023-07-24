from tkinter import Frame, Button, PhotoImage, Toplevel, Label
import tkintermapview
from PIL import ImageTk, Image
from pathlib import Path
import os

import view.config as cf

class Frame1:
        def __init__(
                self,
                frame_root,
                _config_frame_body,
                ubicacion_view
        ) -> None:

            self.ubicacion_view = ubicacion_view
            self.frame_root = frame_root
            self._config_frame_body = _config_frame_body
            self.toplevel = PopupImage(self.frame_root)


            self.frame1 = Frame(
                self.frame_root,
                width=800,
                height=500,
                background=cf.PRIMARY_COLOR
            )
            self._config_frame_body(self.frame1)

            self.map_widget = tkintermapview.TkinterMapView(
                self.frame1,
                width=1200,
                height=900,
                corner_radius=20
            )
            #### MAPA
            img = PhotoImage('im.png')
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
            # self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga",
            #                                 max_zoom=22)
            self.map_widget.grid(row=0, column=0)
            self.map_widget.set_position(-24.790245, -65.4021057)
            self.map_widget.set_zoom(13)

            marker = self.map_widget.set_marker(-24.790245, -65.4021057, image=img, command=lambda x: self.toplevel.get_dialog())
            marker.hide_image(True)
            # print(marker)
            ####

            footer1 = Frame(self.frame1, background=cf.PRIMARY_COLOR)
            footer1.grid(row=1, column=0)

            self.button1 = Button(
                footer1,
                text="Mostrar Ubicaciones",
                background=cf.THIRD_COLOR,
                font=cf.SECONDARY_FONT,
                foreground=cf.SECONDARY_COLOR,
                borderwidth=0,
                relief='ridge',
                width=16,
                command=lambda: self.ubicacion_view.ver_ubicaciones(self.map_widget)
            )

            self.button1.bind("<Enter>", self._change_to_red)
            self.button1.bind("<Leave>", self._change_to_original)

            self.button1.grid(row=0, column=0, padx=(18, 20), pady=50)

            self.button2 = Button(
                footer1,
                text="Mostrar lista de UB",
                background=cf.THIRD_COLOR,
                font=cf.SECONDARY_FONT,
                foreground=cf.SECONDARY_COLOR,
                borderwidth=0,
                relief='ridge',
                width=16
            )
            self.button2.bind("<Enter>", self._change_to_red)
            self.button2.bind("<Leave>", self._change_to_original)

            self.button2.grid(row=0, column=1, padx=(20, 20))

            self.button3 = Button(
                footer1,
                text="Limpiar mapa",
                background=cf.THIRD_COLOR,
                font=cf.SECONDARY_FONT,
                foreground=cf.SECONDARY_COLOR,
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
            event.widget['background'] = cf.THIRD_COLOR



        # Manejar el evento de clic en el marcador

        def on_marker_click(self):
            print("Se hizo clic en el marcador")

        def get_frame(self):
            return self.frame1


class PopupImage:
    def __init__(self, root):
        self.dialog = None
        self.root = root
        self.BASE = Path(__file__).resolve().parent


    def get_dialog(self, event=None):
        if self.dialog is not None:
            return

        self.dialog = Toplevel()
        self.dialog.protocol("WM_DELETE_WINDOW", self.on_dialog_close)

        # Cargar la imagen
        img = os.path.join(self.BASE, 'img\salta.png')
        image = Image.open(img)

        photo = ImageTk.PhotoImage(image)

        # Crear un Label con la imagen de fondo
        background_label = Label(self.dialog, image=photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.dialog.geometry("400x400")
        x, y = self.root.winfo_pointerxy()
        self.dialog.geometry("+%d+%d" % (x, y))


        self.dialog.mainloop()

    def on_dialog_close(self):
        # The dialog is being closed, so we set self.dialog back to None
        self.dialog.destroy()
        self.dialog = None
