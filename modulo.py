def validacionCategoria(categoria):# Valida que la categoría esté entre 0 y 10
    while not (0 <= categoria <= 10):  
        categoria = int(input("Ingrese una categoria valida entre 1 y 10 o 0 para salir: "))
        if categoria == 0:
            return categoria  # Salir si se ingresa 0
    return categoria

def validacionMeses(mes):# Valida que el mes esté entre 1 y 12
    while not (1 <= mes <= 12):  
        mes = int(input("Ingrese un número válido entre 1 y 12: "))
    return mes

def cantidadVentas(cantidad):# Valida que la cantidad sea mayor o igual a 0
    while cantidad < 0:  
        cantidad = int(input("Ingrese una cantidad mayor o igual a 0: "))
    return cantidad

