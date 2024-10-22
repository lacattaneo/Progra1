import random
from modulo_validaciones import validacionCategoria, validacionMeses, cantidadVentas
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
            
def guardar_matriz(matriz, categorias, meses):
    mi_ruta= "datos/"
    nombre_archivo = mi_ruta + "matriz.txt"
    
    try:
        with open(nombre_archivo, 'w') as archivo:
            # Escribir la primera fila (encabezado con los meses)
            encabezado = "\t".join(meses)
            archivo.write("Categoría/Mes\t" + encabezado + "\n")
            
            # Escribir cada fila de la matriz
            for i, categoria in enumerate(categorias):
                ventas = "\t".join(map(str, matriz[i]))  # Convertir cada valor a string
                archivo.write(f"{categoria}\t{ventas}\n")

        print(f"Matriz guardada correctamente en '{nombre_archivo}'.")

    except FileNotFoundError:
        print(f"No se encontró el archivo para guardar la matriz.")
    except Exception as e:
        print(f"Error al guardar la matriz: {e}")
