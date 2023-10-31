import time
import os

os.system("cls")
nombre = input("¿Cómo te llamas? ")
print(f"Hola {nombre}, es hora de jugar al ahorcado")
time.sleep(1)
input("Presiona Enter para empezar a adivinar")
os.system("cls")
time.sleep(0.5)
palabra = ""
tu_palabra = ""
vidas = 6

while vidas > 0:
    fallas = 0
    print(f"Tienes {vidas} vidas")
    for letra in palabra.lower():
        
        if letra.lower() in tu_palabra:
            print(letra, end=" ")
        else:
            print("_", end=" ")
            fallas += 1
    print("")
    if fallas == 0:
        input("Felicidades, ganaste. Presiona Enter para terminar")
        break
    tu_letra = input("Ingrese una letra: ")
    tu_palabra += tu_letra

    if tu_letra not in palabra:
        vidas -= 1
        input(f"Lo siento, {tu_letra} no está dentro de la palabra. Presiona Enter para continuar")
        
        if vidas == 0:
            print("Perdiste")
    else:
        print("Muy bien")
    os.system("cls")
        
        
        
        