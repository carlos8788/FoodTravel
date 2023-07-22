import tkintermapview

class TkinterMapView:
    def __init__(self, frame, object_tk):
        self.map_widget = tkintermapview.TkinterMapView(frame, width=1200, height=600, corner_radius=20)
        self.map_widget.place(relx=0.5, rely=0.5, anchor=object_tk.CENTER)
        self.map_widget.set_position(-24.790245, -65.4021057)
        self.map_widget.set_zoom(13)

