
# Calcular el promedio de ventas por categoría
def calcular_promedio(matriz):
    promedios = []
    for fila in matriz:
        total_ventas = sum(fila)
        promedio = total_ventas / len(fila)
        promedios.append(f"{promedio:.2f}")  # Formatear como cadena con 2 decimales
    return promedios

def imprimir_promedios(promedios, categorias):  # Calcular y mostrar el promedio de ventas por categoría
    print("\nPromedio de ventas por categoría:")
    for idx, promedio in enumerate(promedios):
        print(f"{categorias[idx]}: {promedio} juegos vendidos en promedio por mes.")
