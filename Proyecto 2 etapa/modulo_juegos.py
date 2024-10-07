import os

# Lista de categorías de juegos, definidas como tuplas para que sean inmutables
CATEGORIAS = ("Accion", "Aventu", "RolRPG", "Deport", "Carrer", "Estrat", "Simula", "Puzzle", "Terror", "MulMMO")

def obtener_juegos(ruta_archivo):
    """Lee los juegos del archivo y devuelve un diccionario de juegos por categoría."""
    juegos = {categoria: [] for categoria in CATEGORIAS}  # Crear un diccionario para almacenar los juegos
    try:
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                categoria, juego = linea.split(";")
                if categoria in juegos:
                    juegos[categoria].append(juego)  # Agregar el juego a la categoría correspondiente
    except FileNotFoundError:
        print("No se encontró el archivo de juegos.")
    return juegos

def agregar_juego(ruta_archivo, categoria, juego):
    """Agrega un nuevo juego a la categoría especificada en el archivo."""
    if categoria not in CATEGORIAS:
        print("Categoría no válida.")
        return

    try:
        with open(ruta_archivo, 'a') as archivo:
            archivo.write(f"{categoria};{juego}\n")  # Escribir el juego en el archivo
            print(f"Juego '{juego}' agregado a la categoría '{categoria}' exitosamente.")
    except Exception as e:
        print(f"Error al agregar juego: {e}")

def mostrar_juegos(ruta_archivo):
    """Muestra todos los juegos organizados por categoría."""
    juegos = obtener_juegos(ruta_archivo)
    
    print("\nJuegos por categoría:")
    for categoria, lista_juegos in juegos.items():
        print(f"{categoria}:")
        for idx, juego in enumerate(lista_juegos, start=1):
            print(f"  {idx}. {juego}")
    
