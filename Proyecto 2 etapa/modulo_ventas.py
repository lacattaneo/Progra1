import random

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
        mes_idx = validacionMeses(mes_idx + 1) - 1  

        cantidad = int(input("Ingrese la cantidad de juegos vendidos: "))
        cantidad = cantidadVentas(cantidad)

        # Actualizar la matriz con la cantidad ingresada
        matriz[cat_idx][mes_idx] += cantidad
        print(f"Se ha actualizado la categoría {cate[cat_idx]} para el mes {mes[mes_idx]} con {cantidad} juegos vendidos.")
        print()


def agregar_promociones(matriz, cate, mes):
    promocion = 0
    detalles_promociones = []  # Lista para almacenar detalles de cada promoción
    
    for i in range(len(cate)):  
        for j in range(len(mes)):
            cantidad = random.randint(0, 2) 
            matriz[i][j] += cantidad
            
            if cantidad > 0:
                promocion += 1
                detalles_promociones.append(f"{cate[i]}: {cantidad} promociones en {mes[j]}")
    
    print(" ")
    print(f"Se realizaron {promocion} promociones.")
    
    # Imprimir los detalles de cada promoción
    if detalles_promociones:
        print("Detalles de las promociones:")
        for detalle in detalles_promociones:
            print(detalle)
