from tkinter import Frame, Button
import tkintermapview
import view.config as cf
from view.top_level import PopupImage


class Frame1:
        def __init__(
                self,
                frame_root,
                _config_frame_body,
                ubicacion_view,
                destino_view
        ) -> None:

            self.map_view = 0
            self.ubicacion_view = ubicacion_view
            self.destino_view = destino_view
            self.frame_root = frame_root
            self._config_frame_body = _config_frame_body
            # self.toplevel = PopupImage()

            self.frame1 = Frame(
                self.frame_root,
                width=800,
                height=500,
                background=cf.PRIMARY_COLOR
            )
            self._config_frame_body(self.frame1)

            # MAPA

            self.map_widget = tkintermapview.TkinterMapView(
                self.frame1,
                width=800,
                height=450,
                corner_radius=20
            )

            self.map_1 = "https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga"

            self.map_2 = "https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga"

            self.maps = (self.map_2, self.map_1)

            self.map_widget.grid(row=0, column=0)
            self.map_widget.set_position(-24.790245, -65.4021057)
            self.map_widget.set_zoom(13)
            self.change_map()
            self.map_widget.set_marker(-24.790245, -65.4021057, command=lambda x: PopupImage(self.frame_root,'img\salta.png'))
            self.ubicacion_view.ver_ubicaciones(self.frame_root, self.map_widget, self.destino_view)

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
                command=lambda: self.ubicacion_view.ver_ubicaciones(self.frame_root, self.map_widget, self.destino_view)
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
                width=16,
                command=self.change_map
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

        def _change_to_red(self, event):
            event.widget['background'] = '#191970'

        def _change_to_original(self, event):
            event.widget['background'] = cf.THIRD_COLOR

        def change_map(self):
            self.map_view = (self.map_view + 1) % 2
            return self.map_widget.set_tile_server(self.maps[self.map_view], max_zoom=22)

        def get_frame(self):
            return self.frame1




