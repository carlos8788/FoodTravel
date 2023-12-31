
from controller.base_controller import BaseController
from model.ubicacion import Ubicacion

class UbicacionController(BaseController):
    def _guardar_item( self, direccion, coordenadas):
        self.ubicacion = Ubicacion(self.id_item(), direccion, coordenadas)
        self.items.append(self.ubicacion.to_dict())
        self.data.save_to_json(self.items)
        return self.items

