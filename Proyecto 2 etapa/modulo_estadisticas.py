
# Calcular el promedio de ventas por categoría
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

def calcular_promedio(ruta_archivo):
    matriz = leer_matriz(ruta_archivo)
    promedios = []
    for fila in matriz:
        total_ventas = sum(fila)
        promedio = total_ventas / len(fila) if len(fila) > 0 else 0  # Evitar división por cero
        promedios.append(f"{promedio:.2f}")  # Formatear como cadena con 2 decimales
    return promedios


def imprimir_promedios(promedios, categorias):
    print("\nPromedios de Ventas por Categoría:")
    for categoria, promedio in zip(categorias, promedios):
        print(f"{categoria}: {promedio} juegos vendidos en promedio.")
        
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
