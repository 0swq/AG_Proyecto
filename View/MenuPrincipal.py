from Global import Global
from Utils.Confirmacion import pedir_confirmacion
from Utils.Limpiar import limpiar_consola
from Utils.Mensajes import mostrar_mensaje
from View.MenuClientes import menu_clientes
from View.MenuEmpleados import menu_empleados
from View.MenuPedidos import menu_pedidos
from View.MenuProductos import menu_productos
from View.MenuInicio import menu_login
from Estructuras.Pilas import HistorialPila

pila_historial = HistorialPila()


def menu_principal():
    while True:
        limpiar_consola()
        print(f"\n--- Bienvenido | Usuario actual: {Global.usuario_actual.nombre}---")
        print("1. Pedidos")
        print("2. Clientes")
        print("3. Empleados")
        print("4. Productos")
        print("5. Stats")
        print("6. Cerrar sesión")
        print("7. Historial de acciones")
        print("8. Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            menu_pedidos()
        elif opcion == "2":
            menu_clientes()
        elif opcion == "3":
            menu_empleados()
        elif opcion == "4":
            menu_productos()
        elif opcion == "5":
            while True:
                limpiar_consola()
                print(f"1. Clientes totales: {len(Global.clientes)}")
                print(f"2. Productos totales: {len(Global.productos)}")
                print(f"3. Pedidos totales: {len(Global.pedidos)}")
                print(f"4. Facturas totales: {len(Global.facturas)}")
                print(f"5. Empleados totales: {len(Global.empleados)}")
                print(f"6. Boletas totales: {len(Global.boletas)}")
                print(f"7. Salir")
                op = input("Seleccione opcion: ")
                if op == "1":
                    for i in Global.clientes: print(i)
                    input("Presiona cualquier tecla para continuar...")
                elif op == "2":
                    for i in Global.productos: print(i)
                    input("Presiona cualquier tecla para continuar...")
                elif op == "3":
                    for i in Global.pedidos: print(i)
                    input("Presiona cualquier tecla para continuar...")
                elif op == "4":
                    for i in Global.facturas: print(i)
                    input("Presiona cualquier tecla para continuar...")
                elif op == "5":
                    for i in Global.empleados: print(i)
                    input("Presiona cualquier tecla para continuar...")
                elif op == "6":
                    for i in Global.boletas: print(i)
                    input("Presiona cualquier tecla para continuar...")
                elif op == "7":
                    break
        elif opcion == "6":
            Global.usuario_actual = None
            mostrar_mensaje("info", "Sesión cerrada")
            menu_login()
        elif opcion == "7":
            ver_historial()
        elif opcion == "8":
            break
        else:
            mostrar_mensaje(tipo="error", mensaje="Opción no válida")


def ver_historial():
    limpiar_consola()
    print("         HISTORIAL DE OPERACIONES")
    print("=" * 80)
    print()

    try:
        historial = pila_historial.obtener_invertido()

        if not historial or len(historial) == 0:
            mostrar_mensaje("advertencia", "No hay operaciones en el historial")
            print()
            input("Presiona cualquier tecla para continuar...")
            return

        print(f"\n{'#':<5} {'Operación':<40} {'Entidad':<15} {'Fecha y Hora':<20}")
        print("-" * 80)

        for elemento in historial:
            num, operacion, clase, fecha = elemento

            fecha_formateada = fecha.strftime("%d/%m/%Y %H:%M:%S")
            operacion_corta = operacion[:37] + "..." if len(operacion) > 40 else operacion

            print(f"{num:<5} {operacion_corta:<40} {clase:<15} {fecha_formateada:<20}")

        print(f"\nTotal de operaciones: {len(historial)}")
        print()
        input("Presiona cualquier tecla para continuar...")

        prueba = pedir_confirmacion("¿Desea revertir la última acción?")
        if prueba:
            resultado = pila_historial.pop()
            if resultado:
                mostrar_mensaje("exito", "Última acción revertida correctamente")
            else:
                mostrar_mensaje("advertencia", "No hay acciones para revertir")
            input("Presiona cualquier tecla para continuar...")

    except Exception as e:
        mostrar_mensaje("error", f"Error al mostrar historial: {str(e)}")
