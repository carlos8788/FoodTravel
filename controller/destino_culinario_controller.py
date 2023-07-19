from DAO.data import Data
from controller.base_controller import BaseController
from model.destino_culinario import DestinoCulinario


class DestinoCulinarioController(BaseController):

    def crear_item(
            self,
            id,
            nombre,
            tipo_cocina,
            ingredientes,
            precio_minimo,
            precio_maximo,
            popularidad,
            disponibilidad,
            id_ubicacion,
            imagen):
        destino_culinario =  DestinoCulinario(
                id,
                nombre,
                tipo_cocina,
                ingredientes,
                precio_minimo,
                precio_maximo,
                popularidad,
                disponibilidad,
                id_ubicacion,
                imagen)

        self.items.append(destino_culinario.to_dict())
        self.data.save_to_json(self.items)
        return self.items





if __name__ == '__main__':
    pass
