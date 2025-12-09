from Controller.ProductoController import ProductosController
from Utils.Limpiar import limpiar_consola
from Utils.Mensajes import mostrar_mensaje
from Utils.Confirmacion import pedir_confirmacion

producto_controller = ProductosController()


def menu_productos():
    while True:
        limpiar_consola()
        print("\n--- Gestión de Productos ---")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Buscar producto")
        print("4. Editar producto")
        print("5. Eliminar producto")
        print("6. Volver")

        op = input("Seleccione opción: ")

        if op == "1":
            registrar_producto()
        elif op == "2":
            listar_productos()
        elif op == "3":
            buscar_producto()
        elif op == "4":
            editar_producto()
        elif op == "5":
            eliminar_producto()
        elif op == "6":
            return
        else:
            mostrar_mensaje("error", "Opción inválida")


def registrar_producto():
    limpiar_consola()
    print("         REGISTRAR NUEVO PRODUCTO")
    print("=" * 50)
    print()

    try:
        print("Ingrese los datos del producto:")
        print("-" * 50)
        nombre = input("Nombre: ").strip()
        print("Categorías: entrada, plato_principal, postre, bebida")
        categoria = input("Categoría: ").strip()
        precio = input("Precio: ").strip()
        costo = input("Costo: ").strip()
        tiempo_preparacion = input("Tiempo de preparación (minutos): ").strip()

        resultado = producto_controller.crear(nombre, categoria, precio, costo, tiempo_preparacion)
        if type(resultado) is str:
            mostrar_mensaje("error", f"✗ No se pudo registrar el producto, motivo: {resultado}")
        else:
            mostrar_mensaje("exito", "Producto registrado exitosamente")
    except Exception as error:
        mostrar_mensaje("error", f"Error inesperado: {str(error)}")

    print()
    input("Presiona cualquier tecla para continuar...")


def listar_productos():
    limpiar_consola()
    print("         LISTA DE PRODUCTOS")
    print("=" * 50)
    print()
    try:
        productos = producto_controller.obtener_todos()

        if not productos:
            mostrar_mensaje("advertencia", "No hay productos registrados")
        else:
            print(
                f"\n{'ID':<5} {'Nombre':<25} {'Categoría':<18} {'Precio':<10} {'Costo':<10} {'Prep(min)':<10} {'Rent.':<10}")
            print("-" * 100)
            for producto in productos:
                print(f"{producto.id:<5} {producto.nombre:<25} {producto.categoria:<18} "
                      f"{producto.precio:<10.2f} {producto.costo:<10.2f} "
                      f"{producto.tiempo_preparacion:<10} {producto.rentabilidad:<10.2f}")
            print(f"\nTotal de productos: {len(productos)}")
    except Exception as e:
        mostrar_mensaje("error", f"Error al listar productos: {str(e)}")

    print()
    input("Presiona cualquier tecla para continuar...")


def buscar_producto():
    limpiar_consola()
    print("         BUSCAR PRODUCTO")
    print("=" * 50)
    print()
    try:
        id_solicitado = input("ID del producto a buscar: ")
        producto = producto_controller.buscar_id(id_solicitado)

        if producto is None:
            mostrar_mensaje("error", f"No se encontró el producto con ID: {id_solicitado}")
        elif type(producto) is str:
            mostrar_mensaje("error", producto)
        else:
            print("\nProducto encontrado:")
            print(producto)
    except Exception as error:
        mostrar_mensaje("error", f"Error al buscar: {str(error)}")

    print()
    input("Presiona cualquier tecla para continuar...")


def editar_producto():
    limpiar_consola()
    print("         EDITAR PRODUCTO")
    print("=" * 50)
    print()
    mostrar_mensaje("info",
                    f"Se procedera a listar todos los productos registrados, escribe el id del que desees editar")

    listar_productos()
    print("         ESCRIBE EL ID DE UN PRODUCTO PARA EDITARLO")
    print("=" * 50)
    print()
    try:
        id_solicitado = input("ID que se desea editar: ")
        producto = producto_controller.buscar_id(id_solicitado)

        if producto is None:
            mostrar_mensaje("error", f"No se encontró el producto con ID: {id_solicitado}")
            input("\nPresiona cualquier tecla para continuar...")
            return

        if type(producto) is str:
            mostrar_mensaje("error", producto)
            input("\nPresiona cualquier tecla para continuar...")
            return

        limpiar_consola()
        print("==> Producto seleccionado ==>")
        print(producto)
        print()
        print("=" * 50)
        print()
        mostrar_mensaje("info", "Deja en blanco los atributos que no quieras modificar")
        nombre = input("Nombre: ").strip()
        print("Categorías: entrada, plato_principal, postre, bebida")
        categoria = input("Categoría: ").strip()
        precio = input("Precio: ").strip()
        costo = input("Costo: ").strip()
        tiempo_preparacion = input("Tiempo de preparación (minutos): ").strip()

        resultado = producto_controller.actualizar(
            id_solicitado,
            nombre if nombre else None,
            categoria if categoria else None,
            precio if precio else None,
            costo if costo else None,
            tiempo_preparacion if tiempo_preparacion else None
        )
        if type(resultado) is str:
            mostrar_mensaje("error", resultado)
        else:
            mostrar_mensaje("exito", "Actualizado correctamente")
    except Exception as error:
        mostrar_mensaje("error", f"Error al editar: {str(error)}")

    print()
    input("Presiona cualquier tecla para continuar...")


def eliminar_producto():
    limpiar_consola()
    print("         ELIMINAR PRODUCTO")
    print("=" * 50)
    mostrar_mensaje("info",
                    f"Se procedera a listar todos los productos registrados, escribe el id del que desees eliminar")

    listar_productos()
    print("         ESCRIBE EL ID DE UN PRODUCTO PARA ELIMINARLO")
    print("=" * 50)
    print()
    try:
        id_solicitado = input("ID que se desea eliminar: ")
        producto = producto_controller.buscar_id(id_solicitado)

        if producto is None:
            mostrar_mensaje("error", f"No se encontró el producto con ID: {id_solicitado}")
            input("\nPresiona cualquier tecla para continuar...")
            return

        if type(producto) is str:
            mostrar_mensaje("error", producto)
            input("\nPresiona cualquier tecla para continuar...")
            return

        prueba_uno = pedir_confirmacion(f"Estas realmente seguro de eliminar el producto (I): {producto}")
        if not prueba_uno: return
        prueba_dos = pedir_confirmacion(f"Estas realmente seguro de eliminar el producto (II): {producto}")
        if not prueba_dos: return
        prueba_tres = pedir_confirmacion(f"Estas realmente seguro de eliminar el producto (III): {producto}")
        if not prueba_tres: return

        resultado = producto_controller.eliminar(id_solicitado)
        if type(resultado) is str:
            mostrar_mensaje("error", resultado)
        else:
            mostrar_mensaje("exito", "Producto eliminado exitosamente")
    except Exception as error:
        mostrar_mensaje("error", f"Error al eliminar: {str(error)}")

    print()
    input("Presiona cualquier tecla para continuar...")