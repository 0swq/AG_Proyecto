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
        cliente_info = f", cliente='{self.cliente_nombre}'" if self.cliente_nombre else ""
        return (f"Boleta(id={self.id}, numero='{self.numero_comprobante}', "
                f"total={self.total:.2f}{cliente_info}, "
                f"fecha='{self.fecha_emision.strftime('%Y-%m-%d %H:%M:%S')}')")


class Factura(ComprobanteInterface):
    def __init__(self, id, pago, numero_factura, ruc, razon_social):
        super().__init__(id, pago)
        self.numero_comprobante = numero_factura if numero_factura else generar_numero_factura(Global.ultimo_id_factura)
        self.ruc = ruc
        self.razon_social = razon_social

    def __str__(self):
        return (f"Factura(id={self.id}, numero='{self.numero_comprobante}', "
                f"total={self.total:.2f}, ruc='{self.ruc}', "
                f"razon_social='{self.razon_social}', "
                f"fecha='{self.fecha_emision.strftime('%Y-%m-%d %H:%M:%S')}')")