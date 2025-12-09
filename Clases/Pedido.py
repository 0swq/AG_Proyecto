from datetime import datetime
import math

from Global import Global


class Pedido:
    def __init__(self, id, cliente, detalles,
                 tipo="salon", estado="pendiente", prioridad=1):
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
        tiempos_permitidos = {
            "salon": 40,
            "para_llevar": 25,
        }
        tiempo_permitido = tiempos_permitidos.get(self.tipo, 40)
        self.deadline = math.ceil(tiempo_permitido / 5)

    def __str__(self):
        return (f"Pedido(id={self.id}, cliente={self.cliente if self.cliente else 'Sin cliente'}, "
                f"empleado={self.empleado.nombre if self.empleado else 'Sin empleado'}, total={self.total}, "
                f"prep={self.tiempo_preparacion}min, deadline={self.deadline}, "
                f"valor={self.valor}, estado='{self.estado}')")