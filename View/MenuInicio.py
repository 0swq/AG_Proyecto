# View/MenuInicio.py

from Global import Global
from Controller.EmpleadoController import EmpleadoController
from Utils.Limpiar import limpiar_consola
from Utils.Mensajes import mostrar_mensaje
from Utils.Confirmacion import pedir_confirmacion

empleado_controller = EmpleadoController()


def menu_inicio():
    while True:
        limpiar_consola()
        print("\n--- Sistema de Restaurante ---")
        print("1. Iniciar Sesión")
        print("2. Salir")

        op = input("Seleccione opción: ")

        if op == "1":
            menu_login()
        elif op == "2":
            return
        else:
            mostrar_mensaje("error", "Opción inválida")


def menu_login():
    limpiar_consola()
    print("         INICIAR SESIÓN")
    print("=" * 50)
    print()

    try:
        print("Ingrese sus datos:")
        print("-" * 50)
        usuario = input("Usuario: ").strip()
        password = input("Contraseña: ").strip()

        if not usuario or not password:
            mostrar_mensaje("error", "Debe ingresar usuario y contraseña")
            input("\nPresiona cualquier tecla para continuar...")
            return

        empleado_logeado = empleado_controller.autenticar(usuario, password)

        if empleado_logeado:
            Global.usuario_actual = empleado_logeado
            mostrar_mensaje("exito", f"¡Bienvenido, {empleado_logeado.nombre}!")
            print(f"Rol: {empleado_logeado.rol.capitalize()}")
            input("\nPresiona cualquier tecla para acceder al sistema...")

            from View.MenuPrincipal import menu_principal
            menu_principal()

            Global.usuario_actual = None
        else:
            mostrar_mensaje("error", "Usuario o contraseña incorrectos")
            input("\nPresiona cualquier tecla para continuar...")

    except Exception as error:
        pass