from Utils.Limpiar import limpiar_consola
from View.Menu import menu_principal
from Clases.Empleado import Empleado
from Controller.EmpleadoController import EmpleadoController
from Utils.Confirmacion import pedir_confirmacion
from Utils.Mensajes import mostrar_mensaje

empleado_controller = EmpleadoController()

def menu_inicio():
    while True:
        limpiar_consola()
        print("\n====MENÚ PRINCIPAL====")
        print("1. Iniciar Sesión")
        print("2. Registrar")
        print("3. Salir")

        opcion = input("Seleccione una opción")

        if opcion == "1":
            menu_login()

        elif opcion == "2":
            menu_registrar()

        elif opcion == "3":
            mostrar_mensaje("info","Saliendo del sistema...")
            break
        else:
            mostrar_mensaje("error", "Opción inválida")
            input("Presione Enter para continuar...")



def menu_login():

    limpiar_consola()
    print("\n====INICIAR SESIÓN====")
    usuario = input("Usuario: ").strip()
    password = input("Contraseña: ").strip()

    empleado_logeado = empleado_controller.autenticar(usuario, password)

    if empleado_logeado:
        print(f"¡Login exitoso! Bienvenido, {empleado_logeado.nombre}")
        input("Presione Enter para acceder al sistema...")
        menu_principal()
    else:
        mostrar_mensaje("error", "Login fallido")
        input("Presione Enter para intentar de nuevo...")

def menu_registrar():

    limpiar_consola()
    print("\n====REGISTRAR====")

    nombre = input("Nombre: ").strip()
    rol = input("rol: ").strip()
    usuario = input("Usuario: ").strip()
    password = input("Password: ").strip()

    resultado = empleado_controller.crear(nombre, rol, usuario, password)

    if isinstance(resultado, str):

        mostrar_mensaje("error",f"Error al registrar: {resultado}")
        input("Presione Enter para intentar de nuevo...")
        menu_inicio()
    else:
        mostrar_mensaje( "info", "Registro exitoso!!")

        input("Presione entre para continuar al Inicio...")

    menu_inicio()

    return

