import random
from modulo import validacionCategoria, validacionMeses, cantidadVentas

def matriz():  # Función para crear la matriz
    categorias = 10
    meses = 12
    matriz = [[0]*meses for i in range(categorias)]
    return matriz

def imprimir_matriz(matriz, cate, mes):  # Función para imprimir la matriz
    canCate = len(matriz)
    cantMeses = len(matriz[0])
    print("     ", end="   ")
    for i in range(12):
        print("%3s" % (mes[i]), end=" ")
    print()

    for f in range(canCate):
        print("%6s" % (cate[f]), end=" ")
        for c in range(cantMeses):
            print("%3d" % matriz[f][c], end=" ")
        print()

def agregar_venta(matriz, cate, mes):
    while True:
        print("Categorías disponibles:")
        for idx, categoria in enumerate(cate):
            print(f"{idx + 1}. {categoria}")

        cat_idx = int(input("Seleccione el número de la categoría (0 para salir): ")) - 1
        cat_idx = validacionCategoria(cat_idx + 1) - 1 
        
        # Si el usuario ingresa 0, se sale del bucle
        if cat_idx == -1:
            print("Finalizando la carga de ventas.")
            break

        mes_idx = int(input("Seleccione el número del mes (1-12): ")) - 1
        mes_idx = validacionMeses(mes_idx + 1) - 1  # Ajusta para que devuelva el índice correcto (0-11)

        cantidad = int(input("Ingrese la cantidad de juegos vendidos: "))
        cantidad = cantidadVentas(cantidad)

        # Actualizar la matriz con la cantidad ingresada
        matriz[cat_idx][mes_idx] += cantidad
        print(f"Se ha actualizado la categoría {cate[cat_idx]} para el mes {mes[mes_idx]} con {cantidad} juegos vendidos.")
        print()

# Función para calcular el promedio de ventas por categoría (enfoque básico)
def calcular_promedio(matriz):
    promedios = []
    for fila in matriz:
        total_ventas = sum(fila)  # Sumar todas las ventas en la fila (categoría)
        promedio = total_ventas // len(fila)  # Calcular el promedio dividiendo por la cantidad de meses
        promedios.append(promedio)  # Guardar el promedio en la lista
    return promedios

# Nueva función para agregar ventas aleatorias usando random
def agregar_ventas_random(matriz, cate, mes):
    for i in range(len(cate)):  # Itera sobre cada categoría
        for j in range(len(mes)):  # Itera sobre cada mes
            cantidad = random.randint(0, 5)  # Genera una cantidad aleatoria de ventas (0 a 100)
            matriz[i][j] += cantidad  # Actualiza la matriz
    print("Ventas aleatorias agregadas exitosamente.")

# Main
m = matriz()
categorias = ["Accion", "Aventu", "RolRPG", "Deport", "Carrer", "Estrat", "Simula", "Puzzle", "Terror", "MulMMO"]
meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]

# Llamar a la función para agregar juegos aleatoriamente
agregar_venta(m, categorias, meses)
agregar_ventas_random(m, categorias, meses)

# Imprimir la matriz actualizada
imprimir_matriz(m, categorias, meses)

# Calcular y mostrar el promedio de ventas por categoría
promedios = calcular_promedio(m)
print("\nPromedio de ventas por categoría:")
for idx, promedio in enumerate(promedios):
    print(f"{categorias[idx]}: {promedio} juegos vendidos en promedio por mes.")

