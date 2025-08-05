# Diccionario con factores de conversión entre unidades
conversiones = {
    "metros_a_pies": 3.28084,
    "pies_a_metros": 1 / 3.28084,
    "kilometros_a_millas": 0.621371,
    "millas_a_kilometros": 1 / 0.621371,
    "gramos_a_libras": 0.00220462,
    "libras_a_gramos": 1 / 0.00220462,
    "litros_a_galones": 0.264172,
    "galones_a_litros": 1 / 0.264172
}


def convertir(cantidad, unidad_origen, unidad_destino):
    """
    Convierte una cantidad de una unidad de origen a una unidad de destino,
    si la conversión existe en el diccionario.

    :param cantidad: número (float) a convertir
    :param unidad_origen: unidad desde la que se desea convertir (str)
    :param unidad_destino: unidad a la que se desea convertir (str)
    :return: cantidad convertida o mensaje de error
    """
    clave = f"{unidad_origen}a{unidad_destino}"
    if clave in conversiones:
        factor = conversiones[clave]
        resultado = cantidad * factor
        return resultado
    else:
        return None
def mostrar_unidades_disponibles():
    print("\nUnidades disponibles:")
    unidades = set()
    for clave in conversiones.keys():
        origen, destino = clave.partition('_a')
        unidades.add(origen)
        unidades.add(destino)
    print(", ".join(sorted(unidades)))


# Programa principal
def main():
    print("Bienvenido al conversor de unidades ")
    mostrar_unidades_disponibles()

    while True:
        try:
            cantidad = float(input("\nIngresa la cantidad a convertir: "))
            unidad_origen = input("Unidad de origen: ").lower()
            unidad_destino = input("Unidad de destino: ").lower()

            resultado = convertir(cantidad, unidad_origen, unidad_destino)

            if resultado is not None:
                print(f"\n Resultado: {cantidad} {unidad_origen} = {resultado:.4f} {unidad_destino}")
            else:
                print("\n Conversión no disponible. Revisa las unidades.")

            opcion = input("\n¿Deseas hacer otra conversión? (y/n): ").lower()
            if opcion != "s":
                print("Gracias por usar el conversor. ¡Hasta luego! ")
                break
        except ValueError:
            print(" Error: Ingresa una cantidad válida (número).")