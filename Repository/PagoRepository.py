from collections import deque
from Clases.Pago import Pago
import Global.Global as Global
from Estructuras.Arboles import construir_arbol, buscar


class PagoRepository:
    historial_recientes = deque(maxlen=10)

    def agregar(self, pago: Pago):
        Global.ultimo_id_pago += 1
        pago.id = Global.ultimo_id_pago
        self.historial_recientes.append(pago)
        return pago


    def actualizar(self,pago_nuevo: Pago, pago_actual:Pago):
        for attr, valor in vars(pago_nuevo).items():
            if attr != 'id' and attr in vars(pago_actual) and valor is not None:
                setattr(pago_actual, attr, valor)
        return pago_actual
