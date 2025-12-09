from collections import deque

from Clases.DetallePedido import DetallePedido
import Global.Global as Global

class DetallePedidoRepository:
    historial_recientes = deque(maxlen=10)
    def agregar(self, detalle: DetallePedido):
        self.historial_recientes.append(detalle)
        return detalle

    def actualizar(self, detalle_nuevo: DetallePedido, detalle_actual: DetallePedido):
        for attr, valor in vars(detalle_nuevo).items():
            if  attr in vars(detalle_actual) and valor is not None:
                setattr(detalle_actual, attr, valor)
        return detalle_actual
