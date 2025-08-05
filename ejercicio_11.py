def comparar_listas(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    comunes = set1 & set2
    solo_en_primera = set1 - set2
    solo_en_segunda = set2 - set1
    return comunes, solo_en_primera, solo_en_segunda
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

resultado = comparar_listas(lista1, lista2)

print("Elementos comunes:", resultado[0])
print("Solo en la primera lista:", resultado[1])
print("Solo en la segunda lista:", resultado[2])

