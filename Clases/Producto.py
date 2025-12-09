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
        return (f"Producto(id={self.id}, nombre='{self.nombre}', categoria='{self.categoria}', "
                f"precio={self.precio}, costo={self.costo}, prep={self.tiempo_preparacion}min, "
                f"rent={self.rentabilidad})")