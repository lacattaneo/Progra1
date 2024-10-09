from modulo_validaciones import validacionCategoria, validacionMeses, cantidadVentas
from modulo_estadisticas import calcular_promedio, imprimir_promedios
from modulo_usuarios import crear_usuario, mostrar_usuarios
from modulo_ventas import agregar_venta, agregar_promociones
from modulo_juegos import obtener_juegos, agregar_juego, mostrar_juegos

matriz = lambda categorias=10, meses=12: [[0] * meses for _ in range(categorias)] #Funcion lambda para crear matriz por comprension

mi_ruta= "datos/"

def main():
    print(' ')
    print('*' * 64)
    print('*' * 64)
    print('*' * 5 + " Bienvenido al Administrador de Ventas de Videojuegos " + '*' * 5)
    print('*' * 64)
    print('*' * 64)
    print('\n')
    
    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 6):
        print('''
        [1] - Usuarios
        [2] - Catalogo de Juegos
        [3] - Mostrar Estadísticas
        [4] - Agregar Ventas
        [5] - Salir del programa''')
        print(' ')
        eleccion_menu = input("Elige una opcion: ")
        print(' ')
        

    return int(eleccion_menu)

def imprimir_matriz(matriz, cate, mes):  # Función para imprimir la matriz
    canCate = len(matriz)
    cantMeses = len(matriz[0])
    print("     ", end="   ")
    for i in range(12):
        print("%3s" % (mes[i]), end=" ")
    print()

    for f in range(canCate):
        print("%6s" % (cate[f]), end=" ")
        for c in range(cantMeses):
            print("%3d" % matriz[f][c], end=" ")
        print()

def volver_inicio():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\nPresione V para volver al menu: ")
        print(" ")

m = matriz()
categorias = ["Accion", "Aventu", "RolRPG", "Deport", "Carrer", "Estrat", "Simula", "Puzzle", "Terror", "MulMMO"]
meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]

finalizar_programa = False

while not finalizar_programa:
    menu = main()
    
    if menu == 1:
        eleccion_usuario = 'x'
        while not eleccion_usuario.isnumeric() or int(eleccion_usuario) not in range(1, 4):
            print('''
            [1] - Crear Usuario
            [2] - Mostrar Usuarios
            [3] - Volver al Menu Principal''')
            print(' ')
            eleccion_usuario = input("Elige una opción: ")
        
        if eleccion_usuario == '1':
            crear_usuario(mi_ruta)  # Crear usuario
        elif eleccion_usuario == '2':         
            mostrar_usuarios(mi_ruta)  # Mostrar usuarios
        elif eleccion_usuario == '3':
            continue  # Volver al menú principal

    elif menu == 2:
        eleccion_usuario = 'x'
        while not eleccion_usuario.isnumeric() or int(eleccion_usuario) not in range(1, 4):
            print('''
            [1] - Agregar Juego
            [2] - Mostrar Catalogo
            [3] - Volver al Menu Principal''')
            print(' ')
            eleccion_usuario = input("Elige una opción: ")
            
        if eleccion_usuario == '1':  # Agregar un juego
            categoria = input("Seleccione la categoría para agregar un juego: ")
            juego = input("Ingrese el nombre del juego: ")
            agregar_juego("datos/juegos.txt", categoria, juego)
        elif eleccion_usuario == '2':  # Mostrar el catálogo de juegos
            obtener_juegos("datos/juegos.txt")
            mostrar_juegos("datos/juegos.txt")
        elif eleccion_usuario == '3':
            continue  # Volver al menú principal

    elif menu == 3:
        imprimir_matriz(m, categorias, meses)
        promedios = calcular_promedio(m)
        imprimir_promedios(promedios, categorias)
        volver_inicio()
        
    elif menu == 4:
        eleccion_usuario = 'x'
        while not eleccion_usuario.isnumeric() or int(eleccion_usuario) not in range(1, 4):
            print('''
            [1] - Agregar Ventas
            [2] - Agregar Promociones
            [3] - Volver al Menu Principal''')
            print(' ')
            eleccion_usuario = input("Elige una opción: ")
            
        if eleccion_usuario == '1':  # Agregar una Venta
            agregar_venta(m, categorias, meses)
            volver_inicio()
        elif eleccion_usuario == '2':  # Agregar Promociones
            agregar_promociones(m, categorias, meses)
            volver_inicio()
        elif eleccion_usuario == '3':
            continue  # Volver al menú principal
            
    elif menu == 5:
        print("Fin Del Programa, Gracias por Confiar en Nosotros!!")
        finalizar_programa = True
