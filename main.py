from controller.ubicacion_controller import UbicacionController
from controller.destino_culinario_controller import DestinoCulinarioController
from view.destino_culinario_view import DestinoCulinarioView
from view.tkinter_view import MainWindow
from view.ubicacion_view import UbicacionView


class Main():
    def __init__(self):
        self.ubicacion_controller = UbicacionController('DAO/JSON/ubicaciones.json')
        self.destino_culinario_controller = DestinoCulinarioController('DAO/JSON/destinos_culinarios.json')
        self.ubicacion_view = UbicacionView(self.ubicacion_controller)
        self.destino_culinario_view = DestinoCulinarioView(self.destino_culinario_controller)
        MainWindow(self.ubicacion_view, self.destino_culinario_view)

if __name__ == "__main__":
    Main()
