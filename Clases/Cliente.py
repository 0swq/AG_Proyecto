class Cliente:
    def __init__(self, id, nombre, telefono):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Cliente(id={self.id}, nombre='{self.nombre}', telefono='{self.telefono}')"
