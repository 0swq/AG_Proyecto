from Controller.BoletaController import BoletaController
from Controller.DetallePedidoController import DetallePedidoController
from Controller.FacturaController import FacturaController
from Controller.ProductoController import ProductosController
from Utils.Confirmacion import pedir_confirmacion
from Utils.Limpiar import limpiar_consola
from Utils.Mensajes import mostrar_mensaje

productos_controller = ProductosController()
detalle_controller = DetallePedidoController()
factura_controller = FacturaController()
boleta_controller = BoletaController()


def menu_comprobantes():
    while True:
        limpiar_consola()
        print("\n--- Gestión de Pedidos completados y comprobantes de pago ---")
        print("1. Ver facturas / pedidos completados")
        print("2. Ver boletas / pedidos completados")
        print("3. Editar comprobantes")
        print("4. Volver")

        op = input("Seleccione opción: ")

        if op == "1":
            ver_facturas()
        elif op == "2":
            ver_boletas()
        elif op == "3":
            editar_comprobantes()
        elif op == "4":
            return
        else:
            mostrar_mensaje("error", "Opción inválida")


def ver_facturas():
    limpiar_consola()
    print("         FACTURAS ACTUALES")
    print("=" * 50)
    print()

    try:
        facturas = factura_controller.obtener_todos()
        facturas_list = [f for f in facturas if hasattr(f, 'ruc')]

        if not facturas_list:
            mostrar_mensaje("advertencia", "No hay facturas registradas")
            input("\nPresiona cualquier tecla para continuar...")
            return

        print(f"\n{'ID':<5} {'Número':<15} {'RUC':<15} {'Razón Social':<25} {'Total':<12} {'Fecha':<20}")
        print("-" * 100)
        for factura in facturas_list:
            fecha_str = factura.fecha_emision.strftime('%Y-%m-%d %H:%M')
            print(f"{factura.id:<5} {factura.numero_comprobante:<15} {factura.ruc:<15} "
                  f"{factura.razon_social:<25} S/. {factura.total:<8.2f} {fecha_str:<20}")

        print(f"\nTotal de facturas: {len(facturas_list)}")

        input("\nPresiona cualquier tecla para continuar...")
        prueba = pedir_confirmacion("¿Deseas inspeccionar alguna factura?")
        if not prueba:
            return

        id_factura = input("Ingresa el ID de la factura que desees inspeccionar: ")
        factura = factura_controller.buscar_id(id_factura)

        if type(factura) is str:
            mostrar_mensaje("error", factura)
            input("\nPresiona cualquier tecla para continuar...")
            return

        imprimir_factura_detallada(factura)

    except Exception as e:
        mostrar_mensaje("error", f"Error al listar facturas: {str(e)}")

    input("\nPresiona cualquier tecla para continuar...")


def ver_boletas():
    limpiar_consola()
    print("         BOLETAS ACTUALES")
    print("=" * 50)
    print()

    try:
        comprobantes = boleta_controller.obtener_todos()
        boletas_list = [b for b in comprobantes if not hasattr(b, 'ruc')]

        if not boletas_list:
            mostrar_mensaje("advertencia", "No hay boletas registradas")
            input("\nPresiona cualquier tecla para continuar...")
            return

        print(f"\n{'ID':<5} {'Número':<20} {'Cliente DNI':<15} {'Total':<12} {'Fecha':<20}")
        print("-" * 80)
        for boleta in boletas_list:
            fecha_str = boleta.fecha_emision.strftime('%Y-%m-%d %H:%M')
            cliente_dni = boleta.pago.pedido.cliente.dni if boleta.pago and boleta.pago.pedido and boleta.pago.pedido.cliente else "Sin cliente"
            print(f"{boleta.id:<5} {boleta.numero_comprobante:<20} {cliente_dni:<15} "
                  f"S/. {boleta.total:<8.2f} {fecha_str:<20}")

        print(f"\nTotal de boletas: {len(boletas_list)}")

        input("\nPresiona cualquier tecla para continuar...")
        prueba = pedir_confirmacion("¿Deseas inspeccionar alguna boleta?")
        if not prueba:
            return

        id_boleta = input("Ingresa el ID de la boleta que desees inspeccionar: ")
        boleta = boleta_controller.buscar_id(id_boleta)

        if type(boleta) is str:
            mostrar_mensaje("error", boleta)
            input("\nPresiona cualquier tecla para continuar...")
            return

        imprimir_boleta_detallada(boleta)

    except Exception as e:
        mostrar_mensaje("error", f"Error al listar boletas: {str(e)}")

    input("\nPresiona cualquier tecla para continuar...")


