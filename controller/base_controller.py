from abc import abstractmethod

from DAO.data import Data


class BaseController:
    def __init__(self, path):
        self.data = Data(path)
        self.items = self.data.load_from_json()

    @abstractmethod
    def crear_item(self):
        pass
    def ver_items(self):
        return self.items

    def ver_items_id(self, id):
        for item in self.items:
            if item['id'] == id:
                return item
        return None

    def eliminar_item_id(self, id):
        for item in self.items:
            if item['id'] == id:
                self.items.remove(item)
                self.data.save_to_json(self.items)
                break