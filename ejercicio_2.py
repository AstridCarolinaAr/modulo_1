# verficador de mayor de edad

def verificar_edad(edad):
    """
    Esta funcion verifica si la persona es mayor de edad
    """
    if edad > 18:
        print("Usted es mayor de edad")
    elif edad < 18:
        print("Usted es menor de edad")
    else:
        print("Dato inválido")

    if 18 <= edad <= 25:
        print("Usted es joven adulto")

# se llama a la funcion
edad = int(input(f"Ingrese su edad: "))
verificar_edad(edad)


