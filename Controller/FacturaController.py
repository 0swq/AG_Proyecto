from copy import deepcopy
from Repository.FacturaRepository import FacturaRepository
from Clases.Comprobante import Factura
from Utils.Validador import Validador
from Estructuras.Pilas import HistorialPila
from Global import Global

historial = HistorialPila()


class FacturaController:
    def __init__(self):
        self.repo = FacturaRepository()

    def crear(self, pago, ruc, razon_social, prefijo="FAC"):
        if not pago:
            raise ValueError("Debe proporcionar un pago válido")

        if not Validador.ruc(ruc):
            raise ValueError("Debe proporcionar un RUC válido (11 dígitos)")

        if not Validador.razon_social(razon_social):
            raise ValueError("Debe proporcionar una razón social válida (entre 2 y 200 caracteres)")

        factura = Factura(0, pago, "", ruc.strip(), razon_social.strip())

        historial.push(f"Factura creada", deepcopy(Global.facturas), "facturas")

        return self.repo.agregar(factura, prefijo)

    def obtener_todos(self):
        return self.repo.listar_todos()

    def buscar_id(self, id):
        try:
            id = int(id)
        except ValueError:
            return f"El id no tiene un formato incorrecto"
        resultado = self.repo.buscar_id(id)
        if not resultado:
            return f"No se encontro el registro con el id: {id}"
        return resultado

    def actualizar(self, id, pago, ruc, razon_social):
        if not Validador.id_valido(id):
            raise ValueError("ID inválido")

        if not pago:
            raise ValueError("Debe proporcionar un pago válido")

        if not Validador.ruc(ruc):
            raise ValueError("Debe proporcionar un RUC válido (11 dígitos)")

        if not Validador.razon_social(razon_social):
            raise ValueError("Debe proporcionar una razón social válida (entre 2 y 200 caracteres)")

        historial.push(f"Factura actualizada: ID {id}", deepcopy(Global.facturas), "facturas")

        factura = Factura(id, pago, "", ruc.strip(), razon_social.strip())
        return self.repo.actualizar(id, factura)

    def eliminar(self, id):
        if not Validador.id_valido(id):
            raise ValueError("ID inválido")

        historial.push(f"Factura eliminada: ID {id}", deepcopy(Global.facturas), "facturas")

        return self.repo.borrar(id)

    def buscar(self, criterio):
        pass