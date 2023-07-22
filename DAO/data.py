import json

class Data:
    def __init__(self, path):
        self.path = path

    def save_to_json(self, data=[]):
        try:
            with open(self.path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except FileNotFoundError as e:
            print(e)

    def load_from_json(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data
        except FileNotFoundError as e:
            self.save_to_json()

if __name__ == '__main__':
    data1 = Data('JSON/ubicaciones.json')
    data2 = Data('JSON/destinos_culinarios.json')

    datos = data2.load_from_json()
    print(datos)
    # data2.save_to_json(datos)

    nuevo_destino = {'direccion': 123, 'destinos': 1}
    datos.append(nuevo_destino)
    data2.save_to_json(datos)