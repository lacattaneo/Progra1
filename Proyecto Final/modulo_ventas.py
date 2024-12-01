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
        guardar_matriz(matriz, cate, mes[mes_idx])  # Guardar en ventas_mes.csv
        guardar_calendario("datos/", calendario)  # Guardar en ventas_diarias.csv
        
        print(f"Se ha actualizado la categoría {cate[cat_idx]} para el mes {mes[mes_idx]} y día {dia} con {cantidad} juegos vendidos.")
        print()

def guardar_matriz(matriz, categorias, meses):
    mi_ruta = "datos/"
    nombre_archivo = mi_ruta + "ventas_mes.csv"

    try:
        datos_existentes = {}
        try:
            # Cambié a 'utf-8-sig' para manejar el BOM o 'latin1' en caso de que no sea UTF-8 puro
            with open(nombre_archivo, 'r', encoding='utf-8-sig') as archivo:
                lineas = archivo.readlines()

                for linea in lineas:
                    partes = linea.strip().split(",")  # Usar coma para dividir
                    if len(partes) < 2:  # Saltar líneas sin suficientes datos
                        continue
                    categoria = partes[0]
                    if categoria in categorias:
                        categoria_idx = categorias.index(categoria)
                        ventas_actualizadas = partes[1:]

                        if len(ventas_actualizadas) == len(meses):
                            # Actualizamos la matriz con las ventas correspondientes
                            matriz[categoria_idx] = [int(x) for x in ventas_actualizadas]
                        else:
                            print(f"Advertencia: Las ventas para {categoria} no coinciden con el número de meses.")
        except FileNotFoundError:
            print(f"Archivo no encontrado. Se creará uno nuevo en '{nombre_archivo}'.")

        # Escribir los datos actualizados de la matriz en el archivo, sin modificar la cabecera
        with open(nombre_archivo, 'w', encoding='utf-8-sig') as archivo:
            # Mantener la cabecera original intacta
            archivo.write("Categoría/Mes" + "," + ",".join(meses) + "\n")  # Usar coma como delimitador
            
            # Escribir las ventas actualizadas para cada categoría
            for i, categoria in enumerate(categorias):
                archivo.write(categoria + "," + ",".join(map(str, matriz[i])) + "\n")  # Usar coma como delimitador

        print(f"Matriz actualizada correctamente en '{nombre_archivo}'.")

    except FileNotFoundError:
        print(f"No se encontró el archivo: {nombre_archivo}. Por favor, verifica la ruta.")
    except IOError:
        print(f"Se produjo un error al intentar acceder o modificar el archivo: {nombre_archivo}.")

def guardar_calendario(ruta_archivo, calendario):
    nombre_archivo = ruta_archivo + "ventas_diarias.csv"
    try:
        with open(nombre_archivo, 'w') as archivo:  # Abrir en modo 'w' para reescribir
            archivo.write("Mes,Día,Ventas\n")  # Escribir encabezado
            for mes, dias in calendario.items():
                for dia, ventas in dias.items():
                    archivo.write(f"{mes},{dia},{ventas}\n")
        print(f"Calendario guardado exitosamente en {nombre_archivo}.")
    except IOError:
        print("Error al intentar guardar el calendario. Verifica los permisos.")
    except FileNotFoundError:
        print(f"No se encontró el archivo para guardar el calendario.")

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
        # Usar 'utf-8-sig' o 'latin1' para leer el archivo con codificación permisiva
        with open(nombre_archivo, 'r', encoding='utf-8-sig') as archivo:
            lines = archivo.readlines()

            # Itera sobre las líneas del archivo (ignorando encabezados)
            for i, line in enumerate(lines):
                if i == 0:  # Si hay encabezados, los dejamos pasar
                    continue

                # Se espera que la primera columna sea la categoría y el resto los datos
                values = line.strip().split(",")  # Usar coma como delimitador
                categoria = values[0]
                meses_ventas = values[1:]

                # Verifica que la cantidad de datos coincida con los meses
                if len(meses_ventas) == len(meses):
                    categoria_index = categorias.index(categoria)  # Encuentra la posición de la categoría
                    matriz[categoria_index] = [int(x) for x in meses_ventas]       
        print(f"Matriz cargada correctamente desde '{nombre_archivo}'.")
    except FileNotFoundError:
        print(f"Archivo no encontrado: {nombre_archivo}")
    except IOError:
        print("Error al cargar el archivo.")
    except ValueError as e:
        print(f"Error al procesar los datos: {e}")
        
    return matriz
