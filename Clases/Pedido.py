from datetime import datetime
import math
from Global import Global
from Utils.Validador import Validador


class Pedido:
    def __init__(self, id, cliente, detalles, tipo="salon", estado="pendiente", prioridad=1):
        self.id = id
        self.cliente = cliente
        self.empleado = Global.usuario_actual
        self.tipo = tipo
        self.estado = estado
        self.detalles = detalles or []
        self.total = sum(d.subtotal for d in self.detalles if d.subtotal is not None)
        self.valor = sum(d.rentabilidad for d in self.detalles if d.rentabilidad is not None)
        self.tiempo_preparacion = max((d.tiempo_total for d in self.detalles if d.tiempo_total is not None), default=0)
        self.fecha = datetime.now()
        self.prioridad = prioridad
        tiempo_permitido = Validador.tiempo_permitido_pedido(self.tipo)
        self.deadline = math.ceil(tiempo_permitido / 5)

    def __str__(self):
        componentes = [
            f"ID: {self.id}",
            f"Cliente: {self.cliente if self.cliente else 'Sin cliente'}",
            f"Empleado: {self.empleado.nombre if self.empleado else 'Sin empleado'}",
            f"Tipo: {self.tipo}",
            f"Estado: {self.estado}",
            f"Total: {self.total:.2f}",
            f"Valor: {self.valor:.2f}",
            f"Preparación: {self.tiempo_preparacion}min",
            f"Deadline: {self.deadline}",
            f"Fecha: {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}",
            f"Prioridad: {self.prioridad}",
            f"Items: {len(self.detalles)}"
        ]
        return " ➜ ".join(componentes)