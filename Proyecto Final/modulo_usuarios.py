import csv

def crear_usuario(ruta_archivo):
    nombre_archivo = ruta_archivo + "usuarios.csv"
    usuarios_existentes = set()

    # Leer nombres existentes desde el archivo
    try:
        with open(nombre_archivo, 'r', newline='') as archivo:
            lector_csv = csv.reader(archivo)
            for fila in lector_csv:
                if len(fila) >= 2:  # Verificar que haya al menos ID y nombre
                    usuarios_existentes.add(fila[1])  # Agregar el nombre y apellido al conjunto
    except FileNotFoundError:
        print("El archivo 'usuarios.csv' no se encontró. Se creará uno nuevo al agregar usuarios.")
    except IOError:
        print("Error al intentar leer el archivo. Por favor, verifica los permisos.")
        return

    # Solicitar el nombre y apellido del nuevo usuario
    while True:
        nombreyapellido = input("Ingrese el nombre y apellido del usuario: ").strip()
        if nombreyapellido in usuarios_existentes:
            print("Error: El usuario ya existe. Por favor, ingrese un nombre diferente.")
        else:
            break

    # Asignar un nuevo ID automáticamente
    nuevo_id = len(usuarios_existentes) + 1

    # Guardar el nuevo usuario en el archivo CSV
    try:
        with open(nombre_archivo, 'a', newline='') as archivo:
            escritor_csv = csv.writer(archivo)
            escritor_csv.writerow([nuevo_id, nombreyapellido])  # Escribir el ID y el nombre en columnas separadas
            print(f"Usuario '{nombreyapellido}' creado exitosamente.")
    except IOError:
        print("Error al intentar escribir en el archivo. Por favor, verifica los permisos.")


def mostrar_usuarios(ruta_archivo):
    nombre_archivo = ruta_archivo + "usuarios.csv"
    try:
        with open(nombre_archivo, 'r') as archivo:
            print("\nUsuarios registrados:")
            for linea in archivo:
                linea = linea.strip()  # Eliminar espacios innecesarios
                if not linea:  # Si la línea está vacía, se omite
                    continue
                
                partes = linea.split(",")  # Dividir la línea por el carácter ","
                if len(partes) < 2:  # Verificar que haya al menos ID y nombre
                    print(f"Línea incorrecta: {linea}")  # Informar sobre líneas incorrectas
                    continue
                
                numerodeusuario, nombreyapellido = partes
                print(f"Número de Usuario: {numerodeusuario}, Nombre: {nombreyapellido}")
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")
    except IOError:
        print("Error al intentar leer el archivo. Por favor, verifica los permisos.")
