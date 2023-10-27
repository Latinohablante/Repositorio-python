"""
El proceso que se ha seguido es el siguiente:

1. Se crea una función que inicialice el juego (inicializar_juego):
    - Esta función da valor True a la variable juego_en_curso, encargada de ser un flag para terminar el juego.
    - Crea una lista de dos elementos, cada elemento es un jugador, cada jugador es una lista de otros dos elementos que son su nombre y su valor representado en el tablero (X y O).
    - Elige de forma aleatoria el jugador actual.
    - Crea el tablero, es una lista con tres elementos, cada elemento es una línea del tablero.
    - Devuelve los valores incializados.
2. Se crea una función para actualizar el tablero (actualizar_tablero):
    - Recibe como parámetros el jugador del turno actual, las coordenadas que a elegido el jugador y el estado del tablero actualmente.
    - Actualiza la casilla que a seleccionado el jugador, colocando en su lugar una X o una O, dependiendo del jugador actual. A la coordenada se resta 1 para seleccionar la ubicación correcta a marcar (las listas comienzan por 0).
    - Devuelve el tablero actual.
3. Se crea una función para comprobar si el tablero está completo (tablero_completo):
    - Recibe como parámetro el tablero actual.
    - Devuelve True si no quedan huecos en el tablero, en caso contrario False.
4. Se crea una función para comprobar si el jugador a ganado (comprobar_ganador):
    - Recibe como parámetros el jugador actual y el tablero actual.
    - Realiza comprobaciones por filas, columnas y diagonales para ver si el jugador actual ha ganado el juego, en caso de ganar devuelve True si no devuelve False.
5. Ahora se inicializa el juego llamando a la función inicializar_juego y guardando los valores que devuelve en variables.
6. A continuación se crea un bucle controlado por la variable juego_en_curso.
    - Lo primero que hacemos en el bucle es comprobar si el tablero esta completo, llamando a la función tablero_completo, si está lleno damos valor False a la variable juego_en_curso, rompemos el bucle principal e informamos al usuario de que no hay ganador.
    - Limpiamos siempre la pantalla con os.system(«cls»).
    - Imprime un mensaje con el nombre del jugador actual.
    - Dibujamos el tablero, con las coordenadas horizontales y verticales.
    - Imprime un mensaje indicando que seleccione coordenadas, se deben introducir dos números consecutivos, sin espacios, que serán las coordenadas elegidas por el jugador.
    - Se actualiza el tablero mediante la función actualizar_tablero.
    - Comprobamos si el jugador a ganado mediante la función comprobar_ganador, si el jugador a ganado damos valor False a la variable juego_en_curso, se imprime el tablero con el resultado final y un mensaje indicando el nombre del ganador.
    - Cambiamos de un jugador a otro, para ello damos valor 0 a la variable jugador_actual cuando tenga valor 1 y viceversa.

Para mejorar:

El juego permite introducir coordenadas ya utilizadas y sobre escribir huecos, debería de controlarse que no lo permita.
Se repite código en varios lugares, deberían de crearse funciones para evitarlo, por ejemplo para imprimir el tablero.
Se puede eliminar el uso de funciones y crear el juego en una clase, para que funcione mediante programación orientada a objetos, pensad que cada nuevo juego podría ser un objeto.

"""
import json
import os
import time



# Funcion que carga el archivo json
def cargarInfo(lstGanadores, rutaGanadores):
    try: 
        fd = open(rutaGanadores, "r") #Fd es la apertura del archivo
    except Exception as e:  

        try: 
            fd = open(rutaGanadores , "w")  
        except Exception as d:  
            print("Error al intentar abrir el archivo\n" , d) 
            return [] 
    try:
        linea = fd.readline()
        if linea.strip() != "": # Si tiene el archivo algo de contenido cargará los datos, sino creará una lista vacia.
            fd.seek(0) # Posiciona el puntero en 0
            lstGanadores = json.load(fd) # json.load() --> carga el archivo
        else: 
            lstGanadores = []
    except Exception as e:
        print("Error al cargar la informacion\n" , e) 
        return [] 
    
    # print(lstPersonal) # -> imprime si el archivo existe
    fd.close() #Si se carga todo cierre el archivo
    return lstGanadores #Devuelve la lista cargada

