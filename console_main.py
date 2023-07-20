from controller.ubicacion_controller import UbicacionController
from controller.destino_culinario_controller import DestinoCulinarioController
from view.tkinter_view import MainWindow
from view.ubicacion_view import UbicacionView
from view.destino_culinario_view import DestinoCulinarioView

class MainApp:
    def __init__(self):
        self.ubicacion_controller = UbicacionController('DAO/JSON/ubicaciones.json')
        self.destino_culinario_controller = DestinoCulinarioController('DAO/JSON/destinos_culinarios.json')
        self.ubicacion_view = UbicacionView(self.ubicacion_controller)
        self.destino_culinario_view = DestinoCulinarioView(self.destino_culinario_controller)

    def run(self):
        self.destino_culinario_view.crear_destino_culinario()
        self.ubicacion_view.crear_ubicacion()

        self.ubicacion_view.ver_ubicaciones()
        self.destino_culinario_view.ver_destinos_culinarios()
        print("\n================================")
        print("\n================================")
        self.ubicacion_view.ver_ubicacion_id()
        self.destino_culinario_view.ver_destino_culinario_id()



if __name__ == "__main__":
    app = MainApp()
    app.run()
