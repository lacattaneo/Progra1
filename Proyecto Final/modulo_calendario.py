def crear_calendario(anio):
    dias_por_mes = {
        "Enero": {dia: 0 for dia in range(1, 32)},
        "Febrero": {dia: 0 for dia in (range(1, 30) if es_bisiesto(anio) else range(1, 29))},
        "Marzo": {dia: 0 for dia in range(1, 32)},
        "Abril": {dia: 0 for dia in range(1, 31)},
        "Mayo": {dia: 0 for dia in range(1, 32)},
        "Junio": {dia: 0 for dia in range(1, 31)},
        "Julio": {dia: 0 for dia in range(1, 32)},
        "Agosto": {dia: 0 for dia in range(1, 32)},
        "Septiembre": {dia: 0 for dia in range(1, 31)},
        "Octubre": {dia: 0 for dia in range(1, 32)},
        "Noviembre": {dia: 0 for dia in range(1, 31)},
        "Diciembre": {dia: 0 for dia in range(1, 32)}
    }
    return dias_por_mes


def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)
