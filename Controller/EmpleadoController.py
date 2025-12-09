from Repository.EmpleadoRepository import EmpleadoRepository
from Clases.Empleado import Empleado
from Utils.Validador import Validador


class EmpleadoController:
    def __init__(self):
        self.repo = EmpleadoRepository()

    def crear(self, nombre, rol, usuario=None, password=None):
        if not Validador.nombre(nombre):
            return "Nombre inválido. Debe contener solo letras y espacios (2-50 caracteres)"
        if not Validador.rol(rol):
            return "Rol inválido. Debe ser 'administrador', 'cajero' o 'cocinero'"
        if usuario and not Validador.usuario(usuario):
            return "Usuario inválido. Debe contener 4-20 caracteres alfanuméricos o guión bajo"
        if password and not Validador.password(password):
            return "Contraseña inválida. Debe contener 6-20 caracteres con al menos una letra y un número"

        empleado = Empleado(0, nombre.strip(), rol.lower().strip(), usuario.strip() if usuario else None, password)
        return self.repo.agregar(empleado)

    def obtener_todos(self):
        return self.repo.listar_todos()

    def actualizar(self, id, nombre=None, rol=None, usuario=None, password=None):
        try:
            id = int(id)
        except ValueError:
            return "El id no tiene un formato incorrecto"

        if nombre and not Validador.nombre(nombre):
            return "Nombre inválido. Debe contener solo letras y espacios (2-50 caracteres)"
        if rol and not Validador.rol(rol):
            return "Rol inválido. Debe ser 'administrador', 'cajero' o 'cocinero'"
        if usuario and not Validador.usuario(usuario):
            return "Usuario inválido. Debe contener 4-20 caracteres alfanuméricos o guión bajo"
        if password and not Validador.password(password):
            return "Contraseña inválida. Debe contener 6-20 caracteres con al menos una letra y un número"

        empleado = Empleado(id, nombre, rol, usuario, password)
        resultado = self.repo.actualizar(id, empleado)

        if not resultado:
            return f"No se encontró el registro con el id: {id}"
        return True

    def eliminar(self, id):
        try:
            id = int(id)
        except ValueError:
            return "El id no tiene un formato incorrecto"
        if not self.repo.borrar(id):
            return f"No se encontró el registro con el id: {id}"
        return True

    def buscar_id(self, id):
        try:
            id = int(id)
        except ValueError:
            return "El id no tiene un formato incorrecto"
        resultado = self.repo.buscar_id(id)
        if not resultado:
            return f"No se encontró el registro con el id: {id}"
        return resultado

    def autenticar(self, usuario, password):
        return self.repo.autenticar(usuario, password)

    def listar_por_rol(self, rol):
        return self.repo.listar_por_rol(rol)

    def buscar(self, criterio):
        pass