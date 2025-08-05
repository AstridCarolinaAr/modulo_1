agenda = {
    "Laura": "3111234567",
    "Carlos": "3009876543",
    "Juan": "3104567890"
}
def seleccion_1():
    '''
    Agrega un contacto a la agenda
    '''
    global agenda
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el numero del contacto: ")
    agenda[nombre] = numero
    print(f"El contacto {nombre} ha sido agregado a la agenda")
def seleccion_2(agenda):
    '''
    Busca contacto por el nombre
    '''
    nombre = input("Ingrese el nombre del contacto: ")
    if nombre in agenda:
        print(f"El contacto {nombre} tiene el numero {agenda[nombre]}")
    else:
        print(f"El contacto {nombre} no esta en la agenda")
def seleccion_3(agenda):
    '''
    Muestra la agenda
    '''
    for nombre, numero in agenda.items():
        print(f"{nombre}: {numero}")
opcion = int(input("1 :Añadir Contacto\n2 :Buscar contacto por el nombre Contacto\n3 :Mostrar todos los contactos\n4 :Salir\n ingrese la opcion que deese realizar: "))
while opcion != 4:
     if opcion == 1:
       seleccion_1()
     elif opcion == 2:
         seleccion_2(agenda)
     elif opcion == 3:
         seleccion_3(agenda)
     elif opcion == 4:
         print("Gracias por usar el programa")
     else:
         print("Opcion no valida")

     opcion = int(input("\n1 :Añadir Contacto\n2 :Buscar contacto por el nombre Contacto\n3 :Mostrar todos los contactos\n4 :Salir\n ingrese la opcion que deese realizar: "))
