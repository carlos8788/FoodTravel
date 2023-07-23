from controller.ubicacion_controller import UbicacionController
from controller.destino_culinario_controller import DestinoCulinarioController
from view.destino_culinario_view import DestinoCulinarioView
from view.tkinter_view import MainWindow
from view.ubicacion_view import UbicacionView
from pathlib import Path
import os

class Main():
    def __init__(self):
        self.BASE_DIR = Path(__file__).resolve().parent
        self.dir_destinos_culinarios = os.path.join(self.BASE_DIR, 'DAO/JSON/ubicaciones.json')
        self.dir_ubicaiones = os.path.join(self.BASE_DIR, 'DAO/JSON/destinos_culinarios.json')

        self.ubicacion_controller = UbicacionController(self.dir_destinos_culinarios)
        self.destino_culinario_controller = DestinoCulinarioController(self.dir_ubicaiones)
        self.ubicacion_view = UbicacionView(self.ubicacion_controller)
        self.destino_culinario_view = DestinoCulinarioView(self.destino_culinario_controller)
        MainWindow(self.ubicacion_view, self.destino_culinario_view)

if __name__ == "__main__":
    Main()
