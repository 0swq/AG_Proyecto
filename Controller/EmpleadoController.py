from copy import deepcopy
from Repository.EmpleadoRepository import EmpleadoRepository
from Clases.Empleado import Empleado
from Utils.Validador import Validador
from Estructuras.Pilas import HistorialPila
from Global import Global

historial = HistorialPila()


class EmpleadoController:
    def __init__(self):
        self.repo = EmpleadoRepository()

    def crear(self, nombre, rol, usuario=None, password=None):
        if not Validador.nombre(nombre):
            return "Nombre inválido. Debe contener solo letras y espacios (2-50 caracteres)"
        if type(self.buscar_por_usuario(usuario)) == Empleado:
            return "Ya existe un empleado con ese usuario"
        if not Validador.rol(rol):
            return "Rol inválido. Debe ser 'administrador', 'cajero' o 'cocinero'"

        if usuario:
            if not Validador.usuario(usuario):
                return "Usuario inválido. Debe contener 4-20 caracteres alfanuméricos o guión bajo"
            if type(self.repo.buscar_por_usuario(usuario)) == Empleado:
                return "Error, ya hay un empleado registrado con ese usuario"

        if password and not Validador.password(password):
            return "Contraseña inválida. Debe contener 6-20 caracteres con al menos una letra y un número"

        if password and not usuario:
            return "Debe proporcionar un usuario si desea establecer una contraseña"

        empleado = Empleado(0, nombre.strip(), rol.lower().strip(),
                            usuario.strip() if usuario else None,
                            password)

        historial.push(f"Empleado creado: {nombre}", deepcopy(Global.empleados), "empleados")

        return self.repo.agregar(empleado)

    def obtener_todos(self):
        return self.repo.listar_todos()

    def actualizar(self, id, nombre=None, rol=None, usuario=None, password=None):
        try:
            id = int(id)
        except ValueError:
            return "El id no tiene un formato correcto"

        if nombre and not Validador.nombre(nombre):
            return "Nombre inválido. Debe contener solo letras y espacios (2-50 caracteres)"
        if rol and not Validador.rol(rol):
            return "Rol inválido. Debe ser 'administrador', 'cajero' o 'cocinero'"
        if usuario and not Validador.usuario(usuario):
            return "Usuario inválido. Debe contener 4-20 caracteres alfanuméricos o guión bajo"
        if password and not Validador.password(password):
            return "Contraseña inválida. Debe contener 6-20 caracteres con al menos una letra y un número"

        historial.push(f"Empleado actualizado: ID {id}", deepcopy(Global.empleados), "empleados")

        empleado = Empleado(id, nombre, rol, usuario, password)
        resultado = self.repo.actualizar(id, empleado)

        if not resultado:
            return f"No se encontró el registro con el id: {id}"
        return True

    def eliminar(self, id):
        try:
            id = int(id)
        except ValueError:
            return "El id no tiene un formato correcto"

        historial.push(f"Empleado eliminado: ID {id}", deepcopy(Global.empleados), "empleados")

        if not self.repo.borrar(id):
            return f"No se encontró el registro con el id: {id}"
        return True

    def buscar_id(self, id):
        try:
            id = int(id)
        except ValueError:
            return "El id no tiene un formato correcto"
        resultado = self.repo.buscar_id(id)
        if not resultado:
            return f"No se encontró el registro con el id: {id}"
        return resultado

    def autenticar(self, usuario, password):
        return self.repo.autenticar(usuario, password)

    def buscar_por_usuario(self, usuario):
        if not Validador.usuario(usuario):
            return "El usuario no tiene un formato correcto"
        resultado = self.repo.buscar_por_usuario(usuario)
        if not resultado:
            return f"No se encontro el registro"
        return resultado

    def listar_por_rol(self, rol):
        return self.repo.listar_por_rol(rol)