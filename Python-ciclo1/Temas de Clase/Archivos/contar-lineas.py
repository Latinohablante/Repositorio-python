fd = open("Temas de Clase/Archivos/mbox-short.txt", "r")

cp = 0
cl = 0
for linea in fd:
    linea = linea.strip() # quitar espacios al inicio y al final
    cp += len(linea.split(" "))


    # Esta estrategia es muy lejana al valor que quiero que es 8272
    # for lin in linea.split(" "):
    #     if lin.isalnum():
    #         cp += 1

    cl+=1


fd.close()
print("Cantidad de lineas:",cl)
print("Cantidad de palabras: ",cp)