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
        print("3. Volver")

        op = input("Seleccione opción: ")

        if op == "1":
            ver_facturas()
        elif op == "2":
            ver_boletas()
        elif op == "3":
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
    print("\n" + "=" * 80)
    print("                              FACTURA")
    print("=" * 80)
    print(f"\nNúmero de Factura: {factura.numero_comprobante}")
    print(f"Fecha de Emisión:  {factura.fecha_emision.strftime('%Y-%m-%d %H:%M:%S')}")

    print("\n--- DATOS DEL CLIENTE ---")
    print(f"RUC:           {factura.ruc}")
    print(f"Razón Social:  {factura.razon_social}")

    if factura.pago and factura.pago.pedido:
        pedido = factura.pago.pedido
        print("\n--- DETALLE DEL PEDIDO ---")
        print(f"Pedido ID:     {pedido.id}")
        cliente_dni = pedido.cliente.dni if pedido.cliente else "Sin cliente"
        print(f"Cliente DNI:   {cliente_dni}")
        print(f"Tipo:          {pedido.tipo.capitalize()}")
        print(f"Empleado:      {pedido.empleado.nombre if pedido.empleado else 'Sin empleado'}")

        if pedido.detalles:
            print("\n--- PRODUCTOS ---")
            for detalle in pedido.detalles:
                producto_nombre = detalle.producto.nombre
                precio_unit = detalle.producto.precio
                print(f"  • {producto_nombre} - Cantidad: {detalle.cantidad} - "
                      f"Precio: S/. {precio_unit:.2f} - Subtotal: S/. {detalle.subtotal:.2f}")

    print("\n--- INFORMACIÓN DE PAGO ---")
    if factura.pago:
        print(f"Método de Pago:  {factura.pago.metodo.capitalize()}")
        print(f"Estado:          {factura.pago.estado.capitalize()}")

    print(f"\nTOTAL A PAGAR: S/. {factura.total:.2f}")
    print("=" * 80 + "\n")


def imprimir_boleta_detallada(boleta):
    limpiar_consola()
    print("\n" + "=" * 80)
    print("                              BOLETA")
    print("=" * 80)
    print(f"\nNúmero de Boleta: {boleta.numero_comprobante}")
    print(f"Fecha de Emisión: {boleta.fecha_emision.strftime('%Y-%m-%d %H:%M:%S')}")

    print("\n--- DATOS DEL CLIENTE ---")
    cliente_dni = boleta.pago.pedido.cliente.dni if boleta.pago and boleta.pago.pedido and boleta.pago.pedido.cliente else "Sin especificar"
    print(f"Cliente DNI: {cliente_dni}")

    if boleta.pago and boleta.pago.pedido:
        pedido = boleta.pago.pedido
        print("\n--- DETALLE DEL PEDIDO ---")
        print(f"Pedido ID:     {pedido.id}")
        print(f"Tipo:          {pedido.tipo.capitalize()}")
        print(f"Empleado:      {pedido.empleado.nombre if pedido.empleado else 'Sin empleado'}")

        if pedido.detalles:
            print("\n--- PRODUCTOS ---")
            for detalle in pedido.detalles:
                producto_nombre = detalle.producto.nombre
                precio_unit = detalle.producto.precio
                print(f"  • {producto_nombre} - Cantidad: {detalle.cantidad} - "
                      f"Precio: S/. {precio_unit:.2f} - Subtotal: S/. {detalle.subtotal:.2f}")

    print("\n--- INFORMACIÓN DE PAGO ---")
    if boleta.pago:
        print(f"Método de Pago:  {boleta.pago.metodo.capitalize()}")
        print(f"Estado:          {boleta.pago.estado.capitalize()}")

    print(f"\nTOTAL A PAGAR: S/. {boleta.total:.2f}")
    print("=" * 80 + "\n")

def editar_comprobantes():
    limpiar_consola()
    print("         EDITAR COMPROBANTES")
    print("=" * 50)
    print()
    mostrar_mensaje("advertencia", "Funcionalidad en desarrollo")
    input("\nPresiona cualquier tecla para continuar...")

from Utils.Limpiar import limpiar_consola

