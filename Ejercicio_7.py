# Sistema que permite gestionar una lista de compras

def mostrar_menu():
    """
    Muestra el menú principal de opciones al usuario.
    """
    print("\n MENÚ DE LISTA DE COMPRAS")
    print("1. Ingresa un producto")
    print("2. Elimina un producto")
    print("3. Ver lista completa")
    print("4. Salir")

def agregar_item(lista):
    """
    Solicita al usuario que ingrese un producto y lo agrega a la lista.
    :param lista: lista de compras a modificar
    """
    item = input("Ingrese un producto: ")
    lista.append(item)
    print(f" El producto '{item}' ha sido agregado a la lista de compras.")

def eliminar_item(lista):
    """
    Solicita al usuario que ingrese un producto y lo elimina de la lista si existe.
    :param lista: lista de compras a modificar
    """
    item = input("Ingrese un producto a eliminar: ")
    if item in lista:
        lista.remove(item)
        print(f" El producto '{item}' ha sido eliminado de la lista.")
    else:
        print(f" El producto '{item}' no se encuentra en la lista.")

def ver_lista(lista):
    """
    Muestra la lista de compras completa.
    :param lista: lista de compras a mostrar
    """
    if lista:
        print("\n Lista de compras:")
        for i, item in enumerate(lista, start=1):
            print(f"{i}. {item}")
    else:
        print(" La lista de compras está vacía.")

def main():
    """
    Función principal que ejecuta el menú y gestiona la lista de compras.
    """
    lista_compras = []

    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            agregar_item(lista_compras)
        elif opcion == "2":
            eliminar_item(lista_compras)
        elif opcion == "3":
            ver_lista(lista_compras)
        elif opcion == "4":
            print("Haz terminado de agregar productos a la lita de compras.")
            break
        else:
            print("Opción no válida. Por favor, elija entre 1 y 4.")
