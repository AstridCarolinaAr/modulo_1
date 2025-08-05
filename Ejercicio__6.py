# Definición de la función
def analizar_calificaciones(calificaciones):
    promedio = sum(calificaciones) / len(calificaciones)
    mayor = max(calificaciones)
    menor = min(calificaciones)
    return (promedio, mayor, menor)  # Se retorna como una tupla

# Lista de calificaciones de ejemplo
notas = [3.5, 4.2, 2.8, 5.0, 4.8]

# Llamar la función y guardar el resultado
resultado = analizar_calificaciones(notas)

# Mostrar los resultados
print("Resultados del análisis de calificaciones:")
print(f"Promedio: {resultado[0]:.2f}")
print(f"Nota más alta: {resultado[1]}")
print(f"Nota más baja: {resultado[2]}")
