from collections import deque
from Clases.Cliente import Cliente
import Global.Global as Global
from Estructuras.Arboles import construir_arbol, buscar


class ClientesRepository:
    historial_recientes = deque(maxlen=10)
    def __init__(self):
        self.clientes = Global.clientes


    def agregar(self, cliente: Cliente):
        Global.ultimo_id_cliente += 1
        cliente.id = Global.ultimo_id_cliente
        self.clientes.append(cliente)
        self.historial_recientes.append(cliente)
        return cliente

    def listar_todos(self):
        return self.clientes

    def buscar_id(self,id):
        Global.raiz_clientes = construir_arbol(Global.clientes, 'id')
        return buscar(Global.raiz_clientes, id, 'id')

    def actualizar(self, id, cliente_nuevo: Cliente):
        cliente = next((c for c in self.clientes if c.id == id), None)
        if not cliente:
            return False
        for attr, valor in vars(cliente_nuevo).items():
            if attr != 'id' and attr in vars(cliente) and valor is not None:
                setattr(cliente, attr, valor)
        return True

    def borrar(self, id):
        cliente = next((c for c in self.clientes if c.id == id), None)
        if cliente:
            self.clientes.remove(cliente)
            if cliente in self.historial_recientes:
                self.historial_recientes.remove(cliente)
            return True
        return False