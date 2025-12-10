from copy import deepcopy
from Estructuras.Pilas import HistorialPila
from Global import Global
from Repository.BoletaRepository import BoletaRepository
from Clases.Comprobante import Boleta

historial = HistorialPila()

class BoletaController:
    def __init__(self):
        self.repo = BoletaRepository()

    def crear(self, pago, prefijo="BOL"):
        if not pago:
            raise ValueError("Debe proporcionar un pago válido")

        boleta = Boleta(0, pago)
        historial.push(f"Boleta creada", deepcopy(Global.boletas), "boletas")
        return self.repo.agregar(boleta, prefijo)

    def obtener_todos(self):
        return self.repo.listar_todos()

    def actualizar(self, id, pago):
        if not pago:
            raise ValueError("Debe proporcionar un pago válido")

        boleta = Boleta(id, pago)
        historial.push(f"Boleta actualizada: {id}", deepcopy(Global.boletas), "boletas")

        return self.repo.actualizar(id, boleta)

    def eliminar(self, id):
        if not id or id <= 0:
            raise ValueError("ID inválido")

        historial.push(f"Boleta eliminada: {id}", deepcopy(Global.boletas), "boletas")
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