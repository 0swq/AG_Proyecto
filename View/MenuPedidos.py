from Clases.Comprobante import Boleta
from Clases.DetallePedido import DetallePedido
from Clases.Pago import Pago
from Controller.BoletaController import BoletaController
from Controller.DetallePedidoController import DetallePedidoController
from Controller.FacturaController import FacturaController
from Controller.PagoController import PagoController
from Controller.PedidoController import PedidosController
from Controller.ProductoController import ProductosController
from Estructuras.Colas import PedidosCola
from Global import Global
from Utils.Limpiar import limpiar_consola
from Utils.Mensajes import mostrar_mensaje
from Utils.Confirmacion import pedir_confirmacion
from Utils.Validador import Validador
from View import MenuProductos
from View.MenuComprobantes import menu_comprobantes

pedido_controller = PedidosController()
pedidos_cola = PedidosCola()
productos_controller = ProductosController()
detalle_controller = DetallePedidoController()
pago_controller = PagoController()
factura_controller = FacturaController()
boleta_controller = BoletaController()
def menu_pedidos():
    while True:
        limpiar_consola()
        print("\n--- Gestión de Pedidos ---")
        print("1. Crear pedido")
        print("2. Ver pedidos en cola")
        print("3. Completar pedido")
        print("4. Buscar pedido por ID")
        print("5. Cancelar pedido")
        print("6. Optimizar cola de pedidos")
        print("7. Ver pedidos completados / comprobantes")
        print("8. Volver")

        op = input("Seleccione opción: ")

        if op == "1":
            crear_pedido()
        elif op == "2":
            mostrar_cola()
        elif op == "3":
            completar_pedido()
        elif op == "4":
            buscar_pedido()
        elif op == "5":
            cancelar_pedido()
        elif op == "6":
            optimizar_cola()
        elif op == "7":
            ver_pedidos()
        elif op == "8":
            return
        else:
            mostrar_mensaje("error", "Opción inválida")


def crear_pedido():
    limpiar_consola()
    print("         CREAR NUEVO PEDIDO")
    print("=" * 50)
    print()

    try:
        print("Ingrese los datos del pedido:")
        print("-" * 50)

        mostrar_mensaje("advertencia", "Debes escribir el nombre del cliente")
        cliente = input("Ingrese el nombre del cliente: ").strip()
        if not Validador.nombre(cliente):
            mostrar_mensaje("error", "Nombre inválido")
            return

        detalles = []
        while True:
            prueba = pedir_confirmacion("¿Deseas agregar un producto al pedido?")
            if not prueba:
                if len(detalles) == 0:
                    mostrar_mensaje("error", "Debe agregar al menos un producto")
                    return
                break

            mostrar_mensaje("info", "Se listarán los productos, selecciona uno para agregarlo al detalle")
            print("         SELECCIONA UN PRODUCTO")
            print("=" * 50)
            print()
            MenuProductos.listar_productos()

            id_producto = input("Ingrese el ID del producto: ")
            producto = productos_controller.buscar_id(id_producto)
            if type(producto) is str:
                mostrar_mensaje("error", producto)
                continue

            cantidad = input("Ingrese la cantidad (número): ")

            detalle = detalle_controller.crear(producto, cantidad)
            if type(detalle) is str:
                mostrar_mensaje("error", detalle)
                continue

            detalles.append(detalle)
            mostrar_mensaje("exito", f"Producto agregado: {detalle}")

        mostrar_mensaje("info", "Indica el tipo de pedido")
        print("Tipos disponibles: salon, para llevar")
        tipo = input("Ingrese el tipo: ").strip().lower()
        while tipo != "salon" and tipo != "para llevar":
            mostrar_mensaje("error", "Tipo inválido. Debe ser 'salon' o 'para llevar'")
            tipo = input("Ingrese el tipo: ").strip().lower()

        mostrar_mensaje("info", "Debe asignar una prioridad 1-5")
        prioridad = 0
        while prioridad < 1 or prioridad > 5:
            try:
                prioridad = int(input("Ingrese la prioridad (1-5): "))
                if prioridad < 1 or prioridad > 5:
                    mostrar_mensaje("error", "La prioridad debe estar entre 1 y 5")
            except ValueError:
                mostrar_mensaje("error", "Debe ingresar un número")

        resultado = pedido_controller.crear(cliente, detalles, tipo, "pendiente", prioridad)
        pedidos_cola.insertar_pedido(resultado)

        if type(resultado) is str:
            mostrar_mensaje("error", f"No se pudo crear el pedido: {resultado}")
        else:
            mostrar_mensaje("exito", f"Pedido creado exitosamente - ID: {resultado.id}")

    except Exception as error:
        mostrar_mensaje("error", f"Error inesperado: {str(error)}")

    print()
    input("Presiona cualquier tecla para continuar...")


