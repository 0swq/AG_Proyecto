from Global import Global
from Repository.PedidoRepository import PedidoRepository
from Clases.Pedido import Pedido
from Utils.Validador import Validador


class PedidosController:
    def __init__(self):
        self.repo = PedidoRepository()

    def crear(self, cliente, detalles, tipo="salon", estado="pendiente", prioridad=1):
        if not Validador.tipo_pedido(tipo):
            return f"Tipo de pedido inválido. Debe ser: {', '.join(Global.tipos_validos)}"

        if not Validador.prioridad(prioridad):
            return "Prioridad inválida. Debe ser un número entre 1 y 5"

        if not cliente:
            return "Debe proporcionar un cliente"

        pedido = Pedido(0, cliente, detalles, tipo.lower().strip(), estado.lower().strip(), int(prioridad))
        return self.repo.agregar(pedido)

    def obtener_todos(self):
        return self.repo.listar_todos()

    def obtener_completados(self):
        return self.repo.listar_completados()
    def obtener_pendientes(self):
        return self.repo.listar_pendientes()

    def actualizar(self, id, cliente=None, detalles=None, tipo=None, estado=None, prioridad=None):
        try:
            id = int(id)
        except ValueError:
            return "El id no tiene un formato correcto"

        if tipo and not Validador.tipo_pedido(tipo):
            return f"Tipo de pedido inválido. Debe ser: {', '.join(Global.tipos_validos)}"

        if prioridad and not Validador.prioridad(prioridad):
            return "Prioridad inválida. Debe ser un número entre 1 y 5"

        pedido_actual = self.buscar_id(id)
        if isinstance(pedido_actual, str):
            return pedido_actual

        pedido_nuevo = Pedido(id, cliente, detalles, tipo, estado, prioridad)
        resultado = self.repo.actualizar(id, pedido_actual, pedido_nuevo)

        if not resultado:
            return f"No se encontró el registro con el id: {id}"
        return True

    def eliminar(self, id):
        try:
            id = int(id)
        except ValueError:
            return "El id no tiene un formato correcto"

        if not self.repo.borrar(id):
            return f"No se encontró el registro con el id: {id}"
        return True

    def buscar_id(self, id):
        try:
            id = int(id)
        except ValueError:
            return "El id no tiene un formato correcto"

        resultado = next((p for p in self.repo.items if p.id == id), None)
        if not resultado:
            return f"No se encontró el registro con el id: {id}"
        return resultado