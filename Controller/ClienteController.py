from Repository.ClienteRepository import ClientesRepository
from Clases.Cliente import Cliente
from Utils.Validador import Validador


class ClientesController:
    def __init__(self):
        self.repo = ClientesRepository()

    def crear(self, dni, telefono=None, direccion=None):
        if not Validador.dni(dni):
            return "DNI inválido. Debe contener 8 dígitos"
        if type(self.repo.buscar_dni(dni)) == Cliente:
            return "Error, el ya hay un cliente registrado con ese DNI"
        if (telefono and not direccion) or (direccion and not telefono):
            return "Para delivery debe proporcionar tanto teléfono como dirección"

        if telefono and not Validador.telefono(telefono):
            return "Teléfono inválido. Debe contener 7-15 dígitos"
        if direccion and not Validador.direccion(direccion):
            return "Dirección inválida. Debe contener entre 5 y 200 caracteres"

        cliente = Cliente(0, dni.strip(), telefono.strip() if telefono else None,
                          direccion.strip() if direccion else None)
        return self.repo.agregar(cliente)


    def obtener_todos(self):
        return self.repo.listar_todos()

    def actualizar(self, id, dni=None, telefono=None, direccion=None):
        try:
            id = int(id)
        except ValueError:
            return "El id no tiene un formato correcto"

        if dni and not Validador.dni(dni):
            return "DNI inválido. Debe contener 8 dígitos"
        if telefono and not Validador.telefono(telefono):
            return "Teléfono inválido. Debe contener 7-15 dígitos"
        if direccion and not Validador.direccion(direccion):
            return "Dirección inválida. Debe contener entre 5 y 200 caracteres"

        cliente = Cliente(id, dni, telefono, direccion)
        resultado = self.repo.actualizar(id, cliente)

        if not resultado:
            return f"No se encontró el registro con el id: {id}"
        return True

    def eliminar(self, id):
        try:
            id = int(id)
        except ValueError:
            return "El id no tiene un formato correcto"
        if not self.repo.borrar(id):
            return f"No se encontró el registro con el id: {id}"
        return True

    def buscar_id(self, id):
        try:
            id = int(id)
        except ValueError:
            return "El id no tiene un formato correcto"
        resultado = self.repo.buscar_id(id)
        if not resultado:
            return f"No se encontró el registro con el id: {id}"
        return resultado
    def buscar_dni(self,dni):
        if not Validador.dni(dni):
            return "DNI inválido. Debe contener 8 dígitos"
        resultado = self.repo.buscar_dni(dni)
        if not resultado:
            return f"No se encontró el registro con el DNI: {dni}"
        return resultado