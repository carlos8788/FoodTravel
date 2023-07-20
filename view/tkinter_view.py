import tkinter as tk

class MainWindow:
    def __init__(self, ubicacion_view, destino_view):

        self.ubicacion_view = ubicacion_view
        self.destino_view = destino_view
        self.root = tk.Tk()
        self.root.title("Aplicación de Destinos Culinarios")
        self.root.geometry("1600x800")
        self.root.resizable(False, False)

        self.style_font = 'Arial 16'

        self.btn_abrir_formulario_ubicacion = tk.Button(
            self.root,
            text="Abrir Formulario Ubicacion",
            font=self.style_font,
            command=lambda: self.ubicacion_view.crear_ubicacion()
        )
        self.btn_abrir_formulario_ubicacion.grid(row=0, column=0, pady=10)

        self.btn_abrir_formulario_destino = tk.Button(
            self.root,
            text="Abrir Formulario Destino",
            font=self.style_font,
            command=lambda: self.destino_view.crear_destino_culinario()
        )
        self.btn_abrir_formulario_destino.grid(row=1, column=0, pady=10)

        self.btn_mostrar_ubicaciones = tk.Button(
            self.root,
            text="Mostrar Ubicaciones",
            font=self.style_font,
            command=lambda: self.ubicacion_view.ver_ubicaciones()
        )
        self.btn_mostrar_ubicaciones.grid(row=2, column=0, pady=10)

        self.btn_mostrar_destinos = tk.Button(
            self.root,
            text="Mostrar Destinos",
            font=self.style_font,
            command=lambda: self.destino_view.ver_destinos_culinarios()
        )
        self.btn_mostrar_destinos.grid(row=3, column=0, pady=10)

        self.btn_mostrar_todos = tk.Button(
            self.root,
            text="Mostrar Todos",
            font=self.style_font,
            command=lambda: self.mostrar_todos(),
            background='red',
            fg='white'
        )
        self.btn_mostrar_todos.grid(row=4, column=0, pady=10)

        self.root.mainloop()

    def mostrar_todos(self):
        self.destino_view.ver_destinos_culinarios()
        self.ubicacion_view.ver_ubicaciones()


if __name__ == "__main__":
    app = MainWindow()
