from controller.base_controller import BaseController
from model.usuario import Usuario

class UsuarioController(BaseController):
    def _guardar_item( self, nombre, apellido, historial_rutas):
        self.usuario = Usuario(self.id_item(), nombre, apellido, historial_rutas)

        self.items.append(self.usuario.to_dict())
        self.data.save_to_json(self.items)
        return self.items