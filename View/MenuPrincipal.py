from Global import Global
from Utils.Limpiar import limpiar_consola
from Utils.Mensajes import mostrar_mensaje
from View.MenuClientes import menu_clientes
from View.MenuEmpleados import menu_empleados
from View.MenuPedidos import menu_pedidos
from View.MenuProductos import menu_productos
from View.MenuInicio import menu_login

def menu_principal():
    while True:
        limpiar_consola()
        print(f"\n--- Bienvenido | Usuario actual: {Global.usuario_actual.nombre}---")
        print("1. Pedidos")
        print("2. Clientes")
        print("3. Empleados")
        print("4. Productos")
        print("5. Stats")
        print("6. Cerrar sesion")
        print("7. Salir")

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
                if op == "2":
                    for i in Global.productos: print(i)
                if op == "3":
                    for i in Global.pedidos: print(i)
                if op == "4":
                    for i in Global.facturas: print(i)
                if op == "5":
                    for i in Global.empleados: print(i)
                if op == "6":
                    for i in Global.boletas: print(i)
                if op == "7":
                    break
                else: continue

        elif opcion == "6":
            Global.usuario_actual = None
            mostrar_mensaje("info","Sesión cerrada")
            menu_login()
        elif opcion=="7":
            break
        else:
            mostrar_mensaje(tipo="error",mensaje="Opción no válida")
