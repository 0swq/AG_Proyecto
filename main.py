import Global.Global as Global
import View.MenuInicio as menus
from Clases.Cliente import Cliente
from Clases.Empleado import Empleado
from Controller.EmpleadoController import EmpleadoController
from Controller.ProductoController import ProductosController
from Controller.ClienteController import ClientesController

ProductosController = ProductosController()
ProductosController.crear("Pollo - 1/2","plato_principal",15,10,5)
ProductosController.crear("Pollo - 1","plato_principal",40,30,5)
ProductosController.crear("Pollo - 1/8","plato_principal",8,4,5)

#push
empleado_controller = EmpleadoController()
cliente_controller=ClientesController()

Global.usuario_actual= Global.empleados.append(Empleado(id=0,nombre="default", rol="admin", usuario="default", password="default"))
cliente_controller.crear("12345678")
menus.menu_inicio()
