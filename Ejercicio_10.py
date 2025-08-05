def contar_letras(texto):
    """
    Función que recibe un texto y devuelve un diccionario con la frecuencia
    de cada letra, sin distinguir mayúsculas y sin contar espacios.
    """
    frecuencias = {}
    texto = texto.lower()
    for letra in texto:
        if letra.isalpha():
            frecuencias[letra] = frecuencias.get(letra, 0) + 1

    return frecuencias

#pedimos los datos o frase al usuario
entrada = input("Ingrese un texto: ")
resultado = contar_letras(entrada)

#imprime el diccionario y las letras con cantidad
print("Frecuencia de letras:")
for letra, cantidad in resultado.items():
    print(f"{letra}: {cantidad}")