# archivo de texto CSV separado por ;
# Información a ingresar: codigo del observatorio, nombre del observatorio, fecha de registro(dia/mes/año),temperatura máxima, temperatura mínima
# 1. Crear listados orden ascendente por sus códigos
# 2. Listado de observatorios ordenados ascendentemente por su nombre
# 3. Listado de observaciones de un observatorio en particular(ingresando su código). Las observaciones están ordenadas por el año, día y mes. 
# 4. Listado de cantidad de observaciones, la observacion de la temp máxima, mínima, y promedio de un observatorio en particular, el usuario ingresa el código del observatorio
# 5. Listado de todas las observaciones a nivel nacional ordenadas por el  código del observatorio y paginadas cada 10 items. El listado muestra el  código y nombre del observatorio, temperatura máxima y mínima y promedio.
# 6. Listado de las observaciones a nivel nacional agrupadas por  observatorio. El listado debe estar ordenado ascendentemente por el promedio de las temperaturas . El listado muestra código y nombre del observatorio y el promedio de las temperaturas.


import json
import time


# FUNCIONES


# funcion ordenamiento burbuja para cadenas
def burbuja_optimus(lstLibros):
    n = len(lstLibros)
    # print(lstLibros)
    for i in range(n-1):
        intercambio = False
        for j in range(n-1-i):
            # k -> llave del codigo de la posición j de la lista
            # k1 -> llave del codigo de la posicion j+1 de la lista
            k = list(lstLibros[j].items())[0][1]["fechaYear"]
            k1 = list(lstLibros[j+1].items())[0][1]["fechaYear"]
            #print(list(lstLibros[j].items())[0][0]["fechaYear"])
            # print("K, K+1,  ", k, k1)
            if k == k1:
                for i2 in range(n-1):
                    intercambio = False
                    for j2 in range(n-1-i2):
                        m = list(lstLibros[j2].items())[0][1]["fechaMes"]
                        m1 = list(lstLibros[j2+1].items())[0][1]["fechaMes"]
                        if m > m1:
                            lstLibros[j2], lstLibros[j2+1] = lstLibros[j2+1], lstLibros[j2]
                            intercambio = True

            elif k > k1:
                lstLibros[j], lstLibros[j+1] = lstLibros[j+1], lstLibros[j]
                intercambio = True

        if intercambio == False:
            break
    return lstLibros

# funcion listar observatorios por código
def listarPorCodigo(lstObservatorios):
    n = len(lstObservatorios)
    # print(lstObservatorios)

    for i in range(n-1):
        intercambio = False
        for j in range(n-1-i):
            # k -> llave del codigo de la posición j de la lista
            # k1 -> llave del codigo de la posicion j+1 de la lista
            k = list(lstObservatorios[j].items())[0][0]
            k1 = list(lstObservatorios[j+1].items())[0][0]
            # print(list(lstObservatorios[j].items())[0][1]["titulo"])
            #print("K, K+1, nombre: ", k, k1, nom)
            if k > k1:
                lstObservatorios[j], lstObservatorios[j+1] = lstObservatorios[j+1], lstObservatorios[j]
                intercambio = True
        if intercambio == False:
            break
    ini = 0
    fin = len(lstObservatorios)
    print("\n{:<20} {:<20} {:<20} {:<20}\n".format("Código", "Nombre", "Temp Máx", "Temp Mín"))
    for i in range(ini,fin):
            if i >= len(lstObservatorios):
                return
            else:  
                for elemento in lstObservatorios[i]:  
                    #print(f"{lstObservatorios[i][elemento]['titulo']}\t\t\t{lstObservatorios[i][elemento]['autor']}\t\t\t${lstObservatorios[i][elemento]['precio']:,}")
                    #print(list(lstObservatorios[i].keys())[0])
                    codigo = list(lstObservatorios[i].keys())[0]
                    print("{:<20} {:<20} {:<20} {:<20}".format(codigo,lstObservatorios[i][elemento]['nombre'],lstObservatorios[i][elemento]['temperaturaMax'],lstObservatorios[i][elemento]['temperaturaMin']))
    input("\nPresione Enter para regresar al menú: ")
    return lstObservatorios


