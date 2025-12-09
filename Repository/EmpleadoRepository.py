from collections import deque
from Clases.Empleado import Empleado
import Global.Global as Global
from Estructuras.Arboles import construir_arbol, buscar


class EmpleadoRepository:
    historial_recientes = deque(maxlen=10)

    def __init__(self):
        self.items = Global.empleados

    def agregar(self, empleado: Empleado):
        Global.ultimo_id_empleado += 1
        empleado.id = Global.ultimo_id_empleado
        self.items.append(empleado)
        self.historial_recientes.append(empleado)
        return empleado

    def listar_todos(self):
        return self.items

    def buscar_id(self, id):
        Global.raiz_empleados = construir_arbol(Global.empleados, 'id')
        return buscar(Global.raiz_empleados, id, 'id')

    def actualizar(self, id, empleado_nuevo: Empleado):
        emp = next((e for e in self.items if e.id == id), None)
        if not emp:
            return False
        for attr, valor in vars(empleado_nuevo).items():
            if attr != 'id' and attr in vars(emp) and valor is not None:
                setattr(emp, attr, valor)
        return True

    def borrar(self, id):
        emp = next((e for e in self.items if e.id == id), None)
        if emp:
            self.items.remove(emp)
            if emp in self.historial_recientes:
                self.historial_recientes.remove(emp)
            return True
        return False

    def buscar_por_usuario(self, usuario):
        return next((e for e in self.items if e.usuario == usuario), None)

    def autenticar(self, usuario, password):
        empleado = self.buscar_por_usuario(usuario)
        if empleado and empleado.password == password:
            return empleado
        return None

    def listar_por_rol(self, rol):
        return [e for e in self.items if e.rol.lower() == rol.lower()]