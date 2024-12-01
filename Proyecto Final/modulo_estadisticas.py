# Función para leer la matriz desde el archivo de ventas
def leer_matriz(ruta_archivo):
    nombre_archivo = ruta_archivo + "ventas_mes.csv"
    matriz = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8-sig') as archivo:
            lineas = archivo.readlines()
            for linea in lineas[1:]:  # Comienza desde la segunda línea (saltamos la cabecera)
                linea = linea.strip()
                if not linea:  # Si la línea está vacía, se omite
                    continue
                try:
                    # Usamos coma como separador
                    fila = list(map(int, linea.split(",")[1:]))  # Ignorar la primera columna (categoría)
                    matriz.append(fila)
                except ValueError:
                    print(f"Línea no válida ignorada: {linea}")
    except FileNotFoundError:
        print("No se encontró el archivo de la matriz.")
    except IOError:
        print("Error al intentar leer el archivo.")
    
    return matriz

# Función para calcular los promedios de ventas por categoría
def calcular_promedio(ruta_archivo, categorias):
    matriz = leer_matriz(ruta_archivo)
    print(matriz)  # Agregar para depuración (ver cómo se lee la matriz)
    
    if len(matriz) != len(categorias):
        print("Error: La cantidad de filas en la matriz no coincide con las categorías.")
        return []

    promedios = calcular_promedio_recursivo(matriz)
    return [f"{promedio:.2f}" for promedio in promedios]  # Formatear los promedios

# Función recursiva que calcula los promedios
def calcular_promedio_recursivo(matriz):
    promedios = []
    for fila in matriz:
        if fila:
            promedio = sum(fila) / len(fila)
        else:
            promedio = 0
        promedios.append(promedio)
    return promedios

# Función para imprimir los promedios de ventas por categoría
def imprimir_promedios(promedios, categorias):
    if not promedios or not categorias:
        print("No hay datos para imprimir los promedios.")
        return

    if len(promedios) != len(categorias):
        print("Error: Las listas de promedios y categorías no tienen la misma longitud.")
        return

    print("\nPromedios de Ventas por Categoría:")
    for i in range(len(categorias)):
        print(f"{categorias[i]}: {promedios[i]} juegos vendidos en promedio Anual.")

# Función para guardar los promedios en un archivo
def guardar_promedios(ruta_archivo, categorias, promedios):
    if len(categorias) != len(promedios):
        print("Error: Las listas de categorías y promedios no coinciden en longitud.")
        return

    nombre_archivo = ruta_archivo + "promedio_anual.txt"
    try:
        with open(nombre_archivo, 'w', encoding='utf-8-sig') as archivo:
            archivo.write("Categoría,Promedio de Ventas\n")
            for i in range(len(categorias)):
                archivo.write(f"{categorias[i]},{promedios[i]} juegos vendidos en promedio.\n")
        print(f"Promedios guardados exitosamente en {nombre_archivo}.")
    except IOError:
        print("Error al guardar el archivo. Verifica los permisos o la ruta.")

# Función para imprimir la matriz de ventas desde el archivo
def imprimir_matriz_de_archivo(ruta_archivo):
    nombre_archivo = ruta_archivo + "ventas_mes.csv"
    try:
        with open(nombre_archivo, 'r', encoding='utf-8-sig') as archivo:
            # Leer la primera línea para obtener los meses
            encabezado = archivo.readline().strip()
            meses = encabezado.split(",")[1:]  # Usamos coma como separador
            
            print("     ", end="   ")
            for mes in meses:
                print(f"{mes:3}", end=" ")
            print()
            
            # Leer y mostrar las categorías y sus ventas
            for linea in archivo:
                linea = linea.strip()
                if not linea:  # Si la línea está vacía, se omite
                    continue
                partes = linea.split(",")  # Usamos coma como separador
                categoria = partes[0]  # Primera columna es la categoría
                ventas = partes[1:]  # El resto son las ventas

                print(f"{categoria:6}", end=" ")
                for venta in ventas:
                    print(f"{venta:3}", end=" ")
                print()

    except FileNotFoundError:
        print(f"No se encontró el archivo: {nombre_archivo}")
    except IOError:
        print("Error al intentar leer el archivo. Por favor, verifica los permisos.")
