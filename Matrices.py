

def matriz():
    categorias=10
    meses=12
    matriz=[[0]*meses for i in range(categorias)]
    return matriz

def imprimir_matriz(matriz,cate,mes):
    canCate = len(matriz)
    cantMeses = len(matriz[0])
    print("     ",end="   ")
    for i in range(12):
        print("%3s" % (mes[i]), end=" ")
    print()


    for f in range (canCate):
        print("%6s" % (cate[f]), end=" ")
        for c in range(cantMeses):
            print("%3d" %matriz[f][c], end=" ")
        print()

m=matriz()
categorias=["Accion","Aventu","RolRPG","Deport","Carrer","Estrat","Simula","Puzzle","Terror","MulMMO"]
meses=["ENE","FEB","MAR","ABR","MAY","JUN","JUL","AGO","SEP","OCT","NOV","DIC"]
imprimir_matriz(m,categorias,meses)
