from Repository.PagoRepository import PagoRepository
from Clases.Pago import Pago
from Utils.Validador import Validador


class PagoController:
    def __init__(self):
        self.repo = PagoRepository()

    def crear(self, pedido,metodo, estado="pagado"):
        if not pedido:
            raise ValueError("Debe proporcionar un pedido válido")
        if not Validador.metodo_pago(metodo):
            raise ValueError("Método de pago inválido. Debe ser 'efectivo', 'tarjeta' o 'transferencia'")
        if not Validador.estado_pago(estado):
            raise ValueError("Estado inválido. Debe ser 'pagado', 'pendiente' o 'cancelado'")

        pago = Pago(0, pedido,metodo.lower().strip(), estado.lower().strip())
        return self.repo.agregar(pago)


    def actualizar(self, id, pedido, metodo, estado="pagado"):
        if not pedido:
            raise ValueError("Debe proporcionar un pedido válido")
        if not Validador.metodo_pago(metodo):
            raise ValueError("Método de pago inválido. Debe ser 'efectivo', 'tarjeta' o 'transferencia'")
        if not Validador.estado_pago(estado):
            raise ValueError("Estado inválido. Debe ser 'pagado', 'pendiente' o 'cancelado'")

        pago = Pago(id, pedido,metodo.lower().strip())
        return self.repo.actualizar(id, pago)

