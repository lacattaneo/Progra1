def leer_matriz(ruta_archivo):
    nombre_archivo = ruta_archivo + "ventas_mes.csv"
    matriz = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            # Ignorar la primera línea (encabezados)
            for linea in lineas[1:]:  # Comienza desde la segunda línea
                linea = linea.strip()  # Eliminar espacios en blanco
                if not linea:  # Si la línea está vacía, se omite
                    continue
                # Convertir la línea en una lista de enteros usando tabulaciones
                try:
                    fila = list(map(int, linea.split("\t")[1:]))  # Ignorar la categoría (primer elemento)
                    matriz.append(fila)
                except ValueError:
                    print(f"Línea no válida ignorada: {linea}")  # Informar sobre líneas no válidas
    except FileNotFoundError:
        print("No se encontró el archivo de la matriz.")
    except IOError:
        print("Error al intentar leer el archivo. Por favor, verifica los permisos.")
    
    return matriz

# Función para llamar a la recursividad
def calcular_promedio(ruta_archivo):
    matriz = leer_matriz(ruta_archivo)
    promedios = calcular_promedio_recursivo(matriz)
    print(f"Promedios calculados: {promedios}")
    return promedios

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

def imprimir_promedios(promedios, categorias):
    if not promedios or not categorias:
        print("No hay datos para imprimir los promedios.")
        return
    print("\nPromedios de Ventas por Categoría:")
    for i in range(len(categorias)):
        print(f"{categorias[i]}: {promedios[i]:.2f} juegos vendidos en promedio Anual.")

def guardar_promedios(ruta_archivo, categorias, promedios):
    nombre_archivo = ruta_archivo + "promedio_anual.txt"
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("Categoría\tPromedio de Ventas\n")
            for i in range(len(categorias)):
                archivo.write(f"{categorias[i]}\t{promedios[i]:.2f} juegos vendidos en promedio.\n")
        print(f"Promedios guardados exitosamente en {nombre_archivo}.")
    except IOError:
        print("Error al guardar el archivo. Por favor, verifica los permisos.")

# Función para imprimir la matriz de ventas desde el archivo
def imprimir_matriz_de_archivo(ruta_archivo):
    nombre_archivo = ruta_archivo + "ventas_mes.csv"
    try:
        with open(nombre_archivo, 'r') as archivo:
            # Leer la primera línea para obtener los meses
            encabezado = archivo.readline().strip()
            meses = encabezado.split("\t")[1:]  # Ignorar la primera columna que es "Categoría/Mes"
            
            print("     ", end="   ")
            for mes in meses:
                print("%3s" % mes, end=" ")
            print()
            
            # Leer y mostrar las categorías y sus ventas
            for linea in archivo:
                linea = linea.strip()
                if not linea:  # Si la línea está vacía, se omite
                    continue
                partes = linea.split("\t")  # Dividir la línea por tabulaciones
                categoria = partes[0]  # Primera columna es la categoría
                ventas = partes[1:]  # El resto son las ventas

                print("%6s" % categoria, end=" ")
                for venta in ventas:
                    print("%3s" % venta, end=" ")
                print()

    except FileNotFoundError:
        print(f"No se encontró el archivo: {nombre_archivo}")
    except IOError:
        print("Error al intentar leer el archivo. Por favor, verifica los permisos.")
