def crear_usuario(ruta_archivo):
    nombre_archivo = ruta_archivo + "usuarios.txt"
    numeros_existentes = set()  # Usamos un conjunto para evitar duplicados

    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(";")
                if len(partes) >= 2:
                    numerodevendedor = partes[0]
                    numeros_existentes.add(numerodevendedor)  # Agregar el número a la lista de existentes

    except FileNotFoundError:
        # Si el archivo no existe, no hay números existentes
        print("no se encuentra el archivo")
        pass
    
    while True:
        numerodevendedor = input("Ingrese el número del vendedor: ")
        if numerodevendedor in numeros_existentes:
            print("Error: El número de vendedor ya existe. Por favor, elija uno diferente.")
        else:
            break

    nombreyapellido = input("Ingrese el nombre y apellido del vendedor: ")

    # Guardar el nuevo usuario en el archivo
    try:
        with open(nombre_archivo, 'a') as archivo:
            archivo.write(f"{numerodevendedor};{nombreyapellido}\n")
            print(f"Usuario {nombreyapellido} creado exitosamente.")
    except Exception as e:
        print(f"Error al crear usuario: {e}")


def mostrar_usuarios(ruta_archivo):
    nombre_archivo = ruta_archivo + "usuarios.txt"
    try:
        with open(nombre_archivo, 'r') as archivo:
            print("\nUsuarios registrados:")
            for linea in archivo:
                linea = linea.strip()  
                if not linea:  # Si la línea está vacía, se omite
                    continue
                
                partes = linea.split(";")  # Dividir la línea por el carácter ";"
                if len(partes) < 2:  # Verificar que haya al menos dos partes
                    print(f"Línea incorrecta: {linea}")  # Informar sobre líneas incorrectas
                    continue
                
                numerodevendedor, nombreyapellido = partes
                print(f"Número de Vendedor: {numerodevendedor}, Nombre: {nombreyapellido}")
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")
    except Exception as e:
        print(f"Error al mostrar usuarios: {e}")

