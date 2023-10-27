fd = open("Temas de Clase/Archivos/nombres.txt", "r")

fd2 = open("Temas de Clase/Archivos/nombres-bak.txt", "w")

for linea in fd:
    fd2.write(linea)


fd2.close()
fd.close()