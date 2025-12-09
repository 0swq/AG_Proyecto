from Repository.ClienteRepository import ClientesRepository
from Clases.Cliente import Cliente
from Utils.Validador import Validador


class ClientesController:
    def __init__(self):
        self.repo = ClientesRepository()

    def crear(self, nombre, telefono):
        if not Validador.nombre(nombre):
            return "Nombre inválido. Debe contener solo letras y espacios (2-50 caracteres)"
        if not Validador.telefono(telefono):
            return "Teléfono inválido. Debe contener 7-15 dígitos"

        cliente = Cliente(0, nombre.strip(), telefono.strip())
        return self.repo.agregar(cliente)

    def obtener_todos(self):
        return self.repo.listar_todos()

    def actualizar(self, id, nombre=None, telefono=None):
        try:
            id = int(id)
        except ValueError:
            return f"El id no tiene un formato incorrecto"
        if nombre and not Validador.nombre(nombre):
            return "Nombre inválido. Debe contener solo letras y espacios (2-50 caracteres)"
        if telefono and not Validador.telefono(telefono):
            return "Teléfono inválido. Debe contener 7-15 dígitos"

        cliente = Cliente(id, nombre, telefono)
        resultado = self.repo.actualizar(id, cliente)

        if not resultado:
            return f"No se encontró el registro con el id: {id}"
        return True

    def eliminar(self, id):
        try:
            id = int(id)
        except ValueError:
            return f"El id no tiene un formato incorrecto"
        if not self.repo.borrar(id):
            return f"No se encontro el registro con el id: {id}"
        return True

    def buscar_id(self, id):
        try:
            id = int(id)
        except ValueError:
            return f"El id no tiene un formato incorrecto"
        resultado = self.repo.buscar_id(id)
        if not resultado:
            return f"No se encontro el registro con el id: {id}"
        return resultado
