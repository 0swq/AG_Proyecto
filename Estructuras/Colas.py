import Global.Global as Global

class PedidosCola:
    def __init__(self):
        self.cabeza = Global.cabeza_cola_pedidos
        self.cola = Global.cola_cola_pedidos

    def insertar_pedido(self, pedido):
        nuevo = Global.Nodo(pedido)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
            return
        self.cola.siguiente = nuevo
        self.cola = nuevo

    def completar_pedido(self):
        if self.cabeza is None:
            print("No hay pedidos en espera.")
            return None
        pedido_completado = self.cabeza.valor
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:
            self.cola = None
        pedido_completado.estado="completado"
        return pedido_completado

    def cancelar_pedido(self):
        if self.cabeza is None:
            print("No hay pedidos en espera.")
            return None
        pedido_cancelado = self.cabeza.valor
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:
            self.cola = None
        pedido_cancelado.estado="cancelado"
        return pedido_cancelado

    def mostrar_cola(self):
        temp = self.cabeza
        pedidos = []
        while temp:
            pedidos.append(temp.valor)
            temp = temp.siguiente
        return pedidos

    def JobSequence(self):
        pedidos = []
        temp = self.cabeza
        while temp:
            pedidos.append(temp.valor)
            temp = temp.siguiente
        if not pedidos:
            return []
        pedidos_ordenados = sorted(pedidos, key=lambda p: p.valor, reverse=True)
        deadline_max = max(p.deadline for p in pedidos)

        slots = [None] * deadline_max
        no_asignados = []
        for p in pedidos_ordenados:
            asignado = False
            for t in range(min(p.deadline, deadline_max) - 1, -1, -1):
                if slots[t] is None:
                    slots[t] = p
                    asignado = True
                    break
            if not asignado:
                no_asignados.append(p)
        asignados = [p for p in slots if p is not None]
        resultado = asignados + no_asignados

        self.cabeza = None
        self.cola = None
        for p in resultado:
            nuevo = Global.Nodo(p)
            if self.cabeza is None:
                self.cabeza = nuevo
                self.cola = nuevo
            else:
                self.cola.siguiente = nuevo
                self.cola = nuevo
        Global.cabeza_cola_pedidos = self.cabeza
        Global.cola_cola_pedidos = self.cola
        return resultado
