import json

fd = open("Temas de Clase/Archivos/Json/lista.json", "r")

lst = []

lst = json.load(fd) # 

for elemento in lst:
    print(f"Nombre: {elemento['nombre']}")
    print(f"Edad: {elemento['edad']}")
    print("-" * 30)

fd.close()