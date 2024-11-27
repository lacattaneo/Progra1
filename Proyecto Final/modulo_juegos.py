import os

# Lista de categorías de juegos, con la capitalización esperada para mostrarlas
CATEGORIAS = ("Accion", "Aventu", "RolRPG", "Deport", "Carrer", "Estrat", "Simula", "Puzzle", "Terror", "MulMMO")

# Función para obtener los juegos desde el archivo
def obtener_juegos(ruta_archivo):
    nombre_archivo = os.path.join(ruta_archivo, "juegos.csv")  # Usamos os.path.join para manejar bien las rutas
    juegos = {categoria.lower(): [] for categoria in CATEGORIAS}  # Crear un diccionario para almacenar los juegos
    
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue  # Ignorar líneas vacías
                partes = linea.split("\t")  # Separar la línea por el delimitador '\t' (tabulaciones)
                if len(partes) == 2:  # Verificar que la línea tenga exactamente 2 partes (categoría y juego)
                    categoria, juego = partes
                    categoria = categoria.strip().lower()  # Normalizamos la categoría a minúsculas
                    if categoria in juegos:
                        juegos[categoria].append(juego.strip())  # Agregar el juego a la categoría correspondiente
    except FileNotFoundError:
        print("No se encontró el archivo de juegos.")
    except IOError:
        print("Hubo un error al intentar leer el archivo.")
    return juegos

# Función para agregar un juego
def agregar_juego(ruta_archivo, categoria, juego):
    """Agrega un nuevo juego a la categoría especificada en el archivo."""
    categoria = categoria.strip().lower()  # Asegurarse de que la categoría esté en minúsculas
    if categoria not in [cat.lower() for cat in CATEGORIAS]:  # Comparación insensible a mayúsculas
        print(f"Categoría '{categoria}' no válida.")
        return

    nombre_archivo = os.path.join(ruta_archivo, "juegos.csv")
    
    # Verificar si el archivo existe
    if not os.path.exists(nombre_archivo):
        print(f"El archivo {nombre_archivo} no existe. Creando uno nuevo.")
    
    try:
        with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(f"{categoria.capitalize()}\t{juego}\n")  # Usar tabulación para separar categoría y juego
            print(f"Juego '{juego}' agregado a la categoría '{categoria.capitalize()}' exitosamente.")
    except FileNotFoundError:
        print("No se encontró el archivo para agregar el juego.")
    except IOError as e:
        print(f"Hubo un error al intentar escribir en el archivo: {e}")

# Función para mostrar los juegos
def mostrar_juegos(ruta_archivo):
    """Muestra todos los juegos organizados por categoría."""
    juegos = obtener_juegos(ruta_archivo)
    
    print("\nJuegos por categoría:")
    for categoria, lista_juegos in juegos.items():
        print(f"{categoria.capitalize()}:")  # Nombre de la categoría (con mayúscula inicial)
        if lista_juegos:  # Verifica si hay juegos en la categoría
            for idx, juego in enumerate(lista_juegos, start=1):
                print(f"  {idx}. {juego}")
        else:
            print("  No hay juegos en esta categoría.")