# Funcion que guarda al ganador
def guardarGanador(lstGanadores , ruta): 
    
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

# funcion ordenamiento burbuja para cadenas
def burbuja_optimus(lstGanadores):
    n = len(lstGanadores)
    # print(lstLibros)
    for i in range(n-1):
        intercambio = False
 
        for j in range(n-1-i):
            # k -> llave del codigo de la posición j de la lista
            # k1 -> llave del codigo de la posicion j+1 de la lista
            k = list(lstGanadores[j].items())[0][0]
            k1 = list(lstGanadores[j+1].items())[0][0]
            print(list(lstGanadores[j].items())[0][1]["movimientos"])
            #print("K, K+1, nombre: ", k, k1, nom)
            if k > k1:
                lstGanadores[j], lstGanadores[j+1] = lstGanadores[j+1], lstGanadores[j]
                intercambio = True
 
        if intercambio == False:
            break
    return lstGanadores


# funcion listar Ganadores
def listarGanadores(lstGanadores):
    ini = 0
    fin = len(lstGanadores)
    n = len(lstGanadores)
    # print(lstGanadores)
    for i in range(n-1):
        intercambio = False
        for j in range(n-1-i):
            # k -> llave del codigo de la posición j de la lista
            # k1 -> llave del codigo de la posicion j+1 de la lista
            k = list(lstGanadores[j].items())[0][1]["movimientos"]
            k1 = list(lstGanadores[j+1].items())[0][1]["movimientos"]
            
            #print(list(lstGanadores[j].items())[0][1]["titulo"])
            #print("K, K+1, nombre: ", k, k1, nom)
            
            if k == k1:
                for l in range(n-1):
                    intercambio = False
                    for f in range(n-1-l):
                        # k -> llave del codigo de la posición j de la lista
                        # k1 -> llave del codigo de la posicion j+1 de la lista
                        m = list(lstGanadores[f].items())[0][1]["tiempo"]
                        m1 = list(lstGanadores[f+1].items())[0][1]["tiempo"]
                        if m > m1:
                            lstGanadores[j], lstGanadores[j+1] = lstGanadores[j+1], lstGanadores[j]
                            intercambio = True
            elif k > k1:
                lstGanadores[j], lstGanadores[j+1] = lstGanadores[j+1], lstGanadores[j]
                intercambio = True

        if intercambio == False:
            break
    #print(f"\nTítulo \t\t\tAutor \t\t\tPrecio \t\tcódigo")
    print("{:<20} {:<20} {:<20}".format("movimientos", "tiempo", "Nombre"))
    while True:
        for i in range(ini,fin):
            if i >= len(lstGanadores):
                return
            else:  
                for elemento in lstGanadores[i]:  
                    #print(f"{lstGanadores[i][elemento]['titulo']}\t\t\t{lstGanadores[i][elemento]['autor']}\t\t\t${lstGanadores[i][elemento]['precio']:,}")
                    print("{:<20} {:<20} {:<20}".format(lstGanadores[i][elemento]['movimientos'],lstGanadores[i][elemento]['tiempo'],list(lstGanadores[i].keys())[0]))
        while True:
            continuar = int(input("\nSi desea continuar digite 1, si quiere salir presione 2: "))
            if continuar < 1 or continuar > 2:
                print("Ingrese una opción valida")
                continue
            break
        if continuar == 2:
            return
        # ini +=5
        # fin +=5
    return lstGanadores



def seleccionCasilla():
    while True:
        try:
            op = int(input(">>> Opción (1-9)? "))
            if op < 1 or op > 9:
                print("Opción no válida. Escoja de 1 a 9.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 9.")
            input("Presione cualquier tecla para continuar...")

