from datetime import datetime
from abc import ABC, abstractmethod

from Global import Global
from Utils.GenerarNumero import generar_numero_factura


class ComprobanteInterface(ABC):
    def __init__(self, id, pago):
        self.id = id
        self.pago = pago
        self.numero_comprobante = None
        self.fecha_emision = datetime.now()
        self.total = pago.monto

    def __repr__(self):
        return self.__str__()


class Boleta(ComprobanteInterface):
    def __init__(self, id, pago):
        super().__init__(id, pago)
        self.numero_comprobante = generar_numero_factura(Global.ultimo_id_factura)
        self.cliente_nombre = pago.pedido.cliente

    def __str__(self):
        componentes = [
            f"Tipo: Boleta",
            f"ID: {self.id}",
            f"N°: {self.numero_comprobante}",
            f"Total: {self.total:.2f}",
            f"Fecha: {self.fecha_emision.strftime('%Y-%m-%d %H:%M:%S')}"
        ]

        if self.cliente_nombre:
            componentes.append(f"Cliente: {self.cliente_nombre}")

        return " ➜ ".join(componentes)


class Factura(ComprobanteInterface):
    def __init__(self, id, pago, numero_factura, ruc, razon_social):
        super().__init__(id, pago)
        self.numero_comprobante = numero_factura if numero_factura else generar_numero_factura(Global.ultimo_id_factura)
        self.ruc = ruc
        self.razon_social = razon_social

    def __str__(self):
        componentes = [
            f"Tipo: Factura",
            f"ID: {self.id}",
            f"N°: {self.numero_comprobante}",
            f"Total: {self.total:.2f}",
            f"RUC: {self.ruc}",
            f"Razón Social: {self.razon_social}",
            f"Fecha: {self.fecha_emision.strftime('%Y-%m-%d %H:%M:%S')}"
        ]

        return " ➜ ".join(componentes)
