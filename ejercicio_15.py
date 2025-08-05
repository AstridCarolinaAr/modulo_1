def calcular_promedio(calificaciones):
    '''
    Calcula el promedio de una lista de calificaciones.

    Parámetros:
    calificaciones (list): Lista de números (floats o ints).

    Retorna:
    float: Promedio de las calificaciones.
    '''
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)
def obtener_estado(promedio):
    '''
    Determina si el estudiante está aprobado o reprobado.

    Parámetros:
    promedio (float): Promedio de calificaciones del estudiante.

    Retorna:
    str: "Aprobado" si el promedio >= 3.0, de lo contrario "Reprobado".
    '''
    if promedio >= 3.0:
        return "Aprobado"
    else:
        return "Reprobado"
def generar_reporte(estudiantes):
    '''
    Genera e imprime un reporte de calificaciones con promedio y estado.

    Parámetros:
    estudiantes (dict): Diccionario con nombres como claves y listas de
                        calificaciones como valores.

    Retorna:
    None
    '''
    print("\nReporte de Calificaciones:")
    print("-" * 30)
    for nombre, notas in estudiantes.items():
        promedio = calcular_promedio(notas)
        estado = obtener_estado(promedio)
        print(f"- Estudiante: {nombre}, Promedio: {promedio:.2f}, Estado: {estado}")
    print("-" * 30)
estudiantes = {}
cantidad = int(input("¿Cuántos estudiantes vas a ingresar? "))
for _ in range(cantidad):
    nombre = input("\nNombre del estudiante: ")
    notas_input = input("Ingresa las calificaciones separadas por comas (ej: 3.5,4.0,2.8): ")
    notas = [float(nota.strip()) for nota in notas_input.split(",") if nota.strip()]
    estudiantes[nombre] = notas
generar_reporte(estudiantes)
