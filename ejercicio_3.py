#contador de vocales y consonantes
vocales = 0
consonantes = 0
palabra = input("Ingrese una palabra: ")
palabra =palabra.replace(" ","").lower()

for letra in palabra:
    if letra.lower() in "aeiou":
        vocales += 1
    elif letra.isalpha():
        consonantes += 1

print(f"La palabra {palabra}\n tiene {vocales} vocales\n {consonantes} consonantes.")