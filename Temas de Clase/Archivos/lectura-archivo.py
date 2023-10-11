archivo = open("Temas de Clase/Archivos/nombres.txt", "r")

texto = archivo.read()
# print(texto)


archivo.seek(0) # seek lleva el puntero al principio del archivo
texto2 = archivo.readline()
# print(texto2)


archivo.seek(0)
texto3 = archivo.readlines()
print(texto3)


archivo.close()