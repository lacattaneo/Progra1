import random
from modulo_validaciones import validacionCategoria, validacionMeses, cantidadVentas
import os

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
        dias_disponibles = calendario.get(mes_seleccionado, {})

        print(f"Días disponibles en {mes_seleccionado}: {list(dias_disponibles.keys())}")
        dia = int(input(f"Seleccione el día del mes de {mes_seleccionado}: "))
        
        if dia not in dias_disponibles:
            print("Día no válido, por favor seleccione un día correcto.")
            continue

        # Selección y validación de la cantidad de juegos vendidos
        cantidad = cantidadVentas(int(input("Ingrese la cantidad de juegos vendidos: ")))

        # Actualizar la matriz de ventas mensuales con la cantidad ingresada
        matriz[cat_idx][mes_idx] += cantidad
        
        # Actualizar el calendario de ventas diarias
        actualizar_ventas(calendario, mes_seleccionado, dia, cantidad)
        
        # Guardar ambos archivos
        guardar_matriz(matriz, cate, mes)  # Guardar en ventas_mes.csv
        guardar_calendario("datos/", calendario)  # Guardar en ventas_diarias.csv
        
        print(f"Se ha actualizado la categoría {cate[cat_idx]} para el mes {mes[mes_idx]} y día {dia} con {cantidad} juegos vendidos.")
        print()

def guardar_matriz(matriz, categorias, mes):
    mi_ruta = "datos/"
    nombre_archivo = mi_ruta + "ventas_mes.csv"

    try:
        # Abrir el archivo en modo de añadir ('a')
        with open(nombre_archivo, 'a') as archivo:
            # Escribir las filas de la matriz al final del archivo
            for i in range(len(categorias)):
                archivo.write(f"{categorias[i]}\t" + "\t".join(map(str, matriz[i])) + "\n")

        print(f"Matriz guardada correctamente en '{nombre_archivo}'.")
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo o el directorio '{mi_ruta}'. Verifica que exista.")
    except IOError:
        print("Error al intentar guardar la matriz. Por favor, verifica los permisos o la ruta.")


def guardar_calendario(ruta_archivo, calendario):
    nombre_archivo = ruta_archivo + "ventas_diarias.csv"
    try:
        with open(nombre_archivo, 'a') as archivo:  # Abrir en modo 'a' para agregar
            # Escribir el encabezado solo si el archivo está vacío
            archivo.write("Mes\tDía\tVentas\n")
            
            # Escribir los datos del calendario
            for mes, dias in calendario.items():
                for dia, ventas in dias.items():
                    archivo.write(f"{mes}\t{dia}\t{ventas}\n")
        
        print(f"Calendario guardado exitosamente en {nombre_archivo}.")
    except FileNotFoundError:
        print(f"No se encontró el archivo para guardar el calendario.")
    except IOError:
        print("Error al intentar guardar el calendario. Por favor, verifica los permisos.")

def actualizar_ventas(calendario, mes, dia, cantidad):
    """Suma la cantidad de ventas al calendario evitando duplicados."""
    if mes in calendario and dia in calendario[mes]:
        calendario[mes][dia] += cantidad  # Sumar ventas si ya existe el día
    else:
        # Si no existe el mes o el día, inicializarlo
        if mes not in calendario:
            calendario[mes] = {}
        calendario[mes][dia] = cantidad

    # Mostrar el nuevo valor registrado
    print(f"Nuevas ventas registradas para {mes} {dia}: {calendario[mes][dia]}")

def cargar_matriz(categorias, meses):
    mi_ruta = "datos/"
    nombre_archivo = mi_ruta + "ventas_mes.csv"
    matriz = [[0] * len(meses) for _ in range(len(categorias))]  # Inicializa la matriz con las dimensiones correctas

    try:
        with open(nombre_archivo, 'r') as archivo:
            lines = archivo.readlines()
            
            # Verifica si hay líneas después del encabezado
            for i, line in enumerate(lines[1:]):  # Saltamos el encabezado
                # Evita que el índice se salga del rango
                if i < len(categorias):
                    values = line.strip().split("\t")[1:]  # Evitar la columna de categorías
                    # Asignar los valores de las ventas, convirtiendo a int
                    matriz[i] = [int(x) for x in values]
                else:
                    print(f"Advertencia: Línea extra en el archivo {nombre_archivo} en la posición {i+1}, no se asignará.")
            
        print(f"Matriz cargada correctamente desde '{nombre_archivo}'.")
    except FileNotFoundError:
        print(f"Archivo no encontrado. Inicializando la matriz con valores por defecto.")
    except IOError:
        print("Error al cargar la matriz")
    
    return matriz
