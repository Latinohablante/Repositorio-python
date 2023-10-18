# BIENVENIDO AL CÓDIGO DEL JUEGO TIC-TAC-TOE
import json

# FUNCIONES

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

def fichaJugador():
    while True:
        try:
            ficha = input("Ingrese la ficha con la que quiere jugar [ X ] o [ O ]: ")
            if ficha != "X" or ficha != "O":
                print("Elección inválida. Ingrese [ X ] o [ O ]")
                continue
            break
        except ValueError:
            print("Error. Elección inválida.")

# funcion menu

def menu():
    while True:
        try:
            print("*** JUEGO TIC TAC TOE ***".center(40))
            print("MENU".center(40))
            print("1. Jugar con un amigo ")
            print("2. Consultar tabla de posiciones ")
            print("3. Salir ")
            op = int(input(">>> Opción (1-3)? "))
            if op < 1 or op > 3:
                print("Opción no válida. Escoja de 1 a 3.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 3.")
            input("Presione Enter para continuar...")

# Programa principal

rutaGanadores = "Ejercicios-Entregar/Proyecto-Tic-Tac-Toe/lst-Ganadores.json"
lstGanadores = []
lstLibros = cargarInfo(lstGanadores, rutaGanadores)

while True:

    op = menu()

    if op == 1:
        agregarLibro(lstLibros, rutaFile)
    elif op == 2:
        consultarLibro(lstLibros)
    elif op == 3:
        print("Gracias por usar el software") 
        break


jugador1 = leerNombreJugador("Ingrese el nombre del jugador 1: ")

jugador2 = leerNombreJugador("Ingrese el nombre del jugador 2: ")