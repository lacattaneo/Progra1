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
    
    # Formatear los promedios a dos decimales
    promedios_formateados = [f"{promedio:.2f}" for promedio in promedios]
    
    print(f"Promedios calculados: {promedios_formateados}")
    return promedios_formateados


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

    if len(promedios) != len(categorias):
        print("Error: Las listas de promedios y categorías no tienen la misma longitud.")
        return

    print("\nPromedios de Ventas por Categoría:")
    for i in range(len(categorias)):
        try:
            promedio = float(promedios[i])  # Convertir a float antes de formatear
            print(f"{categorias[i]}: {promedio:.2f} juegos vendidos en promedio Anual.")
        except ValueError:
            print(f"Error: El valor '{promedios[i]}' no es un número válido.")



def guardar_promedios(ruta_archivo, categorias, promedios):
    nombre_archivo = ruta_archivo + "promedio_anual.txt"
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("Categoría\tPromedio de Ventas\n")
            for i in range(len(categorias)):
                try:
                    promedio = float(promedios[i])  # Convertir a float antes de formatear
                    archivo.write(f"{categorias[i]}\t{promedio:.2f} juegos vendidos en promedio.\n")
                except ValueError:
                    archivo.write(f"{categorias[i]}\tError: Valor no válido\n")
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

def guardar_matriz(matriz, categorias, mes):
    mi_ruta = "datos/"
    nombre_archivo = mi_ruta + "ventas_mes.csv"

    try:
        # Leer el archivo existente
        datos_existentes = {}
        try:
            with open(nombre_archivo, 'r') as archivo:
                for linea in archivo:
                    partes = linea.strip().split("\t")
                    categoria = partes[0]
                    try:
                        valores = list(map(int, partes[1:]))
                        datos_existentes[categoria] = valores
                    except ValueError:
                        print(f"Advertencia: Se ignoró una línea no numérica: {linea}")
        except FileNotFoundError:
            print(f"Archivo no encontrado. Se creará un nuevo archivo en '{nombre_archivo}'.")

        # Actualizar los datos existentes con los nuevos datos
        for i in range(len(categorias)):
            datos_existentes[categorias[i]] = matriz[i]

        # Escribir los datos actualizados en el archivo
        with open(nombre_archivo, 'w') as archivo:
            for categoria, valores in datos_existentes.items():
                archivo.write(f"{categoria}\t" + "\t".join(map(str, valores)) + "\n")

        print(f"Matriz actualizada correctamente en '{nombre_archivo}'.")

    except IOError:
        print("Error al intentar guardar la matriz. Por favor, verifica los permisos o la ruta.")