# Funcion que analiza si existe el nombre en el archivo json
def existeNombre(nombre, lstGanadores): 
    for datos in lstGanadores:  
        k = str(list(datos.keys())[0]) # Devuelve la lista de las llaves pero se debe colocar el list para que la ordene correctamente en la lista y el [0] para que tome la posición 0 que en este caso es el nombre del jugador
        if k == nombre:
            return True 
    return False


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

# Funcion que pregunta la ficha al jugador 1
def fichaJugador(nombre,lstJugadores):
    while True:
        try:
            ficha = input(f"{nombre} Ingrese la ficha con la que quiere jugar [ X ] o [ O ]: ")
            if ficha.lower() == "x" or ficha.lower() == "o":
                list(lstJugadores[0].items())[0][1]["ficha"] = ficha
                break
            else:
                print("Elección inválida. Ingrese [ x ] o [ o ]")
                continue
        except ValueError:
            print("Error. Elección inválida.")
    return ficha

# Funcion que asigna la ficha al jugador 2
def fichaJugador2(lstJugadores):
    ficha1 = list(lstJugadores[0].items())[0][1]["ficha"]
    # ficha2 = list(lstJugadores[1].items())[0][1]["ficha"]
    # print(ficha2)
    
    if ficha1.lower() == "x":
        list(lstJugadores[1].items())[0][1]["ficha"] = "o"
    elif ficha1.lower() == "o":
        list(lstJugadores[1].items())[0][1]["ficha"] = "x"
    return list(lstJugadores[1].items())[0][1]["ficha"]

# funcion agregar nombre de jugador 1
def agregarJugador1(lstGanadores,lstJugadores, ruta): 

    nombre = leerNombreJugador("Ingrese el nombre del jugador 1: ")
    

    while  existeNombre(nombre , lstGanadores):
        print("-> Ya existe un jugador con ese nombre en la tabla de Ganadores") 
        input("Presione Enter para continuar")
        nombre = leerNombreJugador("Ingrese el nombre del jugador 1: ")

    movimientos = 0
    tiempo = 0
    ficha = ""
    dicJugador = {}
    dicJugador[nombre] = {"movimientos":movimientos,"tiempo":tiempo,"ficha":ficha}
    lstJugadores.append(dicJugador)
    ficha = fichaJugador(nombre,lstJugadores)
    # burbuja_optimus(lstGanadores)

    # if guardarJugador(lstGanadores , ruta)  == True:

    #     input("El Jugador ha sido guardado en la lista de jugadores con éxito.\nPresione Enter para continuar")
    
    # else: 
    #     input("Ocurrió algún error al guardar al jugador. \nPresione Enter para continuar")

def agregarJugador2(lstGanadores,lstJugadores, ruta): 

    nombre = leerNombreJugador("Ingrese el nombre del jugador 2: ")
    
    while  existeNombre(nombre , lstGanadores):  
        print("-> Ya existe un jugador con ese nombre en la tabla de Ganadores") 
        input("Presione Enter para continuar")
        nombre = leerNombreJugador("Ingrese el nombre del jugador 2: ")

    movimientos = 0
    tiempo = 0
    ficha = ""
    dicJugador = {}
    
    dicJugador[nombre] = {"movimientos":movimientos,"tiempo":tiempo,"ficha":ficha}
    lstJugadores.append(dicJugador)
    ficha = fichaJugador2(lstJugadores)
    # list(lstJugadores[1].items())[0][1]["ficha"] = ficha



def inicializar_juego():
    """Función que inicializa los valores del juego"""
    juego_en_curso = True
    #lstJugadores = []
    jugador1 = agregarJugador1(lstGanadores,lstJugadores, rutaGanadores)
    jugador2 = agregarJugador2(lstGanadores,lstJugadores, rutaGanadores)
    # lstJugadores = [[input("Jugador 1: "),"x"], [input("Jugador 2: "),"o"]]
    jugador_actual = 0
    tablero = [[7,8,9],[4,5,6],[1,2,3]]
    return juego_en_curso, lstJugadores, jugador_actual, tablero

