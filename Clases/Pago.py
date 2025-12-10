from datetime import datetime

from Global import Global


class Pago:
    def __init__(self, id, pedido, metodo, estado="pagado"):
        self.id = id
        self.pedido = pedido
        self.empleado = Global.usuario_actual
        self.metodo = metodo
        self.estado = estado
        self.fecha = datetime.now()
        self.monto = sum(d.subtotal for d in pedido.detalles if d.subtotal is not None) if pedido and pedido.detalles else 0

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        componentes = [
            f"ID: {self.id}",
            f"Pedido: {self.pedido.id if self.pedido else 'Sin pedido'}",
            f"Empleado: {self.empleado.nombre if self.empleado else 'Sin empleado'}",
            f"Monto: {self.monto:.2f}",
            f"Método: {self.metodo}",
            f"Estado: {self.estado}",
            f"Fecha: {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}"
        ]
        return " ➜ ".join(componentes)