def validacionCategoria(categoria):# Valida que la categoría esté entre 0 y 10
    while not (0 <= categoria <= 10):  
        categoria = int(input("Ingrese una categoria valida entre 1 y 10 o 0 para salir: "))
        if categoria == 0:
            return categoria  # Salir si se ingresa 0
    return categoria

# Validación de mes (entre 1 y 12)
validacionMeses = lambda mes: mes if (1 <= mes <= 12) else int(input("Ingrese un número válido entre 1 y 12: "))

# Validación de cantidad (mayor o igual a 0)
cantidadVentas = lambda cantidad: cantidad if cantidad >= 0 else int(input("Ingrese una cantidad mayor o igual a 0: "))
