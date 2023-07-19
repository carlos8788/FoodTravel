from DAO.data import Data
from model.destino_culinario import DestinoCulinario


class DestinoCulinarioController:
    def __init__(self,path):
        self.data = Data(path)
        self.destinos_culinarios = self.data.load_from_json()

    def crear_destino_culinario(
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

        self.destinos_culinarios.append(destino_culinario.to_dict())
        self.data.save_from_json(self.destinos_culinarios)
        return self.destinos_culinarios

    def ver_destinos_culinarios(self):
        return self.destinos_culinarios

    def ver_destino_culinario_id(self, id):
        #return next((destino for destino in self.destinos_culinarios if destino['id'] == id), None)
        for destino in self.destinos_culinarios:
            if destino['id'] == id:
                return destino
        return None

    def eliminar_destino_culinario(self, id):
        for destino in self.destinos_culinarios:
            if destino['id'] == id:
                self.destinos_culinarios.remove(destino)
                self.data.save_to_json(self.destinos_culinarios)
                break



if __name__ == '__main__':
    destinos_culinarios = [
        {
            "id": 1,
            "nombre": "La Cocina de Luigi",
            "tipo_cocina": "Italiana",
            "ingredientes": ["Pasta", "Tomate", "Aceite de Oliva", "Queso Parmesano"],
            "precio_minimo": 10.0,
            "precio_maximo": 20.0,
            "popularidad": 4.5,
            "disponibilidad": True,
            "id_ubicacion": "1",
            "imagen": "url_imagen_1"
        },
        {
            "id": 2,
            "nombre": "Sakura Sushi",
            "tipo_cocina": "Japonesa",
            "ingredientes": ["Arroz", "Pescado", "Algas", "Soja"],
            "precio_minimo": 15.0,
            "precio_maximo": 30.0,
            "popularidad": 4.7,
            "disponibilidad": True,
            "id_ubicacion": "2",
            "imagen": "url_imagen_2"
        },
        {
            "id": 3,
            "nombre": "El Asador Criollo",
            "tipo_cocina": "Argentina",
            "ingredientes": ["Carne de Res", "Chorizo", "Mollejas", "Vino Malbec"],
            "precio_minimo": 20.0,
            "precio_maximo": 40.0,
            "popularidad": 4.6,
            "disponibilidad": False,
            "id_ubicacion": "3",
            "imagen": "url_imagen_3"
        },
        {
            "id": 4,
            "nombre": "Le Petite Boulangerie",
            "tipo_cocina": "Francesa",
            "ingredientes": ["Harina", "Huevos", "Mantequilla", "Chocolate"],
            "precio_minimo": 5.0,
            "precio_maximo": 15.0,
            "popularidad": 4.4,
            "disponibilidad": True,
            "id_ubicacion": "4",
            "imagen": "url_imagen_4"
        }
    ]

    id = 1
    for destino in destinos_culinarios:
        if destino['id'] == id:
            destinos_culinarios.remove(destino)
    print(destinos_culinarios)
