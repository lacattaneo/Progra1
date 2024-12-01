from modulo_estadisticas import calcular_promedio, imprimir_promedios, imprimir_matriz_de_archivo, guardar_promedios
from modulo_usuarios import crear_usuario, mostrar_usuarios
from modulo_ventas import agregar_venta, guardar_matriz, guardar_calendario
from modulo_juegos import obtener_juegos, agregar_juego, mostrar_juegos


def menu_principal():
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


def volver_inicio():
    eleccion_regresar = 'x'
    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\nPresione V para volver al menu: ")
        print(" ")


def menu(matriz_ventas, categorias_juegos, meses_del_anio, calendario_ventas):
    mi_ruta= "datos/"
    finalizar_programa = False
    while not finalizar_programa:
        menu = menu_principal()
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
                print("""CATEGORIAS = ("Accion", "Aventu", "RolRPG", "Deport", "Carrer", "Estrat", "Simula", "Puzzle", "Terror", "MulMMO")""")
                categoria = input("Seleccione la categoría para agregar un juego: ")
                juego = input("Ingrese el nombre del juego: ")
                agregar_juego(mi_ruta, categoria, juego)
            elif eleccion_usuario == '2':  # Mostrar el catálogo de juegos
                obtener_juegos(mi_ruta)
                mostrar_juegos(mi_ruta)
            elif eleccion_usuario == '3':
                continue  # Volver al menú principal

        elif menu == 3:
            imprimir_matriz_de_archivo(mi_ruta)
            promedios = calcular_promedio(mi_ruta, categorias_juegos)
            imprimir_promedios(promedios, categorias_juegos)
            guardar_promedios(mi_ruta, categorias_juegos, promedios)
            volver_inicio()

            
        elif menu == 4:
            eleccion_usuario = 'x'
            while not eleccion_usuario.isnumeric() or int(eleccion_usuario) not in range(1, 3):
                print('''
                [1] - Agregar Ventas
                [2] - Volver al Menu Principal''')
                print(' ')
                eleccion_usuario = input("Elige una opción: ")
                
            if eleccion_usuario == '1': # Agregar una Venta
                agregar_venta(matriz_ventas, categorias_juegos, meses_del_anio, calendario_ventas)
                guardar_calendario(mi_ruta, calendario_ventas)  # Sólo guardar el calendario
                volver_inicio()
            elif eleccion_usuario == '2':
                continue  # Volver al menú principal
                
        elif menu == 5:
            print("Fin Del Programa, Gracias por Confiar en Nosotros!!")
            finalizar_programa = True
