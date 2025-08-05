#tabla de multiplicar
num = int(input("Ingrese un numero: "))
'''
estamos utulizando la funcion range que nos permite crear una secuencia de numeros
el primero es donde empieza y el segundo es donde termina y asi vamos a imprimir la tabla de multiplciar 
dependiendo del numero infgresado
'''
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
