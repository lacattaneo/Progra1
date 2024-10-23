
def leer_matriz(ruta_archivo):
    nombre_archivo = ruta_archivo + "matriz.txt"
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
                    # Usar tabulaciones como delimitador
                    fila = list(map(int, linea.split("\t")[1:]))  # Ignorar la categoría (primer elemento)
                    matriz.append(fila)
                except ValueError:
                    print(f"Línea no válida ignorada: {linea}")  # Informar sobre líneas no válidas
    except FileNotFoundError:
        print("No se encontró el archivo de la matriz.")
    except Exception as e:
        print(f"Error al leer la matriz: {e}")
    
    return matriz

# Función para calcular los promedios de ventas
def calcular_promedio_recursivo(matriz, promedios):
    if not matriz:
        return promedios
    fila = matriz[0]
    total_ventas = sum(fila)
    promedio = total_ventas / len(fila) if len(fila) > 0 else 0
    promedios.append(f"{promedio:.2f}")
    return calcular_promedio_recursivo(matriz[1:], promedios)

def calcular_promedio(ruta_archivo):
    matriz = leer_matriz(ruta_archivo)
    promedios = calcular_promedio_recursivo(matriz, [])
    return promedios

def imprimir_promedios_recursivo(categorias, promedios):
    if not categorias:
        return
    print(f"{categorias[0]}: {promedios[0]} juegos vendidos en promedio.")
    return imprimir_promedios_recursivo(categorias[1:], promedios[1:])

def imprimir_promedios(promedios, categorias):
    print("\nPromedios de Ventas por Categoría:")
    imprimir_promedios_recursivo(categorias, promedios)

def guardar_promedios_recursivo(archivo, categorias, promedios):
    if not categorias:
        return
    archivo.write(f"{categorias[0]}\t{promedios[0]} juegos vendidos en promedio.\n")
    return guardar_promedios_recursivo(archivo, categorias[1:], promedios[1:])

def guardar_promedios(ruta_archivo, categorias, promedios):
    nombre_archivo = ruta_archivo + "estadisticas.txt"
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("Categoría\tPromedio de Ventas\n")
            guardar_promedios_recursivo(archivo, categorias, promedios)
        print(f"Promedios guardados exitosamente en {nombre_archivo}.")
    except Exception as e:
        print(f"Error al guardar los promedios: {e}")

def imprimir_matriz_de_archivo(ruta_archivo):
    nombre_archivo = ruta_archivo + "matriz.txt"
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
        print(f"No se encontró el archivo: {nombre_archivo}.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
