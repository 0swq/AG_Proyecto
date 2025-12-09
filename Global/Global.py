from Controller import ClienteController
from Controller.EmpleadoController import EmpleadoController

#Esta clase esta hecha para contener datos en memoria de forma global y centrailzada

usuario_actual = None

clientes = []
productos = []
pedidos = []
facturas = []
empleados = []
boletas = []

ultimo_id_boleta = 0
ultimo_id_cliente = 0
ultimo_id_empleado = 0
ultimo_id_producto = 0
ultimo_id_pedido = 0
ultimo_id_pago = 0
ultimo_id_factura = 0

cabeza_cola_pedidos = None
cola_cola_pedidos = None


raiz_empleados = None
raiz_clientes=None
raiz_facturas=None
raiz_boletas=None
raiz_productos = None
raiz_pedidos = None

categorias = ['entrada', 'plato_principal', 'postre', 'bebida']
tipos_validos =['salon', 'llevar']
metodos_validos = ['efectivo', 'tarjeta', 'transferencia']


class Nodo:
    def __init__(self,valor):
        self.valor=valor
        self.siguiente=None


