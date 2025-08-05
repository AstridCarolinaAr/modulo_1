def consultar_saldo(saldo):
    """
    Muestra el saldo actual.
    :param saldo: Saldo actual del usuario.
    :return: None
    """
    print(f"\nTu saldo actual es: ${saldo:.2f}")


def depositar(saldo):
    """
    Solicita al usuario un monto a depositar y lo agrega al saldo.
    :param saldo: Saldo actual del usuario.
    :return: Nuevo saldo actualizado.
    """
    try:
        monto = float(input("Ingrese el monto a depositar: $"))
        if monto <= 0:
            print("El monto debe ser mayor que cero.")
        else:
            saldo += monto
            print(f"Has depositado ${monto:.2f}.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
    return saldo


def retirar(saldo):
    """
    Solicita un monto a retirar y lo descuenta del saldo si es válido.
    :param saldo: Saldo actual del usuario.
    :return: Nuevo saldo actualizado.
    """
    try:
        monto = float(input("Ingrese el monto a retirar: $"))
        if monto <= 0:
            print("El monto debe ser mayor que cero.")
        elif monto > saldo:
            print("No tienes suficiente saldo para esta operación.")
        else:
            saldo -= monto
            print(f"Has retirado ${monto:.2f}.")
    except ValueError:
        print("Por favor, ingrese un número válido.")
    return saldo


def mostrar_menu():
    """
    Muestra las opciones disponibles en el cajero.
    """
    print("\n--- Cajero Automático ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")


def main():
    """
    Función principal que ejecuta el programa.
    """
    saldo = 0.0

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            consultar_saldo(saldo)
        elif opcion == "2":
            saldo = depositar(saldo)
        elif opcion == "3":
            saldo = retirar(saldo)
        elif opcion == "4":
            print("Gracias por usar el cajero. Hasta luego.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if _name_ == "_main_":
    main()