def poner_ficha(jugador,coordenada_fila, coordenada_columna, tablero_actual,jugador_actual):
    posicion = tablero_actual[coordenada_fila - 1][coordenada_columna - 1]
    # valido si ya hay fichas en la casilla
    if posicion == "x" or posicion == "o":
        # = 1 if jugador_actual == 0 else 0
        return True
    else:
        return False
        

def actualizar_tablero(jugador, coordenada_fila, coordenada_columna, tablero_actual,jugador_actual):
    """Actualiza el tablero con la acción del jugador actual"""
    posicion = tablero_actual[coordenada_fila - 1][coordenada_columna - 1]
    
    #print(list(jugador.items())[0][1]["ficha"])
    #input()
    # valido si ya hay fichas en la casilla
    if posicion == "x" or posicion == "o":
        #jugador_actual = 1 if jugador_actual == 0 else 0
        input("Esa casilla ya tiene una ficha. Presione Enter para continuar")
        #return tablero_actual, jugador_actual
    else:
        # asigna la ficha del jugador a la posición escogida
        #tablero_actual[coordenada_fila - 1][coordenada_columna - 1] = jugador[1]
        tablero_actual[coordenada_fila - 1][coordenada_columna - 1] = list(jugador.items())[0][1]["ficha"]
        
    return tablero_actual

def tablero_completo(tablero_actual):
    """Comprueba si el tablero está completo, devuelve True o False"""
    for linea in tablero_actual:
        for celda in linea:
            if celda in range(1,10):
                return False
    return True

def comprobar_ganador(jugador, tablero_actual):
    """Comprueba si ha ganado el jugador actual, devuelve True o False"""
    #Comprobar por filas
    for i in range(3):
        ganador = True
        for x in range(3):
            if tablero_actual[i][x] != list(jugador.items())[0][1]["ficha"]:
                ganador = False
                break
        if ganador:
            return ganador
    #Comprobar por columnas
    for i in range(3):
        ganador = True
        for x in range(3):
            if tablero_actual[x][i] != list(jugador.items())[0][1]["ficha"]:
                ganador = False
                break
        if ganador:
            return ganador
    #Comprobar por diagonales
    ganador = True
    for i in range(3):
        if tablero_actual[i][i] != list(jugador.items())[0][1]["ficha"]:
            ganador = False
            break
    if ganador:
        return ganador
    ganador = True
    
    # diagonal inversa
    for i in range(3):
        if tablero_actual[i][3 - 1 - i] != list(jugador.items())[0][1]["ficha"]:
            ganador = False
            break
    if ganador:
        return ganador
    
    return False

# juego_en_curso, lstJugadores, jugador_actual, tablero = inicializar_juego()


