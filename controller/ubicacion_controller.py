from DAO.data import Data
from model.ubicacion import Ubicacion

class UbicacionController:
    def __init__(self, path):
        self.data = Data(path)
        self.ubicaciones = self.data.load_from_json()

    def crear_ubicacion( self, id_ubicacion, direccion, coordenadas):
        self.ubicacion =  Ubicacion(id_ubicacion, direccion, coordenadas)

        self.ubicaciones.append(self.ubicacion.to_dict())
        self.data.save_from_json(self.ubicaciones)
        return self.ubicaciones

    def ver_ubicacion(self):
        return self.ubicaciones

    def ver_ubicacion_id(self, id):
        for ubicacion in self.ubicaciones:
            if ubicacion['id'] == id:
                return ubicacion
        return None

    def eliminar_ubicacion(self, id):
        for ubicacion in self.ubicaciones:
            if ubicacion['id'] == id:
                self.ubicaciones.remove(ubicacion)
                self.data.save_to_json(self.ubicaciones)
                break