# verficador de mayor de edad
edad = int(input("Ingrese su edad: "))
def evaluar_edad(edad):
    """
    vamos a evaluar si la persona es mayor de edad usando un if
      if: para evaluar si la persona es mayor de edad
        else: para evaluar si la persona es menor de edad ya que si la primera condicion no se cumple
        va entrar a la segunda condicion y se imprime que la persona es menor de edad
    :param edad:
    :return:
       devuelve el valor de la edad
    """
if edad >= 18:

    print("Usted es mayor de edad.")
else:
    print("Usted es menor de edad.")