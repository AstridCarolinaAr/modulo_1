# Inventario inicial vacío
inventario = []
def agregar_producto():
    """
    Agrega un nuevo producto al inventario.
    Solicita nombre, precio y cantidad.
    """
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado exitosamente.\n")
def realizar_venta():
    """
    Realiza una venta actualizando la cantidad de un producto.
    """
    nombre = input("Ingrese el nombre del producto que desea vender: ")
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            cantidad_vender = int(input("Ingrese la cantidad que desea vender: "))
            if cantidad_vender <= producto["cantidad"]:
                producto["cantidad"] -= cantidad_vender
                print(f"Venta realizada. Quedan {producto['cantidad']} unidades de '{producto['nombre']}'.\n")
            else:
                print("No hay suficiente cantidad disponible.\n")
            return
    print("Producto no encontrado en el inventario.\n")
def mostrar_inventario():
    """
    Muestra todos los productos del inventario.
    """
    if not inventario:
        print("El inventario está vacío.\n")
    else:
        print("Inventario ")
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: ${producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}\n")
def mostrar_menu():
    """
    Muestra el menú principal e interactúa con el usuario.
    """
    while True:
        print(" MENÚ PRINCIPAL ")
        print("1. Agregar producto")
        print("2. Realizar venta")
        print("3. Mostrar inventario")
        print("4. Salir")

        opcion = input("opcion_1:para agregar producto,\nopcion_2:para realizar venta, \nopcion_3:para mostrar inventario,\nopcion_4:para salir\nSeleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            realizar_venta()
        elif opcion == "3":
            mostrar_inventario()
        elif opcion == "4":
            print("gracias por usar el programa")
            break
        else:
            print("Opción inválida")
mostrar_menu()
