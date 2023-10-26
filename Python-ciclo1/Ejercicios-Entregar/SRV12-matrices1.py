def crearMatrices(fil, col):
    m = []
    for i in range(fil):
        fila = [0] * col # si col:5 => [0,0,0,0,0]
        m.append(fila)
    return m

def printMatriz(mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            print(mat[f][c], end="\t ")
        print("")

def llenarMatriz1(mat):
    contador = 0
    for f in range(len(mat)):
        # print(f"\nFila #{f+1}")
        for c in range(len(mat[f])):
            contador += 1
            mat[f][c] = contador #int(input(f"mat[{f+1}][{c+1}]? "))

def llenarMatriz2(mat):
    
    for c in range(len(mat)):
        
        contador = 0
        # print(f"\nFila #{f+1}")
        for f in range(len(mat[c])):
            contador += 1
            if mat[c][f] % 2 == 0:
                contador -= 1
                mat[c][f] = contador #int(input(f"mat[{f+1}][{c+1}]? "))
            else:
                mat[c][f] = contador
            

def llenarMatriz7(mat):
    contador = 0
    for f in range(len(mat)):
        # print(f"\nFila #{f+1}")
        for c in range(len(mat[f])):
            contador += 1
            mat[c][f] = contador #int(input(f"mat[{f+1}][{c+1}]? "))
            

filas = int(input("Ingrese el tamaño de la matriz cuadrada: "))
columnas = filas

matriz = crearMatrices(filas,columnas)
llenarMatriz1(matriz)
printMatriz(matriz)