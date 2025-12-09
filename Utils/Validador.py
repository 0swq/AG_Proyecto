import re

from Global import Global


class Validador:
    @staticmethod
    def nombre(nombre: str) -> bool:
        pattern = r"^[A-Za-zÁÉÍÓÚáéíóúñÑ ]{2,50}$"
        return bool(re.match(pattern, nombre.strip()))

    @staticmethod
    def telefono(telefono: str) -> bool:
        pattern = r"^\+?\d{7,15}$"
        return bool(re.match(pattern, telefono.strip()))

    @staticmethod
    def usuario(usuario: str) -> bool:
        pattern = r"^[A-Za-z0-9_]{4,20}$"
        return bool(re.match(pattern, usuario.strip()))

    @staticmethod
    def password(password: str) -> bool:
        pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,20}$"
        return bool(re.match(pattern, password.strip()))

    @staticmethod
    def nombre_producto(nombre: str) -> bool:
        return 2 <= len(nombre.strip()) <= 100

    @staticmethod
    def precio(precio) -> bool:
        try:
            return float(precio) > 0
        except:
            return False

    @staticmethod
    def rol(rol: str) -> bool:
        roles_validos = ['administrador', 'cajero', 'cocinero']
        return rol.lower().strip() in roles_validos

    @staticmethod
    def categoria(categoria: str) -> bool:
        categorias_validas = Global.categorias
        return categoria.lower().strip() in categorias_validas

    @staticmethod
    def cantidad(cantidad) -> bool:
        try:
            cantidad = int(cantidad)
            return cantidad > 0
        except:
            return False

    @staticmethod
    def tipo_pedido(tipo: str) -> bool:
        tipos_validos = Global.tipos_validos
        return tipo.lower().strip() in tipos_validos

    @staticmethod
    def metodo_pago(metodo: str) -> bool:
        metodos_validos = Global.metodos_validos
        return metodo.lower().strip() in metodos_validos

    @staticmethod
    def estado_pago(estado: str) -> bool:
        estados_validos = ['pagado', 'pendiente', 'cancelado']
        return estado.lower().strip() in estados_validos

    @staticmethod
    def tipo_factura(tipo: str) -> bool:
        tipos_validos = ['boleta', 'factura']
        return tipo.lower().strip() in tipos_validos

    @staticmethod
    def tiempo_preparacion(tiempo) -> bool:
        try:
            tiempo = int(tiempo)
            return 1 <= tiempo <= 180
        except:
            return False

    @staticmethod
    def prioridad(prioridad) -> bool:
        try:
            prioridad = int(prioridad)
            return 1 <= prioridad <= 5
        except:
            return False

    @staticmethod
    def ruc(ruc: str) -> bool:
        if not ruc or not ruc.strip():
            return False
        ruc = ruc.strip()
        pattern = r"^\d{11}$"
        return bool(re.match(pattern, ruc))

    @staticmethod
    def razon_social(razon_social: str) -> bool:
        if not razon_social or not razon_social.strip():
            return False
        return 2 <= len(razon_social.strip()) <= 200

    @staticmethod
    def id_valido(id) -> bool:
        try:
            return int(id) > 0
        except:
            return False