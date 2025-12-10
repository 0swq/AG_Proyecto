from collections import deque
from Clases.Producto import Producto
import Global.Global as Global
from Estructuras.Arboles import construir_arbol, buscar


class ProductosRepository:
    historial_recientes = deque(maxlen=10)

    @property
    def productos(self):
        return Global.productos

    def agregar(self, producto: Producto):
        Global.ultimo_id_producto += 1
        producto.id = Global.ultimo_id_producto
        self.productos.append(producto)
        self.historial_recientes.append(producto)
        return producto

    def listar_todos(self):
        return self.productos

    def buscar_id(self, id):
        Global.raiz_productos = construir_arbol(Global.productos, 'id')
        return buscar(Global.raiz_productos, id, 'id')

    def actualizar(self, id, producto_nuevo: Producto):
        producto = next((p for p in self.productos if p.id == id), None)
        if not producto:
            return False
        for attr, valor in vars(producto_nuevo).items():
            if attr != 'id' and attr in vars(producto) and valor is not None:
                setattr(producto, attr, valor)
        producto.rentabilidad = producto.precio - producto.costo
        return True

    def borrar(self, id):
        producto = next((p for p in self.productos if p.id == id), None)
        if producto:
            self.productos.remove(producto)
            if producto in self.historial_recientes:
                self.historial_recientes.remove(producto)
            return True
        return False