# BIENVENIDO AL CÓDIGO DEL JUEGO TIC-TAC-TOE
import json

# FUNCIONES

# Funcion que guarda al ganador
def guardarJugador(lstGanadores , ruta): 
    
    try: 
        fd = open(ruta , "w") # Abre el archivo
    except Exception as e: 
        print("Error al abrir el archivo para guardar el jugador\n" , e) 
        return None
    
    try: 
        json.dump(lstGanadores, fd) # Guarda el archivo
    except Exception as e: 
        print("Error al guardar la informacion del jugador\n" , e)
        return None

    fd.close() # Cierra el archivo
    return True


# Funcion que analiza si existe el nombre en el archivo json
def existeNombre(nombre, lstGanadores): 
    for datos in lstGanadores:  
        k = str(list(datos.keys())[0]) # Devuelve la lista de las llaves pero se debe colocar el list para que la ordene correctamente en la lista y el [0] para que tome la posición 0 que en este caso es el nombre del jugador
        if k == nombre:
            return True 
    return False


# Funcion que carga el archivo json
def cargarInfo(lstGanadores, rutaGanadores):
    try: 
        fd = open(rutaGanadores, "r") #Fd es la apertura del archivo
    except Exception as e:  

        try: 
            fd = open(rutaGanadores , "w")  
        except Exception as d:  
            print("Error al intentar abrir el archivo\n" , d) 
            return None 
    try:
        linea = fd.readline()
        if linea.strip() != "": # Si tiene el archivo algo de contenido cargará los datos, sino creará una lista vacia.
            fd.seek(0) # Posiciona el puntero en 0
            lstGanadores = json.load(fd) # json.load() --> carga el archivo
        else: 
            lstGanadores = []
    except Exception as e: 
        print("Error al cargar la informacion\n" , e) 
        return None 
    
    # print(lstPersonal) # -> imprime si el archivo existe
    fd.close() #Si se carga todo cierre el archivo
    return lstGanadores #Devuelve la lista cargada

# función que lee el nombre del jugador
def leerNombreJugador(msj):
    while True:
        try:
            nom = input(msj)
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def fichaJugador(jugador1,lstGanadores):
    while True:
        try:
            ficha = input(f"{jugador1} Ingrese la ficha con la que quiere jugar [ X ] o [ O ]: ")
            if ficha.lower() == "x" or ficha.lower() == "o":
                list(lstGanadores[jugador1].items())[0][1]["ficha"] = ficha
                break
            else:
                print("Elección inválida. Ingrese [ x ] o [ o ]")
                continue
        except ValueError:
            print("Error. Elección inválida.")

# funcion agregar nombre de jugador
def agregarJugador(lstGanadores,lstJugadores, ruta): 
    print("\n\n Agregar Jugador") 

    nombre = leerNombreJugador("Ingrese el nombre del jugador: ")
    
    while  existeNombre(nombre , lstGanadores):  
        print("-> Ya existe un jugador con ese nombre en la tabla de Ganadores") 
        input("Presione Enter para continuar")
        break
    nombre = input("\nIngrese el nombre del jugador: ")


    movimientos = input("Movimientos: (Aquí van los movimientos)")
    tiempo = input("Tiempo: (Esta parte hay que arreglarla)")
    ficha = fichaJugador()


    dicJugador = {}
    dicJugador[nombre] = {"movimientos":movimientos,"tiempo":tiempo,"ficha":ficha}

    lstJugadores.append(dicJugador)
    # burbuja_optimus(lstLibros)

    if guardarJugador(lstGanadores , ruta)  == True:

        input("El Jugador ha sido guardado en la lista de jugadores con éxito.\nPresione Enter para continuar")
    
    else: 
        input("Ocurrió algún error al guardar al jugador. \nPresione Enter para continuar")



# funcion menu

def menu():
    while True:
        try:
            print("*** JUEGO TIC TAC TOE ***".center(40))
            print("MENU".center(40))
            print("1. Jugar con un amigo ")
            print("2. Consultar tabla de posiciones")
            print("3. Reglas del juego")
            print("4. Salir ")
            op = int(input(">>> Opción (1-4)? "))
            if op < 1 or op > 4:
                print("Opción no válida. Escoja de 1 a 4.")
                input("Presione Enter para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 4.")
            input("Presione Enter para continuar...")

# Programa principal

rutaGanadores = "Ejercicios-Entregar/Proyecto-Tic-Tac-Toe/lst-Ganadores.json"
lstGanadores = []
lstJugadores = []
lstGanadores = cargarInfo(lstGanadores, rutaGanadores)

while True:

    op = menu()

    if op == 1:
        jugador1 = agregarJugador(lstGanadores,lstJugadores,rutaGanadores)
        jugador2 = agregarJugador(lstGanadores,lstJugadores,rutaGanadores)
        ficha = fichaJugador(jugador1)
    elif op == 2:
        consultarLibro(lstLibros)
    elif op == 3:
        consultarLibro(lstLibros)
    elif op == 4:
        print("Gracias por usar el software")
        break


