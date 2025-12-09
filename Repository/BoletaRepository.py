from collections import deque
from Clases.Comprobante import Boleta
import Global.Global as Global
from Estructuras.Arboles import construir_arbol, buscar
from Utils.GenerarNumero import generar_numero_boleta


class BoletaRepository:
    historial_recientes = deque(maxlen=10)

    def __init__(self):
        self.items = Global.boletas

    def agregar(self, boleta: Boleta, prefijo="BOL"):
        Global.ultimo_id_boleta += 1
        boleta.id = Global.ultimo_id_boleta
        boleta.numero_comprobante = generar_numero_boleta(prefijo, boleta.id)
        self.items.append(boleta)
        self.historial_recientes.append(boleta)
        return boleta

    def listar_todos(self):
        return self.items


    def buscar_id(self,id):
        Global.raiz_boletas= construir_arbol(Global.boletas, 'id')
        return buscar(Global.raiz_boletas, id, 'id')

    def actualizar(self, id, boleta_nueva: Boleta):
        b = next((x for x in self.items if x.id == id), None)
        if not b:
            return False
        for attr, valor in vars(boleta_nueva).items():
            if attr != 'id' and attr in vars(b) and valor is not None:
                setattr(b, attr, valor)
        return True

    def borrar(self, id):
        b = next((x for x in self.items if x.id == id), None)
        if b:
            self.items.remove(b)
            if b in self.historial_recientes:
                self.historial_recientes.remove(b)
            return True
        return False