from Repository.ProductoRepository import ProductosRepository
from Clases.Producto import Producto
from Utils.Validador import Validador


class ProductosController:
    def __init__(self):
        self.repo = ProductosRepository()

    def crear(self, nombre, categoria, precio, costo=0, tiempo_preparacion=5):
        if not Validador.nombre_producto(nombre):
            return "Nombre inválido. Debe contener entre 2 y 100 caracteres"
        if not Validador.categoria(categoria):
            return "Categoría inválida. Debe ser: entrada, plato_principal, postre o bebida"
        if not Validador.precio(precio):
            return "Precio inválido. Debe ser un número mayor a 0"
        if not Validador.precio(costo):
            return "Costo inválido. Debe ser un número mayor a 0"
        if not Validador.tiempo_preparacion(tiempo_preparacion):
            return "Tiempo de preparación inválido. Debe ser un número entre 1 y 180 minutos"

        producto = Producto(0, nombre.strip(), categoria.strip().lower(),
                            float(precio), float(costo), int(tiempo_preparacion))
        return self.repo.agregar(producto)

    def obtener_todos(self):
        return self.repo.listar_todos()

    def actualizar(self, id, nombre=None, categoria=None, precio=None, costo=None, tiempo_preparacion=None):
        try:
            id = int(id)
        except ValueError:
            return f"El id no tiene un formato correcto"

        if nombre and not Validador.nombre_producto(nombre):
            return "Nombre inválido. Debe contener entre 2 y 100 caracteres"
        if categoria and not Validador.categoria(categoria):
            return "Categoría inválida. Debe ser: entrada, plato_principal, postre o bebida"
        if precio and not Validador.precio(precio):
            return "Precio inválido. Debe ser un número mayor a 0"
        if costo and not Validador.precio(costo):
            return "Costo inválido. Debe ser un número mayor a 0"
        if tiempo_preparacion and not Validador.tiempo_preparacion(tiempo_preparacion):
            return "Tiempo de preparación inválido. Debe ser un número entre 1 y 180 minutos"

        producto = Producto(
            id,
            nombre.strip() if nombre else None,
            categoria.strip().lower() if categoria else None,
            float(precio) if precio else None,
            float(costo) if costo else None,
            int(tiempo_preparacion) if tiempo_preparacion else None
        )
        resultado = self.repo.actualizar(id, producto)

        if not resultado:
            return f"No se encontró el registro con el id: {id}"
        return True

    def eliminar(self, id):
        try:
            id = int(id)
        except ValueError:
            return f"El id no tiene un formato correcto"
        if not self.repo.borrar(id):
            return f"No se encontró el registro con el id: {id}"
        return True

    def buscar_id(self, id):
        try:
            id = int(id)
        except ValueError:
            return f"El id no tiene un formato correcto"
        resultado = self.repo.buscar_id(id)
        if not resultado:
            return f"No se encontró el registro con el id: {id}"
        return resultado