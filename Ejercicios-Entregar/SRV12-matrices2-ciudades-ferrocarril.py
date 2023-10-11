# En las filas en la primera posición tengo la ciudad principal, y en las posiciones en la misma fila tengo las ciudades con conexión directa

def crearMatrices(ciudadPrincipal, ciudadConexion):
    m = []
    for i in range(ciudadPrincipal):
        fila = [0] * ciudadConexion # si col:5 => [0,0,0,0,0]
        m.append(fila)
    return m

def printMatriz(mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            print(mat[f][c], end=" \t\t")
        print("")

def llenarMatriz(mat):
    for f in range(len(mat)):
        print(f"\nFila #{f+1}")
        for c in range(len(mat[f])):
            mat[f][c] = input(f"ciudad[{f+1}][{c+1}]? ")
            

N = int(input("Ingrese el número de ciudades: "))
conexiones = int(input("Ingrese el número máximo de conexiones de una ciudad dentro de la red ferroviaria: "))

matriz = crearMatrices(N,conexiones)
llenarMatriz(matriz)
printMatriz(matriz)