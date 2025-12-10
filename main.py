import Global.Global as Global
import View.MenuInicio as menus
from Clases.Empleado import Empleado
from Controller.EmpleadoController import EmpleadoController
from Controller.ProductoController import ProductosController
from Controller.ClienteController import ClientesController


productos_controller = ProductosController()
clientes_controller = ClientesController()
empleados_controller = EmpleadoController()


productos_controller.crear("Pollo - 1/2","plato_principal",15,10,5)
productos_controller.crear("Pollo - 1","plato_principal",40,30,5)
productos_controller.crear("Pollo - 1/8","plato_principal",8,4,5)

clientes_controller.crear("12345678")

Global.usuario_actual= Global.empleados.append(Empleado(id=0,nombre="default", rol="admin", usuario="default", password="default"))
clientes_controller.crear("12345678")
menus.menu_inicio()
