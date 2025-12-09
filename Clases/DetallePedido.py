class DetallePedido:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        self.subtotal = producto.precio * cantidad
        self.rentabilidad = producto.rentabilidad * cantidad
        self.tiempo_total = producto.tiempo_preparacion * cantidad

    def __repr__(self):
        return f"{self.producto.nombre} x{self.cantidad}"
