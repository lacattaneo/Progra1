import random
from modulo_validaciones import validacionCategoria, validacionMeses, cantidadVentas

abreviaturas_a_meses = {
    "ENE": "Enero", "FEB": "Febrero", "MAR": "Marzo", "ABR": "Abril",
    "MAY": "Mayo", "JUN": "Junio", "JUL": "Julio", "AGO": "Agosto",
    "SEP": "Septiembre", "OCT": "Octubre", "NOV": "Noviembre", "DIC": "Diciembre"
}

def agregar_venta(matriz, cate, mes, calendario):
    while True:
        print("Categorías disponibles:")
        for idx, categoria in enumerate(cate):
            print(f"{idx + 1}. {categoria}")

        # Selección y validación de la categoría
        cat_idx = validacionCategoria(int(input("Seleccione el número de la categoría (0 para salir): ")))
        
        # Si el usuario ingresa 0, se sale del bucle
        if cat_idx == 0:
            print("Finalizando la carga de ventas.")
            break

        cat_idx -= 1  # Ajustar el índice para usarlo en la matriz

        # Selección y validación del mes
        mes_idx = validacionMeses(int(input("Seleccione el número del mes (1-12): "))) - 1

        # Selección del día dentro del mes
        mes_seleccionado = abreviaturas_a_meses[mes[mes_idx]]
        dias_disponibles = calendario[mes_seleccionado]

        print(f"Días disponibles en {mes_seleccionado}: {list(dias_disponibles.keys())}")
        dia = int(input(f"Seleccione el día del mes de {mes_seleccionado}: "))
        
        if dia not in dias_disponibles:
            print("Día no válido, por favor seleccione un día correcto.")
            continue

        # Selección y validación de la cantidad de juegos vendidos
        cantidad = cantidadVentas(int(input("Ingrese la cantidad de juegos vendidos: ")))

        # Actualizar la matriz con la cantidad ingresada
        matriz[cat_idx][mes_idx] += cantidad
        
        # Actualizar el calendario utilizando la nueva función
        actualizar_ventas(calendario, mes_seleccionado, dia, cantidad)
        
        print(f"Se ha actualizado la categoría {cate[cat_idx]} para el mes {mes[mes_idx]} y día {dia} con {cantidad} juegos vendidos.")
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
    mi_ruta = "datos/"
    nombre_archivo = mi_ruta + "matriz.txt"
    
    try:
        with open(nombre_archivo, 'w') as archivo:  # Cambiar a modo de escritura para sobrescribir
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

def guardar_calendario(ruta_archivo, calendario):
    nombre_archivo = ruta_archivo + "ventas_diarias.txt"
    
    try:
        with open(nombre_archivo, 'a') as archivo:  # Cambiar a modo de anexar
            # Escribir el encabezado cada vez
            archivo.write("Mes\tDía\tVentas\n") 

            for mes, dias in calendario.items():
                for dia, ventas in dias.items():
                    archivo.write(f"{mes}\t{dia}\t{ventas}\n")
        
        print(f"Calendario guardado exitosamente en {nombre_archivo}.")
    
    except Exception as e:
        print(f"Error al guardar el calendario: {e}")

def actualizar_ventas(calendario, mes, dia, cantidad):
    """Suma la cantidad de ventas al calendario evitando duplicados."""
    if mes in calendario and dia in calendario[mes]:
        calendario[mes][dia] += cantidad
    else:
        # Si no existe el mes o el día, lo inicializamos
        if mes not in calendario:
            calendario[mes] = {}
        calendario[mes][dia] = cantidad

    # Muestra el nuevo valor registrado
    print(f"Nuevas ventas registradas para {mes} {dia}: {calendario[mes][dia]}")
