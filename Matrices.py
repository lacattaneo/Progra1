

def matriz():
    categorias=10
    meses=12
    matriz=[[0]*meses for i in range(categorias)]
    return matriz

def imprimir_matriz(matriz):
    categorias = len(matriz)
    columnas = len(matriz[0])
    for f in range (categorias):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end=" ")
        print()
m=matriz()
print(imprimir_matriz(m))