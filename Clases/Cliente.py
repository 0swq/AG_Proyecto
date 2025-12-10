class Cliente:
    def __init__(self, id, dni, telefono=None, direccion=None):
        self.id = id
        self.dni = dni
        self.telefono = telefono
        self.direccion = direccion

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        componentes = [
            f"ID: {self.id}",
            f"DNI: {self.dni}"]
        if self.telefono:
            componentes.append(f"Teléfono: {self.telefono}")
        if self.direccion:
            componentes.append(f"Dirección: {self.direccion}")
        return " ➜ ".join(componentes)