# funcion listar libros por título
def listarObservNombre(lstObservatorios):
    ini = 0
    fin = len(lstObservatorios)
    n = len(lstObservatorios)
    # print(lstLibros)
    for i in range(n-1):
        intercambio = False
        for j in range(n-1-i):
            # k -> llave del codigo de la posición j de la lista
            # k1 -> llave del codigo de la posicion j+1 de la lista
            k = list(lstObservatorios[j].items())[0][1]["nombre"]
            k1 = list(lstObservatorios[j+1].items())[0][1]["nombre"]
            #print(list(lstLibros[j].items())[0][1]["titulo"])
            #print("K, K+1, nombre: ", k, k1, nom)
            if k > k1:
                lstObservatorios[j], lstObservatorios[j+1] = lstObservatorios[j+1], lstObservatorios[j]
                intercambio = True
        if intercambio == False:
            break
    print("\n{:<20} {:<20} {:<20} {:<20}\n".format("Nombre", "Temp Máx", "Temp Mín", "Código"))
    for i in range(ini,fin):
        if i >= len(lstObservatorios):
            return
        else:  
            for elemento in lstObservatorios[i]:  
                codigo = list(lstObservatorios[i].keys())[0]
                print("{:<20} {:<20} {:<20} {:<20}".format(lstObservatorios[i][elemento]['nombre'],lstObservatorios[i][elemento]['temperaturaMax'],lstObservatorios[i][elemento]['temperaturaMin'], codigo))
    input("\nPresione Enter para regresar al menú: ")
    return lstObservatorios

def listarCantObservaciones(lstObservatorios):
    contador = 0
    sumaPromedioDia = 0
    observatorio = input("Ingrese el codigo del observatorio: ")
    n = len(lstObservatorios)
    # print(lstObservatorios)

    for i in range(n-1):
        intercambio = False
        for j in range(n-1-i):
            # k -> llave del codigo de la posición j de la lista
            # k1 -> llave del codigo de la posicion j+1 de la lista
            k = list(lstObservatorios[j].items())[0][0]
            k1 = list(lstObservatorios[j+1].items())[0][0]
            # print(list(lstObservatorios[j].items())[0][1]["titulo"])
            #print("K, K+1, nombre: ", k, k1, nom)
            if k > k1:
                lstObservatorios[j], lstObservatorios[j+1] = lstObservatorios[j+1], lstObservatorios[j]
                intercambio = True
        if intercambio == False:
            break
    ini = 0
    fin = len(lstObservatorios)
    print("\n{:<20} {:<20} {:<20} {:<20} {:<20}".format("Código", "Nombre", "Temp Máx", "Temp Mín", "Promedio Día\n"))
    for i in range(ini,fin):
            if i >= len(lstObservatorios):
                return
            else:  
                for elemento in lstObservatorios[i]:  
                    #print(f"{lstObservatorios[i][elemento]['titulo']}\t\t\t{lstObservatorios[i][elemento]['autor']}\t\t\t${lstObservatorios[i][elemento]['precio']:,}")
                    #print(list(lstObservatorios[i].keys())[0])
                    codigo = list(lstObservatorios[i].keys())[0]
                    if observatorio == codigo:
                        contador += 1
                        sumaTempMax = lstObservatorios[i][elemento]['temperaturaMax']
                        sumaTempMin = lstObservatorios[i][elemento]['temperaturaMin']
                        promedioDia = (sumaTempMax + sumaTempMin) / 2
                        sumaPromedioDia += promedioDia
                        promedioTotal = sumaPromedioDia / contador
                        print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(codigo,lstObservatorios[i][elemento]['nombre'],lstObservatorios[i][elemento]['temperaturaMax'],lstObservatorios[i][elemento]['temperaturaMin'],promedioDia))
    print(f"\nLa cantidad de observaciones es : {contador}")
    print(f"\nEl promedio total de la temperatura del observatorio de código {observatorio} es: {promedioTotal}\n")
    input("Presione Enter para volver al menú.")
    return lstObservatorios

