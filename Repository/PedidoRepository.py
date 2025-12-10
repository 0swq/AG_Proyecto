from collections import deque
from Clases.Pedido import Pedido
import Global.Global as Global
from Estructuras.Arboles import construir_arbol, buscar


class PedidoRepository:
    historial_recientes = deque(maxlen=10)

    @property
    def items(self):
        return Global.pedidos

    def agregar(self, pedido: Pedido):
        Global.ultimo_id_pedido += 1
        pedido.id = Global.ultimo_id_pedido
        self.items.append(pedido)
        self.historial_recientes.append(pedido)
        return pedido

    def listar_todos(self):
        return self.items

    def listar_completados(self):
        return [i for i in self.items if i.estado=="completado"]

    def listar_pendientes(self):
        return [i for i in self.items if i.estado=="pendiente"]

    def buscar_id(self, id):
        Global.raiz_pedidos = construir_arbol(Global.pedidos, 'id')
        return buscar(Global.raiz_pedidos, id, 'id')

    def actualizar(self, id, pedido_actual: Pedido, pedido_nuevo: Pedido):
        if not pedido_actual:
            return False
        for attr, valor in vars(pedido_nuevo).items():
            if attr != 'id' and attr in vars(pedido_actual) and valor is not None:
                setattr(pedido_actual, attr, valor)

        if pedido_actual.detalles:
            pedido_actual.total = sum(d.subtotal for d in pedido_actual.detalles if d.subtotal is not None)
            pedido_actual.valor = sum(d.rentabilidad for d in pedido_actual.detalles if d.rentabilidad is not None)
            pedido_actual.tiempo_preparacion = max(
                (d.tiempo_total for d in pedido_actual.detalles if d.tiempo_total is not None), default=0)

        return pedido_actual

    def borrar(self, id):
        pedido = next((p for p in self.items if p.id == id), None)
        if pedido:
            self.items.remove(pedido)
            if pedido in self.historial_recientes:
                self.historial_recientes.remove(pedido)
            return True
        return False
