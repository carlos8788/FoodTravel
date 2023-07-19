from controller.ubicacion_controller import UbicacionController


class UbicacionView:
    def __init__(self, controller):
        self.controller = controller

    def crear_ubicacion(self):
        id_ubicacion = input('Ingrese el ID de la ubicación: ')
        direccion = input('Ingrese la dirección: ')
        coordenadas = input('Ingrese las coordenadas (en formato "lat,long"): ').split(',')

        self.controller.crear_item(id_ubicacion, direccion, coordenadas)
        print(f'Ubicación creada con éxito.')

    def ver_ubicaciones(self):
        ubicaciones = self.controller.ver_items()
        for ubicacion in ubicaciones:
            print(
                f"ID: {ubicacion['id']}, Dirección: {ubicacion['direccion']}, Coordenadas: {ubicacion['coordenadas']}")

    def ver_ubicacion_id(self):
        id_ubicacion = int(input('Ingrese el ID de la ubicación que desea ver: '))
        ubicacion = self.controller.ver_items_id(id_ubicacion)
        if ubicacion:
            print(
                f"ID: {ubicacion['id']}, Dirección: {ubicacion['direccion']}, Coordenadas: {ubicacion['coordenadas']}")
        else:
            print('La ubicación con el ID proporcionado no existe.')

    def eliminar_ubicacion(self):
        id_ubicacion = input('Ingrese el ID de la ubicación que desea eliminar: ')
        self.controller.eliminar_item_id(id_ubicacion)
        print('Ubicación eliminada con éxito.')

if __name__ == '__main__':
    ubicacion = UbicacionController('../DAO/JSON/ubicaciones.json')
    print(ubicacion.ver_items())
    ubicacion_view = UbicacionView(ubicacion)
    ubicacion_view.ver_ubicacion_id()