def mostrar_cola():
    limpiar_consola()
    print("         PEDIDOS EN COLA")
    print("=" * 50)
    print()
    try:
        pedidos = pedidos_cola.mostrar_cola()

        if not pedidos:
            mostrar_mensaje("advertencia", "No hay pedidos registrados")
        else:
            print(
                f"\n{'ID':<5} {'Cliente':<20} {'Empleado':<20} {'Tipo':<12} {'Estado':<15} {'Total':<10} {'Prior':<6}")
            print("-" * 95)
            for pedido in pedidos:
                cliente_nombre = pedido.cliente if pedido.cliente else "Sin cliente"
                empleado_nombre = pedido.empleado.nombre if pedido.empleado else "Sin empleado"
                print(f"{pedido.id:<5} {cliente_nombre:<20} {empleado_nombre:<20} "
                      f"{pedido.tipo:<12} {pedido.estado:<15} {pedido.total:<10.2f} {pedido.prioridad:<6}")
            print(f"\nTotal de pedidos: {len(pedidos)}")
    except Exception as e:
        mostrar_mensaje("error", f"Error al listar pedidos: {str(e)}")

    print()
    input("Presiona cualquier tecla para continuar...")


def completar_pedido():
    limpiar_consola()
    print("         COMPLETAR PEDIDO")
    print("=" * 50)
    print()
    print("         PRÓXIMO PEDIDO EN COLA")
    print("=" * 50)
    print()
    try:
        pedido = pedidos_cola.mostrar_cola()

        if pedido is None or len(pedido) == 0:
            mostrar_mensaje("error", "No hay pedidos en cola")
            input("\nPresiona cualquier tecla para continuar...")
            return

        pedido = pedido[0]
        print(pedido)

        prueba_uno = pedir_confirmacion("¿Estás seguro de completar el pedido (I)?")
        if not prueba_uno:
            return

        prueba_dos = pedir_confirmacion("¿Estás seguro de completar el pedido (II)?")
        if not prueba_dos:
            return

        mostrar_mensaje("info",
                        "El pedido procederá a completarse, para ello llena los datos del pago, luego la factura")

        limpiar_consola()
        print()
        print("         CREAR PAGO")
        print("=" * 50)
        print()
        print("Métodos disponibles:", ", ".join(Global.metodos_validos))
        print()

        metodo = None
        while metodo not in Global.metodos_validos:
            metodo = input("Ingrese el método de pago: ").lower().strip()
            if metodo not in Global.metodos_validos:
                mostrar_mensaje("error", f"Método inválido. Use: {', '.join(Global.metodos_validos)}")

        pago = pago_controller.crear(pedido, metodo)
        mostrar_mensaje("exito", "Pago registrado correctamente")

        limpiar_consola()
        print()
        print("         GENERAR COMPROBANTE")
        print("=" * 50)
        print()

        comprobante = None
        while comprobante is None:
            print("1. Boleta")
            print("2. Factura")
            print("3. Cancelar operación")
            print()
            op = input("Seleccione opción: ").strip()

            if op == "1":
                comprobante = boleta_controller.crear(pago)
                mostrar_mensaje("exito", f"Boleta generada: {comprobante.numero_comprobante}")

            elif op == "2":
                limpiar_consola()
                print()
                print("         DATOS DE FACTURA")
                print("=" * 50)
                print()

                ruc = input("Ingrese RUC (11 dígitos): ").strip()
                if not Validador.ruc(ruc):
                    mostrar_mensaje("error", "RUC inválido. Debe tener 11 dígitos")
                    continue

                razon_social = input("Ingrese razón social: ").strip()
                if not Validador.razon_social(razon_social):
                    mostrar_mensaje("error", "Razón social inválida. Debe tener entre 2 y 200 caracteres")
                    continue

                comprobante = factura_controller.crear(pago, ruc, razon_social)
                mostrar_mensaje("exito", f"Factura generada: {comprobante.numero_comprobante}")

            elif op == "3":
                mostrar_mensaje("info", "Operación cancelada")
                return

            else:
                mostrar_mensaje("error", "Opción inválida")

        pedidos_cola.completar_pedido()
        mostrar_mensaje("exito", "Pedido completado exitosamente")
        print()
        print(comprobante)

    except ValueError as ve:
        mostrar_mensaje("error", f"Error de validación: {str(ve)}")
    except Exception as error:
        mostrar_mensaje("error", f"Error al completar pedido: {str(error)}")

    print()
    input("Presiona cualquier tecla para continuar...")

