from collections import deque
from Clases.Comprobante import Factura
import Global.Global as Global
from Estructuras.Arboles import construir_arbol, buscar
from Utils.GenerarNumero import generar_numero_factura

class FacturaRepository:
    historial_recientes = deque(maxlen=10)
    def __init__(self):
        self.items = Global.facturas

    def agregar(self, factura: Factura, prefijo="FAC"):
        Global.ultimo_id_factura += 1
        factura.id = Global.ultimo_id_factura
        factura.numeroFactura = generar_numero_factura(prefijo, factura.id)
        self.items.append(factura)
        self.historial_recientes.append(factura)
        return factura

    def listar_todos(self):
        return self.items
    def buscar_id(self,id):
        Global.raiz_facturas= construir_arbol(Global.facturas, 'id')
        return buscar(Global.raiz_facturas, id, 'id')

    def actualizar(self, id, factura_nueva: Factura):
        f = next((x for x in self.items if x.id == id), None)
        if not f:
            return False
        for attr, valor in vars(factura_nueva).items():
            if attr != 'id' and attr in vars(f) and valor is not None:
                setattr(f, attr, valor)
        return True

    def borrar(self, id):
        f = next((x for x in self.items if x.id == id), None)
        if f:
            self.items.remove(f)
            if f in self.historial_recientes:
                self.historial_recientes.remove(f)
            return True
        return False