class DetallePedido:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        self.subtotal = producto.precio * cantidad
        self.rentabilidad = producto.rentabilidad * cantidad
        self.tiempo_total = producto.tiempo_preparacion * cantidad

    def __str__(self):
        componentes = [
            f"Producto: {self.producto.nombre}",
            f"Cantidad: {self.cantidad}",
            f"Subtotal: {self.subtotal:.2f}",
            f"Rentabilidad: {self.rentabilidad:.2f}",
            f"Tiempo Total: {self.tiempo_total} min"
        ]
        return " ➜ ".join(componentes)