from Controller.EmpleadoController import EmpleadoController
from Global import Global
from Utils.Limpiar import limpiar_consola
from Utils.Mensajes import mostrar_mensaje
from Utils.Confirmacion import pedir_confirmacion
from Utils.Validador import Validador

empleado_controller = EmpleadoController()


def menu_empleados():
    while True:
        limpiar_consola()
        print("\n--- Gestión de Empleados ---")
        print("1. Registrar empleado")
        print("2. Listar empleados")
        print("3. Buscar empleado")
        print("4. Editar empleado")
        print("5. Eliminar empleado")
        print("6. Volver")

        op = input("Seleccione opción: ")

        if op == "1":
            registrar_empleado()
        elif op == "2":
            listar_empleados()
        elif op == "3":
            buscar_empleado()
        elif op == "4":
            if Global.usuario_actual.roll=="admin":
                editar_empleado()
            else:
                mostrar_mensaje("advertencia","Acción no permitida para usuario  normal")
        elif op == "5":
            eliminar_empleado()
        elif op == "6":
            return
        else:
            mostrar_mensaje("error", "Opción inválida")


def registrar_empleado():
    limpiar_consola()
    print("         REGISTRAR NUEVO EMPLEADO")
    print("=" * 50)
    print()

    try:
        print("Ingrese los datos del empleado:")
        print("-" * 50)
        nombre = input("Nombre completo: ").strip()

        print("\nRoles disponibles:")
        print(Global.roles)
        print()
        rol = input("Rol: ").strip().lower()
        if not Validador.rol(rol):
            mostrar_mensaje("errr","Rol invalido.")

        prueba = pedir_confirmacion("¿Desea agregar usuario y contraseña para acceso al sistema?")
        usuario = None
        password = None

        if prueba:
            print("\nDatos de acceso:")
            usuario = input("Usuario: ").strip()
            password = input("Contraseña: ").strip()

        resultado = empleado_controller.crear(nombre, rol, usuario, password)

        if type(resultado) is str:
            mostrar_mensaje("error", f"✗ No se pudo registrar el empleado, motivo: {resultado}")
        else:
            mostrar_mensaje("exito", f"Empleado registrado exitosamente - ID: {resultado.id}")
    except Exception as error:
        mostrar_mensaje("error", f"Error inesperado: {str(error)}")

    print()
    input("Presiona cualquier tecla para continuar...")


def listar_empleados():
    limpiar_consola()
    print("         LISTA DE EMPLEADOS")
    print("=" * 50)
    print()
    try:
        empleados = empleado_controller.obtener_todos()

        if not empleados:
            mostrar_mensaje("advertencia", "No hay empleados registrados")
        else:
            print(f"\n{'ID':<5} {'Nombre':<30} {'Rol':<20} {'Usuario':<20}")
            print("-" * 80)
            for empleado in empleados:
                nombre_corto = empleado.nombre[:27] + "..." if len(empleado.nombre) > 30 else empleado.nombre
                usuario = empleado.usuario if empleado.usuario else "N/A"
                print(f"{empleado.id:<5} {nombre_corto:<30} {empleado.rol:<20} {usuario:<20}")
            print(f"\nTotal de empleados: {len(empleados)}")
    except Exception as e:
        mostrar_mensaje("error", f"Error al listar empleados: {str(e)}")

    print()
    input("Presiona cualquier tecla para continuar...")


def buscar_empleado():
    limpiar_consola()
    print("         BUSCAR EMPLEADO")
    print("=" * 50)
    print()
    try:
        id_solicitado = input("ID del empleado a buscar: ")
        empleado = empleado_controller.buscar_id(id_solicitado)

        if empleado is None:
            mostrar_mensaje("error", f"No se encontró el empleado con ID: {id_solicitado}")
        elif type(empleado) is str:
            mostrar_mensaje("error", empleado)
        else:
            print("\nEmpleado encontrado:")
            print(empleado)
    except Exception as error:
        mostrar_mensaje("error", f"Error al buscar: {str(error)}")

    print()
    input("Presiona cualquier tecla para continuar...")


