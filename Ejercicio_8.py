def consulta_palindromo(frase):
 '''
 Muestra la agenda
 '''
 frase= frase.replace(" ", "").lower()
 invertida = frase[::-1]
 if frase == invertida:
    return True
 else:
    return False

frase = input(str("Ingrese una frase: "))
print(consulta_palindromo(frase))