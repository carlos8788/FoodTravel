import tkintermapview
from tkinter import CENTER
class TkinterMapView:
    def __init__(self, frame):
        self.map_widget = tkintermapview.TkinterMapView(frame, width=1200, height=900, corner_radius=20)
        self.map_widget.grid(row=0, column=0)  # Put in the grid in the desired row and column
        self.map_widget.set_position(-24.790245, -65.4021057)
        self.map_widget.set_zoom(13)


