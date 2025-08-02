# adivina el numero secreto segun el numero ingresado en una serie de 5 intentos
import random
num = random.randint(1, 100)
intentos = 0
while intentos < 5:
    intento = int(input("Ingrese un numero: "))
    intentos += 1
    if intento == num:
        print("Adivinaste el numero secreto.")
        break
    elif intento < num:
        print("El numero secreto es mayor.")
    else:
        print("El numero secreto es menor.")

if intentos == 5:
    print("No adivinaste el numero secreto, el numero era:", {num})