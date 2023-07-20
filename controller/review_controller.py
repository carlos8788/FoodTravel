from controller.base_controller import BaseController
from model.review import Review


class ReviewController(BaseController):

    def _guardar_item(self,id_destino, id_usuario, calificacion, comentario, animo):
        self.review = Review(self.id_item(), id_destino, id_usuario, calificacion, comentario, animo)
        self.items.append(self.review.to_dict())
        self.data.save_to_json(self.items)
        return self.items