def listadoParticularPorFecha(lstObservatorios):
    observatorio = input("Ingrese el codigo del observatorio: ")
    n = len(lstObservatorios)
    # print(lstObservatorios)

    for i in range(n-1):
        intercambio = False
        for j in range(n-1-i):
            # k -> llave del codigo de la posición j de la lista
            # k1 -> llave del codigo de la posicion j+1 de la lista
            k = list(lstObservatorios[j].items())[0][1]["fechaYear"]
            k1 = list(lstObservatorios[j+1].items())[0][1]["fechaYear"]
            #print(list(lstObservatorios[j].items())[0][0]["fechaYear"])
            # print("K, K+1,  ", k, k1)
            if k == k1:
                for i2 in range(n-1):
                    intercambio = False
                    for j2 in range(n-1-i2):
                        m = list(lstObservatorios[j2].items())[0][1]["fechaMes"]
                        m1 = list(lstObservatorios[j2+1].items())[0][1]["fechaMes"]
                        if m > m1:
                            lstObservatorios[j], lstObservatorios[j+1] = lstObservatorios[j+1], lstObservatorios[j]
                            intercambio = True

            elif k > k1:
                lstObservatorios[j], lstObservatorios[j+1] = lstObservatorios[j+1], lstObservatorios[j]
                intercambio = True

        if intercambio == False:
            break
    ini = 0
    fin = len(lstObservatorios)
    print("\n{:<20} {:<20} {:<20} {:<20} {:<20}".format("Código", "Nombre", "Temp Máx", "Temp Mín", "Fecha"))
    for i in range(ini,fin):
            if i >= len(lstObservatorios):
                return
            else:  
                for elemento in lstObservatorios[i]:  
                    #print(f"{lstObservatorios[i][elemento]['titulo']}\t\t\t{lstObservatorios[i][elemento]['autor']}\t\t\t${lstObservatorios[i][elemento]['precio']:,}")
                    #print(list(lstObservatorios[i].keys())[0])
                    codigo = list(lstObservatorios[i].keys())[0]
                    if observatorio == codigo:
                        contador = 0
                        contador += 1
                        sumaPromedioDia = 0
                        sumaTempMax = lstObservatorios[i][elemento]['temperaturaMax']
                        sumaTempMin = lstObservatorios[i][elemento]['temperaturaMin']
                        promedioDia = (sumaTempMax + sumaTempMin) / 2
                        sumaPromedioDia += promedioDia
                        promedioTotal = sumaPromedioDia / contador
                        print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(codigo,lstObservatorios[i][elemento]['nombre'],lstObservatorios[i][elemento]['temperaturaMax'],lstObservatorios[i][elemento]['temperaturaMin'],lstObservatorios[i][elemento]['fecha']))
    print(f"\nEl promedio de la temperatura del observatorio de código {observatorio} es: {promedioTotal}\n")
    input("Presione Enter para volver al menú.")
    return lstObservatorios


def listadoNacionalPorCodigo(lstObservatorios):
    ini = 0
    fin = 10
    n = len(lstObservatorios)
    # print(lstObservatorios)

    for i in range(n-1):
        intercambio = False
        for j in range(n-1-i):
            # k -> llave del codigo de la posición j de la lista
            # k1 -> llave del codigo de la posicion j+1 de la lista
            k = list(lstObservatorios[j].items())[0][0]
            k1 = list(lstObservatorios[j+1].items())[0][0]
            # print(list(lstObservatorios[j].items())[0][1]["titulo"])
            #print("K, K+1, nombre: ", k, k1, nom)
            if k > k1:
                lstObservatorios[j], lstObservatorios[j+1] = lstObservatorios[j+1], lstObservatorios[j]
                intercambio = True
        print()
        if intercambio == False:
            break
    print("{:<20} {:<20} {:<20} {:<20}".format("Código", "Nombre", "Temp Máx", "Temp Mín"))
    while True:
        for i in range(ini,fin):
                if i >= len(lstObservatorios):
                    return
                else:  
                    for elemento in lstObservatorios[i]:  
                        #print(f"{lstObservatorios[i][elemento]['titulo']}\t\t\t{lstObservatorios[i][elemento]['autor']}\t\t\t${lstObservatorios[i][elemento]['precio']:,}")
                        #print(list(lstObservatorios[i].keys())[0])
                        codigo = list(lstObservatorios[i].keys())[0]
                        print("{:<20} {:<20} {:<20} {:<20}".format(codigo,lstObservatorios[i][elemento]['nombre'],lstObservatorios[i][elemento]['temperaturaMax'],lstObservatorios[i][elemento]['temperaturaMin']))
        while True:
            continuar = input("\nSi desea continuar digite 1, si quiere salir presione 2: ")
            print("")
            if continuar < 1 or continuar > 2:
                print("Ingrese una opción valida")
                continue
            break
        if continuar == 2:
            return
        ini +=10
        fin +=10
    return lstObservatorios

# funcion que guarda la informacion en el json
def guardarObservatorios(lstObservatorios , ruta): 
    
    try: 
        fd = open(ruta , "w") # Abre el archivo
    except Exception as e: 
        print("Error al abrir el archivo para guardar los observatorios\n" , e) 
        return []
    
    try: 
        json.dump(lstObservatorios, fd) # Guarda el archivo json
    except Exception as e: 
        print("Error al guardar la informacion de los observatorios\n" , e)
        return []

    fd.close() # Cierra el archivo
    return True


