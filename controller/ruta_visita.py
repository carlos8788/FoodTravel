from controller.base_controller import BaseController
from model.ruta_visita import RutaVisita


class RutaVisitaController(BaseController):

    def _guardar_item(self, nombre, destinos):
        self.ruta = RutaVisita(self.id_item(), nombre, destinos)
        self.items.append(self.ruta.to_dict())
        self.data.save_to_json(self.items)
        return self.items