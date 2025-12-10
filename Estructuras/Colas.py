from copy import deepcopy
from Global import Global
from Estructuras.Pilas import HistorialPila

historial = HistorialPila()


class PedidosCola:
    @property
    def cabeza(self):
        return Global.cabeza_cola_pedidos
    @cabeza.setter
    def cabeza(self, valor):
        Global.cabeza_cola_pedidos = valor
    @property
    def cola(self):
        return Global.cola_cola_pedidos
    @cola.setter
    def cola(self, valor):
        Global.cola_cola_pedidos = valor
    def insertar_pedido(self, pedido):
        nuevo = Global.Nodo(pedido)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            self.cola = nuevo

    def completar_pedido(self):
        if self.cabeza is None:
            print("No hay pedidos en espera.")
            return None
        historial.push(
            "Pedido completado",
            [deepcopy(Global.pedidos), deepcopy(self.cabeza), deepcopy(self.cola),
             deepcopy(Global.facturas),deepcopy(Global.boletas)],"cola")
        pedido = self.cabeza.valor
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:
            self.cola = None
        pedido.estado = "completado"
        return pedido

    def cancelar_pedido(self):
        if self.cabeza is None:
            print("No hay pedidos en espera.")
            return None
        historial.push(
            "Pedido cancelado",
            [deepcopy(Global.pedidos), deepcopy(self.cabeza), deepcopy(self.cola),
             deepcopy(Global.facturas), deepcopy(Global.boletas)],"cola")
        pedido = self.cabeza.valor
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:
            self.cola = None
        pedido.estado = "cancelado"
        return pedido
    def mostrar_cola(self):
        temp = self.cabeza
        pedidos = []
        while temp:
            pedidos.append(temp.valor)
            temp = temp.siguiente
        return pedidos

    def JobSequence(self):
        historial.push(
            "Cola optimizada",
            [deepcopy(Global.pedidos), deepcopy(self.cabeza), deepcopy(self.cola)],
            "cola"
        )
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
        return resultado