# funcion que agrega los observatorios a la lista -> lstObservatorios
def agregarObservatorios(lstObservatorios, ruta, ruta2):
    fd = open(ruta, "r")
    fd2 = open(ruta2, "w")
    for linea in fd:
        if not linea.startswith("CODIGO"):
            datos = linea.split(";")
            codigo = datos[0]
            nombre = datos[1]
            temperaturaMax = float(datos[2])
            temperaturaMin = float(datos[3])
            # ingresar fecha del registro
            fechaDia = time.localtime()[2]
            fechaMes = time.localtime()[1]
            fechaYear = time.localtime()[0]
            fecha = f"{time.localtime()[0]}/{time.localtime()[2]}/{time.localtime()[1]}"


            # *Prueba*
            dicObservatorio = {}
            dicObservatorio[codigo] = {"nombre": nombre, "temperaturaMax": temperaturaMax,"temperaturaMin": temperaturaMin, "fecha": fecha, "fechaYear": fechaYear, "fechaMes": fechaMes, "fechaDia": fechaDia}
            lstObservatorios.append(dicObservatorio)
            # *Finprueba*
            """
            uniLstObservatorio = [0,0]
            uniLstObservatorio[0] = int(codigo)
            diccObservatorio = {}
            uniLstObservatorio[1] = {"nombre": nombre, "temperaturaMax": temperaturaMax,"temperaturaMin": temperaturaMin, "fecha": fecha}
            lstObservatorios.append(uniLstObservatorio)
            print(lstObservatorios)
            """
    fd.close()
    fd2.close()
    # aquí guarda los observatorios en el json
    if guardarObservatorios(lstObservatorios , ruta2)  == True:

        print("Los datos han sido registrado con exito\n")
        return lstObservatorios
    
    else: 
        input("Ocurrio algun error al guardar el libro. \nPresione Enter para continuar")


# funcion menu
def menu():
    while True:
        try:
            print("\n*** Servicios Meteorológicos ACME ***\n".center(40))
            print("MENU\n".center(40))
            print("1. Listado de observatorios ordenado por código ")
            print("2. Listado de observatorios ordenado por nombre ")
            print("3. Listado de observaciones de un observatorio en particular(Ingrese su código). Ordenadas por año, dia y mes ")
            print("4. Listado cantidad de observaciones ")
            print("5. Listado de todas las observaciones a nivel nacional ordenadas por código y paginadas cada 10 items")
            print("6. Listado de las observaciones a nivel nacional agrupadas por observatorio. ")
            print("7. Salir \n")
            op = int(input(">>> Opción (1-7)? "))
            if op < 1 or op > 8:
                print("Opción no válida. Escoja de 1 a 7.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 7.")
            input("Presione cualquier tecla para continuar...")


# función para cargar archivo
def cargarInfo(lstObservatorios, rutaObservatorios): 
    try: 
        fd = open(rutaObservatorios, "r") #Fd es la apertura del archivo
    except Exception as e:  
        try: 
            fd = open(rutaObservatorios , "w")  
        except Exception as d:  
            print("Error al intentar abrir el archivo\n" , d) 
            return None 
    try:
        linea = fd.readline()
        if linea.strip() != "": # Si tiene el archivo algo de contenido cargará los datos, sino creará una lista vacia.
            fd.seek(0) # Posiciona el puntero en 0
            lstObservatorios = json.load(fd) # json.load() --> carga el archivo
        else: 
            lstObservatorios = []
    except Exception as e: 
        print("Error al cargar la informacion\n" , e) 
        return []
    
    # print(lstPersonal) # -> imprime si el archivo existe
    fd.close() #Si se carga todo cierre el archivo
    return lstObservatorios #Devuelve la lista cargada


# Programa principal

rutaFile = "Filtro/datos.csv"
rutaObservatorios = "Filtro/observatorios.json"
lstObservatorios = []
lstObservatorios = cargarInfo(lstObservatorios, rutaObservatorios)
lstObservatorios = agregarObservatorios(lstObservatorios, rutaFile,rutaObservatorios)

burbuja_optimus(lstObservatorios)


while True:
    op = menu()
    if op == 1:
        listarPorCodigo(lstObservatorios)
    elif op == 2:
        listarObservNombre(lstObservatorios)
    elif op == 3:
        listadoParticularPorFecha(lstObservatorios)
    elif op == 4:
        listarCantObservaciones(lstObservatorios)
    elif op == 5:
        listadoNacionalPorCodigo(lstObservatorios)
    elif op == 6:
        listarLibrosAutor(lstLibros)
        pass
    elif op == 7:
        print("Gracias por usar el software") 
        break