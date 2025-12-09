from Utils.Limpiar import limpiar_consola
from Utils.Mensajes import mostrar_mensaje


def menu_empleados():
    while True:
        limpiar_consola()
        print("\n--- Gestión de Empleados ---")
        print("1. Registrar empleado")
        print("2. Listar empleados")
        print("3. Buscar empleado por nombre")
        print("4. Editar empleado")
        print("5. Eliminar empleado")
        print("6. Volver")

        op = input("Seleccione opción: ")

        if op == "1":
            registrar_empleado()
        elif op == "2":
            listar_empleados()
        elif op == "3":
            buscar_empleado_menu()
        elif op == "4":
            editar_empleado()
        elif op == "5":
            eliminar_empleado()
        elif op == "6":
            return
        else:
            mostrar_mensaje("error", "Opción inválida")
