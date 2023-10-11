def calcProdMaxIngresosSem(matrizVentas,matrizPrecios):
    filas = len(matrizVentas)
    lstTotVntas = [0] * filas # -> [0, 0, 0, ..., filas ]
    for f in range(filas):
        lstTotVntas[f] = sum(matrizVentas[f]) * matrizPrecios[f]
    # print(lstTotVntas)
    maxVntas = max(lstTotVntas)
    prodMaxVntas = lstTotVntas.index(maxVntas) + 1
    return prodMaxVntas

def calcDiaMasIngresosSem(matrizVentas,matrizPrecios):
    columnas = len(matrizVentas[0])
    filas = len(matrizVentas)
    lstTotVntasDia = [0] * filas # -> [0, 0, 0, ..., filas ]
    dia = [0] * columnas
    for c in range(columnas):
        for f in range(filas):
            lstTotVntasDia[f] = matrizVentas[f][c] * matrizPrecios[f]
        dia[c] = sum(lstTotVntasDia)

    print(dia)
    diaMaxVntas = max(dia)
    diaMasVentas = dia.index(diaMaxVntas)
    return diaMasVentas

matrizPrecios = [1500, 5000, 6500, 2500, 22500]
matrizVentas = [[100, 88, 92, 94, 85, 110, 118],
                [30, 42, 31, 32, 38, 40, 37],
                [23, 35, 39, 45, 55, 60, 61],
                [45, 50, 56, 65, 47, 57, 68],
                [18, 25, 33, 21, 22, 28, 32]]

productoMaxIngresosSemana = calcProdMaxIngresosSem(matrizVentas,matrizPrecios)

diaMasIngresosSemana = calcDiaMasIngresosSem(matrizVentas,matrizPrecios)

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print(f"El producto que genera más ingresos en la semana es el {productoMaxIngresosSemana}")
print(f"El día con más ingresos en la semana es el {dias[diaMasIngresosSemana]}")