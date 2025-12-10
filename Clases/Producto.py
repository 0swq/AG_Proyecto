class Producto:
    def __init__(self, id, nombre, categoria, precio, costo=0, tiempo_preparacion=5):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.costo = costo
        self.tiempo_preparacion = tiempo_preparacion
        self.rentabilidad = (self.precio - self.costo) if (self.costo is not None and self.precio is not None) else None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        componentes = [
            f"ID: {self.id}",
            f"Nombre: {self.nombre}",
            f"Categoría: {self.categoria}",
            f"Precio: {self.precio:.2f}",
            f"Costo: {self.costo:.2f}",
            f"Preparación: {self.tiempo_preparacion}min",
            f"Rentabilidad: {self.rentabilidad:.2f}"
            if self.rentabilidad is not None else "Rentabilidad: N/A"
        ]

        return " ➜ ".join(componentes)