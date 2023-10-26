# Insertar -> para insertar nuevos registros en el fichero de libros
# Consulta -> busca registros por código
import json

# funciones

# funcion ordenamiento burbuja para cadenas
# Aún no funciona esta parte del código


# def burbuja_optimus(arreglo,cod):
#     n = len(arreglo)
  
#     for i in range(n-1):
#         intercambio = False
 
#         for j in range(n-1-i):
#             if arreglo[j][f"{cod}"] > arreglo[j+1][f"{cod}"]:
#                 arreglo[j][f"{cod}"], arreglo[j+1][f"{cod}"] = arreglo[j+1][f"{cod}"], arreglo[j][f"{cod}"]
#                 intercambio = True
 
#         if intercambio == False:
#             break
#     return arreglo


# función guardar libro

def guardarLibro(lstLibros , ruta): 
    
    try: 
        fd = open(ruta , "w") # Abre el archivo
    except Exception as e: 
        print("Error al abrir el archivo para guardar el empleado\n" , e) 
        return None
    
    try: 
        json.dump(lstLibros, fd) # Guarda el archivo
    except Exception as e: 
        print("Error al guardar la informacion del libro\n" , e)
        return None

    fd.close() # Cierra el archivo
    return True


# funcion que analiza si el código del libro ya existe en el fichero

def existeCod(cod, lstLibros): 
    for datos in lstLibros:  
        k = str(list(datos.keys())[0]) # Devuelve la lista de las llaves pero se debe colocar el list para que la ordene correctamente en la lista
        if k == cod:
            return True 
    return False



# funcion agregar libro

def agregarLibro(lstLibros , ruta): 
    print("\n\n1. Agregar Libro") 

    cod = input("Ingrese el código del libro: ")

    while  existeCod(cod , lstLibros):  
        print("-> Ya existe un libro con ese código") 
        input("Presione Enter para continuar") 
        cod = input("\nIngrese el código: ")

    titulo = input("Título: ") 
    autor = input("Autor: ")
    precio = int(input("Precio: ")) 

    dicLibro = {}
    dicLibro[cod] = {"titulo":titulo , "autor":autor , "precio":precio} 

    lstLibros.append(dicLibro) 
    lstLibros = burbuja_optimus(lstLibros,cod)


    if guardarLibro(lstLibros , ruta)  == True:

        input("El libro ha sido registrado con exito,\nPresione Enter para continuar")
    
    else: 
        input("Ocurrio algun error al guardar el libro. \nPresione Enter para continuar")




# funcion menu

def menu():
    while True:
        try:
            print("*** LIBRERÍA ***".center(40))
            print("MENU".center(40))
            print("1. Ingresar libro ")
            print("2. Consultar libro ")
            print("3. Salir ")
            op = int(input(">>> Opción (1-3)? "))
            if op < 1 or op > 3:
                print("Opción no válida. Escoja de 1 a 3.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 3.")
            input("Presione cualquier tecla para continuar...")


# función para cargar archivo

def cargarInfo(lstLibros , ruta): 
    try: 
        fd = open(ruta, "r") #Fd es la apertura del archivo
    except Exception as e:  

        try: 
            fd = open(ruta , "w")  
        except Exception as d:  
            print("Error al intentar abrir el archivo\n" , d) 
            return None 
    try:
        linea = fd.readline()
        if linea.strip() != "": # Si tiene el archivo algo de contenido cargará los datos, sino creará una lista vacia.
            fd.seek(0) # Posiciona el puntero en 0
            lstLibros = json.load(fd) # json.load() --> carga el archivo
        else: 
            lstLibros = []
    except Exception as e: 
        print("Error al cargar la informacion\n" , e) 
        return None 
    
    # print(lstPersonal) # -> imprime si el archivo existe
    fd.close() #Si se carga todo cierre el archivo
    return lstLibros #Devuelve la lista cargada


# funcion mostrar libro

def mostrarLibro(lstLibros): 

    print("\n\n2. Consultar libro") 
    cod = input("Ingrese el código: ") 

    if not existeCod(cod , lstLibros): 
        print("El libro no está registrado en el fichero.") 
        input("Presione Eter para continuar")
        return
    
    for i in range(len(lstLibros)):  
        datos = lstLibros[i] 
        k = list(datos.keys())[0]
        if k == cod:
            for elemento in lstLibros[i]:
                print(f"Título: {lstLibros[i][elemento]['titulo']}") 
                print(f"Autor: {lstLibros[i][elemento]['autor']}") 
                print(f"Precio: ${lstLibros[i][elemento]['precio']:,}") 
                input("\nPresione Enter para continuar.")


# programa principal
rutaFile = "Ejercicios-Entregar/SVR17-libreria/lst-libros.json"
lstLibros= []
lstLibros = cargarInfo(lstLibros, rutaFile)

while True:

    op = menu()

    if op == 1:
        agregarLibro(lstLibros, rutaFile)
    elif op == 2:
        mostrarLibro(lstLibros)   
    elif op == 3:
        print("Gracias por usar el software") 
        break