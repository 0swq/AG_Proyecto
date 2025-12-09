from Clases.Cliente import Cliente
from Controller.ClienteController import ClientesController
from Utils.Limpiar import limpiar_consola
from Utils.Mensajes import mostrar_mensaje
from Utils.Confirmacion import pedir_confirmacion

cliente_controller = ClientesController()


def menu_clientes():
    while True:
        limpiar_consola()
        print("\n--- Gestión de Clientes ---")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Editar cliente")
        print("5. Eliminar cliente")
        print("6. Volver")

        op = input("Seleccione opción: ")

        if op == "1":
            registrar_cliente()
        elif op == "2":
            listar_clientes()
        elif op == "3":
            buscar_cliente()
        elif op == "4":
            editar_cliente()
        elif op == "5":
            eliminar_cliente()
        elif op == "6":
            return
        else:
            mostrar_mensaje("error", "Opción inválida")


def registrar_cliente():
    limpiar_consola()
    print("         REGISTRAR NUEVO CLIENTE")
    print("=" * 50)
    print()

    try:
        print("Ingrese los datos del cliente:")
        print("-" * 50)
        nombre = input("Nombre completo: ").strip()
        telefono = input("Teléfono: ").strip()
        resultado = cliente_controller.crear(nombre, telefono)
        if type(resultado) is str:
            mostrar_mensaje("error", f"✗ No se pudo registrar el cliente, motivo: {resultado}")
        else:
            mostrar_mensaje("exito", "Cliente registrado exitosamente")
    except Exception as error:
        mostrar_mensaje("error", f"Error inesperado: {str(error)}")

    print()
    input("Presiona cualquier tecla para continuar...")


def listar_clientes():
    limpiar_consola()
    print("         LISTA DE CLIENTES")
    print("=" * 50)
    print()
    try:
        clientes = cliente_controller.obtener_todos()

        if not clientes:
            mostrar_mensaje("advertencia", "No hay clientes registrados")
        else:
            print(f"\n{'ID':<25} {'Nombre':<30} {'Teléfono':<15}")
            print("-" * 70)
            for cliente in clientes:
                print(f"{cliente.id:<25} {cliente.nombre:<30} {cliente.telefono:<15}")
            print(f"\nTotal de clientes: {len(clientes)}")
    except Exception as e:
        mostrar_mensaje("error", f"Error al listar clientes: {str(e)}")

    print()
    input("Presiona cualquier tecla para continuar...")


def buscar_cliente():
    limpiar_consola()
    print("         BUSCAR CLIENTE")
    print("=" * 50)
    print()
    try:
        id_solicitado = input("ID del cliente a buscar: ")
        cliente = cliente_controller.buscar_id(id_solicitado)

        if cliente is None:
            mostrar_mensaje("error", f"No se encontró el cliente con ID: {id_solicitado}")
        elif type(cliente) is str:
            mostrar_mensaje("error", cliente)
        else:
            print("\nCliente encontrado:")
            print(cliente)
    except Exception as error:
        mostrar_mensaje("error", f"Error al buscar: {str(error)}")

    print()
    input("Presiona cualquier tecla para continuar...")


def editar_cliente():
    limpiar_consola()
    print("         EDITAR CLIENTE")
    print("=" * 50)
    print()
    mostrar_mensaje("info",
                    f"Se procedera a listar todos los clientes registrados, escribe el id del que desees editar")

    listar_clientes()
    print("         ESCRIBE EL ID DE UN CLIENTE PARA EDITARLO")
    print("=" * 50)
    print()
    try:
        id_solicitado = input("ID que se desea editar: ")
        cliente = cliente_controller.buscar_id(id_solicitado)

        if cliente is None:
            mostrar_mensaje("error", f"No se encontró el cliente con ID: {id_solicitado}")
            input("\nPresiona cualquier tecla para continuar...")
            return

        if type(cliente) is str:
            mostrar_mensaje("error", cliente)
            input("\nPresiona cualquier tecla para continuar...")
            return

        limpiar_consola()
        print("==> Cliente seleccionado ==>")
        print(cliente)
        print()
        print("=" * 50)
        print()
        mostrar_mensaje("info", "Deja en blanco los atributos que no quieras modificar")
        nombre = input("Nombre completo: ").strip()
        telefono = input("Telefono: ").strip()
        if not nombre and not telefono:
            mostrar_mensaje("advertencia", "No se realizaron cambios")
        else:
            resultado = cliente_controller.actualizar(id_solicitado, nombre if nombre else None,
                                                      telefono if telefono else None)
            if type(resultado) is str:
                mostrar_mensaje("error", resultado)
            else:
                mostrar_mensaje("exito", "Actualizado correctamente")
    except Exception as error:
        mostrar_mensaje("error", f"Error al editar: {str(error)}")

    print()
    input("Presiona cualquier tecla para continuar...")


def eliminar_cliente():
    limpiar_consola()
    print("         ELIMINAR CLIENTE")
    print("=" * 50)
    mostrar_mensaje("info",
                    f"Se procedera a listar todos los clientes registrados, escribe el id del que desees eliminar")

    listar_clientes()
    print("         ESCRIBE EL ID DE UN CLIENTE PARA ELIMINARLO")
    print("=" * 50)
    print()
    try:
        id_solicitado = input("ID que se desea eliminar: ")
        cliente = cliente_controller.buscar_id(id_solicitado)

        if cliente is None:
            mostrar_mensaje("error", f"No se encontró el cliente con ID: {id_solicitado}")
            input("\nPresiona cualquier tecla para continuar...")
            return

        if type(cliente) is str:
            mostrar_mensaje("error", cliente)
            input("\nPresiona cualquier tecla para continuar...")
            return

        prueba_uno = pedir_confirmacion(f"Estas realmente seguro de eliminar el cliente (I): {cliente}")
        if not prueba_uno: return
        prueba_dos = pedir_confirmacion(f"Estas realmente seguro de eliminar el cliente (II): {cliente}")
        if not prueba_dos: return
        prueba_tres = pedir_confirmacion(f"Estas realmente seguro de eliminar el cliente (III): {cliente}")
        if not prueba_tres: return

        resultado = cliente_controller.eliminar(id_solicitado)
        if type(resultado) is str:
            mostrar_mensaje("error", resultado)
        else:
            mostrar_mensaje("exito", "Cliente eliminado exitosamente")
    except Exception as error:
        mostrar_mensaje("error", f"Error al eliminar: {str(error)}")

    print()
    input("Presiona cualquier tecla para continuar...")