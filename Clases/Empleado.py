class Empleado:
    def __init__(self, id, nombre, rol, usuario=None, password=None):
        self.id = id
        self.nombre = nombre
        self.rol = rol
        self.usuario = usuario
        self.password = password

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Empleado(id={self.id}, nombre='{self.nombre}', rol='{self.rol}')"
