from Repository.BoletaRepository import BoletaRepository
from Clases.Comprobante import Boleta


class BoletaController:
    def __init__(self):
        self.repo = BoletaRepository()

    def crear(self, pago, prefijo="BOL"):
        if not pago:
            raise ValueError("Debe proporcionar un pago válido")

        boleta = Boleta(0, pago)
        return self.repo.agregar(boleta, prefijo)

    def obtener_todos(self):
        return self.repo.listar_todos()

    def actualizar(self, id, pago):
        if not pago:
            raise ValueError("Debe proporcionar un pago válido")

        boleta = Boleta(id, pago)
        return self.repo.actualizar(id, boleta)

    def eliminar(self, id):
        if not id or id <= 0:
            raise ValueError("ID inválido")
        return self.repo.borrar(id)

    def buscar_id(self, id):
        try:
            id = int(id)
        except ValueError:
            return f"El id no tiene un formato incorrecto"
        resultado = self.repo.buscar_id(id)
        if not resultado:
            return f"No se encontro el registro con el id: {id}"
        return resultado