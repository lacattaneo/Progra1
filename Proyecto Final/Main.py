from modulo_calendario import crear_calendario
from modulo_menu import menu
from modulo_ventas import cargar_matriz

def datos():
    categorias_juegos = ["Accion", "Aventu", "RolRPG", "Deport", "Carrer", "Estrat", "Simula", "Puzzle", "Terror", "MulMMO"]
    meses_del_anio = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]
    matriz_ventas = cargar_matriz(categorias_juegos, meses_del_anio)
    anio_actual = 2024
    calendario_ventas = crear_calendario(anio_actual)
    return matriz_ventas, categorias_juegos, meses_del_anio, calendario_ventas

def main():
    # Obtener los datos iniciales
    matriz_ventas, categorias_juegos, meses_del_anio, calendario_ventas = datos()
    # Ejecutar el menú principal
    menu(matriz_ventas, categorias_juegos, meses_del_anio, calendario_ventas)

main()