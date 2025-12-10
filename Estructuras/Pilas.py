from copy import deepcopy
from datetime import datetime

from Global import Global

class HistorialPila:
    def __init__(self):
        self.historial:list = Global.historial

    def push(self, operacion,lista,clase):
        self.historial.append(
            {operacion: [lista, clase,datetime.now()]}
        )
        while len(self.historial) > 10:
            del self.historial[0]

    def peek(self):
        return self.historial[-1]

    def pop(self):
        if not self.historial:
            return None

        ultima_accion = self.historial.pop()
        operacion = list(ultima_accion.keys())[0]
        lista, clase, fecha = ultima_accion[operacion]

        if clase == "cola":
            Global.pedidos = lista[0]
            Global.cabeza_cola_pedidos = lista[1]
            Global.cola_cola_pedidos = lista[2]
        else:
            setattr(Global, clase, lista)

        return [operacion, clase, fecha]

    def clear(self):
        self.historial.clear()

    def obtener_invertido(self):
        resultado = []
        for i, elemento in enumerate(reversed(self.historial), start=1):
            operacion = list(elemento.keys())[0]
            lista, clase, fecha = elemento[operacion]

            resultado.append([i, operacion, clase, fecha])
        return resultado
