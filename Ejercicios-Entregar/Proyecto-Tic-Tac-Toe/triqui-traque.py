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

import random
import os

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


def inicializar_juego():
    """Función que inicializa los valores del juego"""
    juego_en_curso = True
    jugadores = [[input("Jugador 1: "),"x"], [input("Jugador 2: "),"o"]]
    jugador_actual = random.randint(0, 1)
    tablero = [[7,8,9],[4,5,6],[1,2,3]]
    return juego_en_curso, jugadores, jugador_actual, tablero

def poner_ficha(jugador, coordenada_fila, coordenada_columna, tablero_actual,jugador_actual):
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
    # valido si ya hay fichas en la casilla
    if posicion == "x" or posicion == "o":
        jugador_actual = 1 if jugador_actual == 0 else 0
        input("Esa casilla ya tiene una ficha. Presione Enter para continuar")
        #return tablero_actual, jugador_actual
    else:
        # asigna la ficha del jugador a la posición escogida
        tablero_actual[coordenada_fila - 1][coordenada_columna - 1] = jugador[1]
    return tablero_actual
# def actualizar_tablero(jugador, coordenada_fila, coordenada_columna, tablero_actual):
#     """Actualiza el tablero con la acción del jugador actual"""
#     posicion = tablero_actual[coordenada_fila - 1][coordenada_columna - 1]
#     # valido si ya hay fichas en la casilla
#     if posicion == "x" or posicion == "o":
#         jugador_actual = 1 if jugador_actual == 0 else 0
#         input("Esa casilla ya tiene una ficha. Presione Enter para continuar")
#     else:
#         tablero_actual[coordenada_fila - 1][coordenada_columna - 1] = jugador[1]
#     return tablero_actual

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
            if tablero_actual[i][x] != jugador[1]:
                ganador = False
                break
        if ganador:
            return ganador
    #Comprobar por columnas
    for i in range(3):
        ganador = True
        for x in range(3):
            if tablero_actual[x][i] != jugador[1]:
                ganador = False
                break
        if ganador:
            return ganador
    #Comprobar por diagonales
    ganador = True
    for i in range(3):
        if tablero_actual[i][i] != jugador[1]:
            ganador = False
            break
    if ganador:
        return ganador
    ganador = True
    
    # diagonal inversa
    for i in range(3):
        if tablero_actual[i][3 - 1 - i] != jugador[1]:
            ganador = False
            break
    if ganador:
        return ganador
    
    return False

juego_en_curso, jugadores, jugador_actual, tablero = inicializar_juego()



while juego_en_curso:
    if tablero_completo(tablero):
        juego_en_curso = False
        os.system("cls")
        print("Fin del juego, no hay ganador")
        break
    os.system("cls")
    #Nuevo turno
    print("Turno de: " + jugadores[jugador_actual][0])
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

        op = seleccionCasilla()

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
    #coordenada_fila, coordenada_columna = list(map(int, input("Elige coordenadas: ")))
    
    ponerFicha = poner_ficha(jugadores[jugador_actual], coordenada_fila,coordenada_columna, tablero,jugador_actual)

    
    #Actualizar tablero
    tablero = actualizar_tablero(jugadores[jugador_actual], coordenada_fila, coordenada_columna, tablero,jugador_actual)
    
    #Comprobamos si ha ganado
    if comprobar_ganador(jugadores[jugador_actual], tablero):
        juego_en_curso = False
        
        #Dibujar tablero Ganador
        os.system("cls")
        print("Ganador: ",jugadores[jugador_actual][0])
        for linea in tablero:
            print(linea[0],"|", linea[1],"|", linea[2])
        
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