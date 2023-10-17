fd = open("Temas de Clase/Archivos/ejercicio empleados/datos-empleados.txt", "r")

#for linea in fd:
#    print(linea, end="")

Listas = []
for linea in fd:
    Listas.append(linea.split(","))

for i in range(1, len(Listas)):
    for k in range(len(Listas[0])):
        print(Listas[0][k].strip(), end=": ")
        print(Listas[i][k].strip())# .strip() -> retira el \n
    print("="*30)

fd.close()

#print(Listas[0])
#print(Listas[0][2])