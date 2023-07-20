from abc import abstractmethod

from DAO.data import Data


class BaseController:
    def __init__(self, path):
        self.data = Data(path)
        self.items = self.data.load_from_json()


    def crear_item(self, *args):
        self.check_item_empty_attributes(args)
        self.guardar_item(*args)

    @abstractmethod
    def _guardar_item(self):
        pass
    def ver_items(self):
        return self.items

    def ver_items_id(self, id):
        return next((item for item in self.items if item['id'] == id), None)

    def eliminar_item_id(self, id):
        for item in self.items:
            if item['id'] == id:
                self.items.remove(item)
                self.data.save_to_json(self.items)
                break
        return None

    def actualizar_item(self, id, new_item):
        for i, item in enumerate(self.items):
            if item['id'] == id:
                self.items[i] = new_item
                self.data.save_to_json(self.items)
                break

    def id_item(self):
        return self.items[-1]['id'] + 1 if self.items else 1

    def check_item_empty_attributes(self):
        return all(value != "" and value is not None for value in item.values())

if __name__ == '__main__':
    item = BaseController('../DAO/JSON/ubicaciones.json')
    print(item.id_item())