def buscar_pedido():
    limpiar_consola()
    print("         BUSCAR PEDIDO")
    print("=" * 50)
    print()
    try:
        id_solicitado = input("ID del pedido a buscar: ")
        pedido = pedido_controller.buscar_id(id_solicitado)

        if pedido is None:
            mostrar_mensaje("error", f"No se encontró el pedido con ID: {id_solicitado}")
        elif type(pedido) is str:
            mostrar_mensaje("error", pedido)
        else:
            print("\nPedido encontrado:")
            print(pedido)
            print(f"\nDetalles del pedido:")
            print(f"  - Cliente: {pedido.cliente if pedido.cliente else 'Sin cliente'}")
            print(f"  - Empleado: {pedido.empleado.nombre if pedido.empleado else 'Sin empleado'}")
            print(f"  - Tipo: {pedido.tipo}")
            print(f"  - Estado: {pedido.estado}")
            print(f"  - Total: S/. {pedido.total:.2f}")
            print(f"  - Tiempo preparación: {pedido.tiempo_preparacion} min")
            print(f"  - Prioridad: {pedido.prioridad}")
            print(f"  - Cantidad de productos: {len(pedido.detalles)}")
    except Exception as error:
        mostrar_mensaje("error", f"Error al buscar: {str(error)}")

    print()
    input("Presiona cualquier tecla para continuar...")


def cancelar_pedido():
    limpiar_consola()
    print("         CANCELAR PEDIDO")
    print("=" * 50)
    mostrar_mensaje("info", "Se procederá a listar todos los pedidos, escribe el id del que desees cancelar")

    ver_pedidos()
    print("         PRÓXIMO PEDIDO EN COLA")
    print("=" * 50)
    print()
    try:
        pedido = pedidos_cola.cabeza
        if pedido is None:
            mostrar_mensaje("error", "No hay pedidos en cola")
            input("\nPresiona cualquier tecla para continuar...")
            return

        prueba_uno = pedir_confirmacion(f"¿Estás seguro de cancelar el pedido (I): {pedido}?")
        if not prueba_uno: return
        prueba_dos = pedir_confirmacion(f"¿Estás seguro de cancelar el pedido (II): {pedido}?")
        if not prueba_dos: return

        pedido = pedidos_cola.cancelar_pedido()
        if pedido:
            mostrar_mensaje("exito", "Pedido cancelado exitosamente")
    except Exception as error:
        mostrar_mensaje("error", f"Error al cancelar pedido: {str(error)}")

    print()
    input("Presiona cualquier tecla para continuar...")


def optimizar_cola():
    limpiar_consola()
    print("         OPTIMIZAR COLA")
    print("=" * 50)
    print()

    try:
        mostrar_mensaje("info", "Cola actual")
        pedidos_cola.mostrar_cola()
        input("Presiona cualquier tecla para la optimización...")
        prueba = pedir_confirmacion(
            "¿Desea optimizar la cola de pedidos?, eso modificará su orden y no será posible revertirlo")
        if not prueba: return
        mostrar_mensaje("advertencia",
                        "Se optimizará la cola buscando el mejor orden posible para maximizar rentabilidad acorde a los tiempos")
        pedidos_cola.JobSequence()
        mostrar_mensaje("info", "Cola optimizada correctamente")
        limpiar_consola()
        print()
        print("         COLA NUEVA")
        print("=" * 50)
        print()
        pedidos = pedidos_cola.mostrar_cola()
        for pedido in pedidos:
            print(str(pedido) + "\n")

    except Exception as error:
        mostrar_mensaje("error", str(error))

    print()
    input("Presiona cualquier tecla para continuar...")


def ver_pedidos():
    limpiar_consola()
    print("         PEDIDOS EN COLA")
    print("=" * 50)
    print()
    menu_comprobantes()
    print()
    input("Presiona cualquier tecla para continuar...")