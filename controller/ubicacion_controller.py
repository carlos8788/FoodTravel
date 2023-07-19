from DAO.data import Data
from controller.base_controller import BaseController
from model import ubicacion
from model.ubicacion import Ubicacion

class UbicacionController(BaseController):
    def crear_item( self, id_ubicacion, direccion, coordenadas):
        self.ubicacion = Ubicacion(id_ubicacion, direccion, coordenadas)

        self.items.append(self.ubicacion.to_dict())
        self.data.save_to_json(self.items)
        return self.items

if __name__ == '__main__':
    ubicacion = UbicacionController('ub.json')
    ubicacion.crear_item(4,'sasd', [1, 2])
    print(ubicacion.ver_items())