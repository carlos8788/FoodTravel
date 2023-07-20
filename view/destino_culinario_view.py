class DestinoCulinarioView:
    def __init__(self, controller):
        self.controller = controller

    def crear_destino_culinario(self):
        id = int(input('Ingrese el ID del destino culinario: '))
        nombre = input('Ingrese el nombre del destino culinario: ')
        tipo_cocina = input('Ingrese el tipo de cocina: ')
        ingredientes = input('Ingrese los ingredientes (separados por comas): ').split(',')
        precio_minimo = float(input('Ingrese el precio mínimo: '))
        precio_maximo = float(input('Ingrese el precio máximo: '))
        popularidad = input('Ingrese la popularidad: ')
        disponibilidad = bool(input('Ingrese la disponibilidad (True/False): '))
        id_ubicacion = int(input('Ingrese el ID de ubicación: '))
        imagen = input('Ingrese la URL de la imagen: ')

        self.controller.crear_item(id, nombre, tipo_cocina, ingredientes)
        print(f'Destino culinario creado con éxito.')

    def ver_destinos_culinarios(self):
        destinos_culinarios = self.controller.ver_items()
        for destino in destinos_culinarios:
            print(f"ID: {destino['id']}, Nombre: {destino['nombre']}, Tipo de cocina: {destino['tipo_cocina']}")

    def ver_destino_culinario_id(self):
        id_destino = int(input('Ingrese el ID del destino culinario que desea ver: '))
        destino = self.controller.ver_items_id(id_destino)
        if destino:
            print(f"ID: {destino['id']}, Nombre: {destino['nombre']}, Tipo de cocina: {destino['tipo_cocina']}")
        else:
            print('El destino culinario con el ID proporcionado no existe.')

    def eliminar_destino_culinario(self):
        id_destino = int(input('Ingrese el ID del destino culinario que desea eliminar: '))
        self.controller.eliminar_item_id(id_destino)
        print('Destino culinario eliminado con éxito.')