def jugando():
    juego_en_curso, lstJugadores, jugador_actual, tablero = inicializar_juego()
    while juego_en_curso:
        if tablero_completo(tablero):
            juego_en_curso = False
            os.system("cls")
            print("Fin del juego, no hay ganador")
            break
        os.system("cls")
        #Nuevo turno
        print("Turno de: ", list(lstJugadores[jugador_actual].keys())[0])
        #Dibujar tablero
        for linea in tablero:
            print(linea[0],"|", linea[1],"|", linea[2])

        # print("0 1 2 3")
        # coordenadas_vertical = 1
        # for linea in tablero:
        #     print(coordenadas_vertical, linea[0], linea[1], linea[2])
        #     coordenadas_vertical += 1

        #Selección de casilla
        while True:
            
            if jugador_actual == 0:
                list(lstJugadores[jugador_actual].items())[0][1]["movimientos"] += 1
                lstJugadores[jugador_actual]
                comienzoTiemJug1 = time.time()
                op = seleccionCasilla()
                finalTiemJug1 = time.time()
                list(lstJugadores[jugador_actual].items())[0][1]["tiempo"] += finalTiemJug1 - comienzoTiemJug1
                print("Tiempo 1: ",list(lstJugadores[jugador_actual].items())[0][1]["tiempo"])
                print("Movimientos", list(lstJugadores[jugador_actual].items())[0][1]["movimientos"])
            else:
                list(lstJugadores[jugador_actual].items())[0][1]["movimientos"] += 1
                lstJugadores[jugador_actual]
                comienzoTiemJug2 = time.time()
                op = seleccionCasilla()
                finalTiemJug2 = time.time()
                list(lstJugadores[jugador_actual].items())[0][1]["tiempo"] += finalTiemJug2 - comienzoTiemJug2
                print("Tiempo 2: ",list(lstJugadores[jugador_actual].items())[0][1]["tiempo"])
                print("Movimientos", list(lstJugadores[jugador_actual].items())[0][1]["movimientos"])

            if op == 1:
                coordenada_fila, coordenada_columna = list(map(int,"31"))
                break
            elif op == 2:
                coordenada_fila, coordenada_columna = list(map(int,"32"))
                break 
            elif op == 3:
                coordenada_fila, coordenada_columna = list(map(int,"33"))
                break
            elif op == 4:
                coordenada_fila, coordenada_columna = list(map(int,"21"))
                break
            elif op == 5:
                coordenada_fila, coordenada_columna = list(map(int,"22"))
                break
            elif op == 6:
                coordenada_fila, coordenada_columna = list(map(int,"23"))
                break
            elif op == 7:
                coordenada_fila, coordenada_columna = list(map(int,"11"))
                break
            elif op == 8:
                coordenada_fila, coordenada_columna = list(map(int,"12"))
                break
            elif op == 9:
                coordenada_fila, coordenada_columna = list(map(int,"13"))
                break


        # Analiza si la posición elegida está ocupada
        ponerFicha = poner_ficha(lstJugadores[jugador_actual], coordenada_fila,coordenada_columna, tablero,jugador_actual)


        #Actualizar tablero
        tablero = actualizar_tablero(lstJugadores[jugador_actual], coordenada_fila, coordenada_columna, tablero,jugador_actual)

        #Comprobamos si ha ganado
        if comprobar_ganador(lstJugadores[jugador_actual], tablero):
            juego_en_curso = False

            #Dibujar tablero Ganador
            os.system("cls")
            print("Ganador: ",list(lstJugadores[jugador_actual].keys())[0])
            if lstGanadores is None:
                print("ingresando Ganador")
                guardarGanador(lstGanadores,rutaGanadores)
            else:
                lstGanadores.append(lstJugadores[jugador_actual])
            #print(lstGanadores)
            guardarGanador(lstGanadores,rutaGanadores)
            for linea in tablero:
                print(linea[0],"|", linea[1],"|", linea[2])
            input("Presione Enter para volver al menú")
            os.system("cls")

            # print("0 1 2 3")
            # coordenadas_vertical = 1
            #for linea in tablero:
                #print(coordenadas_vertical, linea[0], linea[1], linea[2])
                #coordenadas_vertical += 1


        #Cambio de jugador
        if ponerFicha == False:
            jugador_actual = 1 if jugador_actual == 0 else 0
        else:    
            continue
        # if jugador_actual == 0:
        #     jugador_actual = 1
        # else:
        #     jugador_actual = 0

# funcion menu

def menu():
    while True:
        try:
            print("*** JUEGO TIC TAC TOE ***".center(40))
            print("MENU".center(40))
            print("1. Jugar con un amigo ")
            print("2. Consultar tabla de posiciones")
            print("3. Salir ")
            op = int(input(">>> Opción (1-3)? "))
            if op < 1 or op > 3:
                print("Opción no válida. Escoja de 1 a 3.")
                input("Presione Enter para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 3.")
            input("Presione Enter para continuar...")


    # Programa principal

rutaGanadores = "Ciclo1-Python\Ejercicios-Entregar\Proyecto-Tic-Tac-Toe/probando.json"
lstGanadores = []
lstJugadores = []
lstGanadores = cargarInfo(lstGanadores, rutaGanadores)

while True:

    op = menu()

    if op == 1:
        lstJugadores = []
        jugando()
    elif op == 2:
        listarGanadores(lstGanadores)
        pass
    elif op == 3:
        print("Gracias por usar el software")
        break