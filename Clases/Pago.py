from datetime import datetime

from Global import Global


class Pago:
    def __init__(self, id, pedido, metodo, estado="pagado"):
        self.id = id
        self.pedido = pedido
        self.empleado = Global.usuario_actual
        self.monto = sum(d.subtotal for d in pedido.detalles if d.subtotal is not None) if pedido and pedido.detalles else 0
        self.metodo = metodo
        self.estado = estado
        self.fecha = datetime.now()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return (f"Pago(id={self.id}, pedido={self.pedido.id if self.pedido else 'Sin pedido'}, "
                f"empleado={self.empleado.nombre if self.empleado else 'Sin empleado'}, "
                f"monto={self.monto:.2f}, metodo='{self.metodo}', estado='{self.estado}')")