def editar_empleado():
    limpiar_consola()
    print("         EDITAR EMPLEADO")
    print("=" * 50)
    print()
    mostrar_mensaje("info",
                    "Se procederá a listar todos los empleados registrados, escribe el id del que desees editar")

    listar_empleados()
    print("         ESCRIBE EL ID DE UN EMPLEADO PARA EDITARLO")
    print("=" * 50)
    print()
    try:
        id_solicitado = input("ID que se desea editar: ")
        empleado = empleado_controller.buscar_id(id_solicitado)

        if empleado is None:
            mostrar_mensaje("error", f"No se encontró el empleado con ID: {id_solicitado}")
            input("\nPresiona cualquier tecla para continuar...")
            return

        if type(empleado) is str:
            mostrar_mensaje("error", empleado)
            input("\nPresiona cualquier tecla para continuar...")
            return

        limpiar_consola()
        print("==> Empleado seleccionado ==>")
        print(empleado)
        print()
        print("=" * 50)
        print()
        mostrar_mensaje("info", "Deja en blanco los atributos que no quieras modificar")
        nombre = input("Nombre completo: ").strip()

        print("\nRoles disponibles:")
        print(Global.roles)
        print()
        rol = input("Rol: ").strip().lower()

        usuario = None
        password=None
        if (empleado.usuario ==None) and (empleado.password == None) :
            prueba = pedir_confirmacion("¿Desea agregar usuario y contraseña para acceso al sistema?")
            if prueba:
                usuario = input("Usuario: ").strip()
                password = input("Contraseña: ").strip()

        if not nombre and not rol and not usuario and not password:
            mostrar_mensaje("advertencia", "No se realizaron cambios")
        else:
            resultado = empleado_controller.actualizar(
                id_solicitado,
                nombre if nombre else None,
                rol if rol else None,
                usuario if usuario else None,
                password if password else None
            )

            if type(resultado) is str:
                mostrar_mensaje("error", resultado)
            else:
                mostrar_mensaje("exito", "Actualizado correctamente")
    except Exception as error:
        mostrar_mensaje("error", f"Error al editar: {str(error)}")

    print()
    input("Presiona cualquier tecla para continuar...")


def eliminar_empleado():
    limpiar_consola()
    print("         ELIMINAR EMPLEADO")
    print("=" * 50)
    mostrar_mensaje("info",
                    "Se procederá a listar todos los empleados registrados, escribe el id del que desees eliminar")

    listar_empleados()
    print("         ESCRIBE EL ID DE UN EMPLEADO PARA ELIMINARLO")
    print("=" * 50)
    print()
    try:
        id_solicitado = input("ID que se desea eliminar: ")
        empleado = empleado_controller.buscar_id(id_solicitado)
        if empleado==Global.usuario_actual:
            mostrar_mensaje("error","No puedes eliminarte a ti mismo")
        if empleado is None:
            mostrar_mensaje("error", f"No se encontró el empleado con ID: {id_solicitado}")
            input("\nPresiona cualquier tecla para continuar...")
            return

        if type(empleado) is str:
            mostrar_mensaje("error", empleado)
            input("\nPresiona cualquier tecla para continuar...")
            return

        prueba_uno = pedir_confirmacion(f"¿Estás realmente seguro de eliminar el empleado (I): {empleado.nombre}?")
        if not prueba_uno:
            return
        prueba_dos = pedir_confirmacion(f"¿Estás realmente seguro de eliminar el empleado (II): {empleado.nombre}?")
        if not prueba_dos:
            return
        prueba_tres = pedir_confirmacion(f"¿Estás realmente seguro de eliminar el empleado (III): {empleado.nombre}?")
        if not prueba_tres:
            return

        resultado = empleado_controller.eliminar(id_solicitado)
        if type(resultado) is str:
            mostrar_mensaje("error", resultado)
        else:
            mostrar_mensaje("exito", "Empleado eliminado exitosamente")
    except Exception as error:
        mostrar_mensaje("error", f"Error al eliminar: {str(error)}")
