import json

def existeId(id, lstPersonal):
    for datos in lstPersonal:
        k = int(list(datos.keys())[0])
        if k == id:
            return True
    return False
    

def guardarEmpleado(lstPersonal, ruta):
    try:
        fd = open(ruta, "w")
    except Exception as e:
        print("Error al abrir el archivo para guardar el empleado.\n", e)
        return None
    
    try:
        json.dump(lstPersonal, fd)
    except Exception as e:
        print("Error al guardar la información del empleado.\n", e)
        return None
    fd.close()
    return True

def borrarPersonal(lstPersonal, rutaFile):
    print("\n\n3. Borrar Personal")

    id = int(input("Ingrese el ID: "))
    if not existeId(id, lstPersonal):
        print("No existe un empleado con ese ID")
        input("Presione Enter para continuar")
        return
    
    # range(lstPersonal)
    for i in range(lstPersonal):
        datos = lstPersonal[i]
        k = int(list(datos.keys())[0])
        if k == id:
            del lstPersonal[i]
            break

    if guardarEmpleado(lstPersonal,rutaFile) == True:
        print("El empleado ha sido borrado con exito")
        input("Presione Enter para continuar")
    else:
        print("Ocurrio un error al borrar el empleado")
    

def agregarPersonal(lstPersonal, ruta):
    print("\n\n1. Agregar Personal")

    id = int(input("Ingrese el ID: "))
    while existeId(id, lstPersonal):
        print("---> Ya existe un empleado con ese ID")
        id = int(input("\nIngrese el ID: "))

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    sexo = input("Sexo (M/F): ")
    telefono = input("Teléfono: ")
    dicEmpleado = {}
    dicEmpleado[id] = {"nombre":nombre, "edad":edad, "sexo":sexo, "telefono":telefono}
    lstPersonal.append(dicEmpleado)

    if guardarEmpleado(lstPersonal,ruta) == True:
        input("El empleado ha sido registrado con éxito. \nPresione cualquier tecla para continuar...")
    else:
        print("Ocurrio algún error al guardar el empleado.")


def menu():
    while True:
        try:
            print("*** REGISTRO DEL PERSONAL ***")
            print("1. Agregar")
            print("2. Modificar")
            print("3. Eliminar")
            print("4. Ver")
            print("5. Salir")
            op = int(input(">>> Opción (1-5)? "))
            if op < 1 or op > 5:
                print("Opción no válida. Escoja de 1 a 5.")
                input("Presione Enter para continuar...")
                continue
            return op
        except ValueError:
            print("Opcion no válida escoja de 1 a 5")
            input("Presione Enter para continuar")

def cargarInfo(lstPersonal, ruta):
    try:
        fd = open(ruta, "r")
    except Exception as e:
        try:
            fd = open(ruta, "w")
        except Exception as d:
            print("Error al intentar abrir el archivo\n",d)
            return None
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstPersonal = json.load(fd)
        else:
            lstPersonal = []
    except Exception as e:
        print("Error al cargar la información\n", e)
        return None
    print(lstPersonal)
    fd.close()
    return lstPersonal

# *** PROGRAMA PRINCIPAL ***
rutaFile = "Temas de Clase/Archivos/Json/data-Personal.json"
lstPersonal = []
lstPersonal = cargarInfo(lstPersonal,rutaFile)

while True:
    op = menu()
    if op == 1:
        agregarPersonal(lstPersonal,rutaFile)
    elif op == 2:
        # Modificar
        pass
    elif op == 3:
        borrarPersonal(lstPersonal,rutaFile)
        pass
    elif op == 4:
        pass
    elif op == 5:
        pass
    elif op == 6:
        pass
    elif op == 7:
        pass
    elif op == 8:
        print("\n\nGracias por usar el software. Adios")
        break