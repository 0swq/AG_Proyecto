import Global.Global as Global
import View.Menu as menus
from Controller.EmpleadoController import EmpleadoController
from Controller.ProductoController import ProductosController

ProductosController = ProductosController()
ProductosController.crear("Pollo - 1/2","plato_principal",15,10,5)
ProductosController.crear("Pollo - 1","plato_principal",40,30,5)
ProductosController.crear("Pollo - 1/8","plato_principal",8,4,5)

#push
empleado_controller = EmpleadoController()
Global.usuario_actual= empleado_controller.crear(nombre="aw", rol="administrador", usuario="user", password="pass123")

menus.menu_principal()



import Global.Global as Global
import View.MenuLogin as menus

from Controller.EmpleadoController import EmpleadoController
from Controller.ProductoController import ProductosController

ProductosController = ProductosController()
ProductosController.crear("Pollo - 1/2","plato_principal",15,10,5)
ProductosController.crear("Pollo - 1","plato_principal",40,30,5)
ProductosController.crear("Pollo - 1/8","plato_principal",8,4,5)


empleado_controller = EmpleadoController()
Global.usuario_actual= empleado_controller.crear(nombre="aw", rol="administrador", usuario="user", password="pass123")

menus.menu_inicio()