def imprimir_factura_detallada(factura):
    limpiar_consola()
    print()
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 30 + "FACTURA" + " " * 41 + "║")
    print("╠" + "═" * 78 + "╣")
    print(f"║ Número de Factura: {factura.numero_comprobante:<57} ║")
    print(f"║ Fecha de Emisión:  {factura.fecha_emision.strftime('%Y-%m-%d %H:%M:%S'):<57} ║")
    print("╠" + "═" * 78 + "╣")
    print("║" + " " * 25 + "DATOS DEL CLIENTE" + " " * 36 + "║")
    print("╠" + "═" * 78 + "╣")
    print(f"║ RUC:           {factura.ruc:<63} ║")
    print(f"║ Razón Social:  {factura.razon_social:<63} ║")
    print("╠" + "═" * 78 + "╣")
    print("║" + " " * 25 + "DETALLE DEL PEDIDO" + " " * 35 + "║")
    print("╠" + "═" * 78 + "╣")

    if factura.pago and factura.pago.pedido:
        pedido = factura.pago.pedido
        print(f"║ Pedido ID:     {pedido.id:<63} ║")
        cliente_dni = pedido.cliente.dni if pedido.cliente else "Sin cliente"
        print(f"║ Cliente DNI:   {cliente_dni:<63} ║")
        print(f"║ Tipo:          {pedido.tipo.capitalize():<63} ║")
        print(f"║ Empleado:      {pedido.empleado.nombre if pedido.empleado else 'Sin empleado':<63} ║")
        print("╠" + "═" * 78 + "╣")

        if pedido.detalles:
            print("║ PRODUCTOS:" + " " * 67 + "║")
            print("╠" + "─" * 78 + "╣")
            print(f"║ {'Producto':<35} {'Cant':<6} {'P.Unit':<12} {'Subtotal':<20} ║")
            print("╠" + "─" * 78 + "╣")

            for detalle in pedido.detalles:
                producto_nombre = detalle.producto.nombre[:33]
                precio_unit = detalle.producto.precio
                print(f"║ {producto_nombre:<35} {detalle.cantidad:<6} "
                      f"S/. {precio_unit:<8.2f} S/. {detalle.subtotal:<16.2f} ║")

    print("╠" + "═" * 78 + "╣")
    print("║" + " " * 25 + "INFORMACIÓN DE PAGO" + " " * 34 + "║")
    print("╠" + "═" * 78 + "╣")

    if factura.pago:
        print(f"║ Método de Pago:  {factura.pago.metodo.capitalize():<59} ║")
        print(f"║ Estado:          {factura.pago.estado.capitalize():<59} ║")

    print("╠" + "═" * 78 + "╣")
    print(f"║ {'TOTAL A PAGAR:':<58} S/. {factura.total:<15.2f} ║")
    print("╚" + "═" * 78 + "╝")
    print()


def imprimir_boleta_detallada(boleta):
    limpiar_consola()
    print()
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 30 + "BOLETA" + " " * 42 + "║")
    print("╠" + "═" * 78 + "╣")
    print(f"║ Número de Boleta: {boleta.numero_comprobante:<58} ║")
    print(f"║ Fecha de Emisión: {boleta.fecha_emision.strftime('%Y-%m-%d %H:%M:%S'):<58} ║")
    print("╠" + "═" * 78 + "╣")
    print("║" + " " * 25 + "DATOS DEL CLIENTE" + " " * 36 + "║")
    print("╠" + "═" * 78 + "╣")
    cliente_dni = boleta.pago.pedido.cliente.dni if boleta.pago and boleta.pago.pedido and boleta.pago.pedido.cliente else "Sin especificar"
    print(f"║ Cliente DNI: {cliente_dni:<64} ║")
    print("╠" + "═" * 78 + "╣")
    print("║" + " " * 25 + "DETALLE DEL PEDIDO" + " " * 35 + "║")
    print("╠" + "═" * 78 + "╣")

    if boleta.pago and boleta.pago.pedido:
        pedido = boleta.pago.pedido
        print(f"║ Pedido ID:     {pedido.id:<63} ║")
        print(f"║ Tipo:          {pedido.tipo.capitalize():<63} ║")
        print(f"║ Empleado:      {pedido.empleado.nombre if pedido.empleado else 'Sin empleado':<63} ║")
        print("╠" + "═" * 78 + "╣")

        if pedido.detalles:
            print("║ PRODUCTOS:" + " " * 67 + "║")
            print("╠" + "─" * 78 + "╣")
            print(f"║ {'Producto':<35} {'Cant':<6} {'P.Unit':<12} {'Subtotal':<20} ║")
            print("╠" + "─" * 78 + "╣")

            for detalle in pedido.detalles:
                producto_nombre = detalle.producto.nombre[:33]
                precio_unit = detalle.producto.precio
                print(f"║ {producto_nombre:<35} {detalle.cantidad:<6} "
                      f"S/. {precio_unit:<8.2f} S/. {detalle.subtotal:<16.2f} ║")

    print("╠" + "═" * 78 + "╣")
    print("║" + " " * 25 + "INFORMACIÓN DE PAGO" + " " * 34 + "║")
    print("╠" + "═" * 78 + "╣")

    if boleta.pago:
        print(f"║ Método de Pago:  {boleta.pago.metodo.capitalize():<59} ║")
        print(f"║ Estado:          {boleta.pago.estado.capitalize():<59} ║")

    print("╠" + "═" * 78 + "╣")
    print(f"║ {'TOTAL A PAGAR:':<58} S/. {boleta.total:<15.2f} ║")
    print("╚" + "═" * 78 + "╝")
    print()


def editar_comprobantes():
    limpiar_consola()
    print("         EDITAR COMPROBANTES")
    print("=" * 50)
    print()
    mostrar_mensaje("advertencia", "Funcionalidad en desarrollo")
    input("\nPresiona cualquier tecla para continuar...")