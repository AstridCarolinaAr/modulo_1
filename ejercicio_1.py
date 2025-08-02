"""Este codigo calcula el Índice de Masa Corporal (IMC) de una persona.

Solicita al usuario su peso en kilogramos y su altura en metros,
y luego calcula y muestra su IMC.
"""
def evaluar_imc(imc):
  """
    este nos ayuda a evaluar el imc de la persona
    """
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)
print(f"Su IMC es: {imc:.2f}")