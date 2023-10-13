import json

fd = open("Temas de Clase/Archivos/Json/lista.json", "w")

lst = [{"nombre":"Paola","edad": 25},
       {"nombre":"Carlos","edad": 17},
       {"nombre":"Juan","edad": 28},
       {"nombre":"Mateo","edad": 21},
       {"nombre":"Patricia","edad": 19},
       {"nombre":"Yulieth","edad": 20},
       {"nombre":"Marcos","edad": 23}]

json.dump(lst,fd) # Guarda la información en el disco, o sea que crea un archivo

fd.close()