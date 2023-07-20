from controller.base_controller import BaseController
from model.actividad import Actividad


class ActividadController(BaseController):

    def _guardar_item(self, nombre, destino_id, hora_inicio):
        self.actividad = Actividad(self.id_item(), nombre, destino_id, hora_inicio)

        self.items.append(self.actividad.to_dict())
        self.data.save_to_json(self.items)
        return self.items

if __name__ == '__main__':
    actividad = ActividadController('actividad.json')
    print(actividad.ver_items())