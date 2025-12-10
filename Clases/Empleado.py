from Global import Global


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
        componentes = [
            f"ID: {self.id}",
            f"Nombre: {self.nombre}",
            f"Rol: {self.rol}"
        ]
        if self.usuario:
            componentes.append(f"Usuario: {self.usuario}")

        if Global.usuario_actual.rol=="admin":
            componentes.append(f"password: {"••••••••"}")

        return " ➜ ".join(componentes)