
from Repository.DetallePedidoRepository import DetallePedidoRepository
from Clases.DetallePedido import DetallePedido


class DetallePedidoController:
    def __init__(self):
        self.repo = DetallePedidoRepository()

    def crear(self, producto, cantidad):
        if not producto:
            return "Debe proporcionar un producto válido"

        try:
            cantidad = int(cantidad)
            if cantidad <= 0:
                return "La cantidad debe ser mayor a 0"
        except ValueError:
            return "La cantidad debe ser un número válido"

        detalle = DetallePedido(producto, cantidad)
        return self.repo.agregar(detalle)

    def actualizar(self, producto, cantidad,detalle_actual: DetallePedido):
        if not producto:
            return "Debe proporcionar un producto válido"

        try:
            cantidad = int(cantidad)
            if cantidad <= 0:
                return "La cantidad debe ser mayor a 0"
        except ValueError:
            return "La cantidad debe ser un número válido"

        detalle_nuevo = DetallePedido(producto, cantidad)
        resultado = self.repo.actualizar(detalle_nuevo,detalle_actual)

        return resultado