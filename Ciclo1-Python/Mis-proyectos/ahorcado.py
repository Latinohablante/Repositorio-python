import time

nombre = input("¿Cómo te llamas? ")
print(f"Hola {nombre}, es hora de jugar al ahorcado")
time.sleep(1)
print("Comienza a adivinar")
time.sleep(0.5)
palabra = "Avioneta"
tu_palabra = ""
vidas = 6

while vidas > 0:
    fallas = 0
    for letra in palabra:
        if letra in tu_palabra:
            print(letra, end=" ")
        else:
            print("_", end=" ")
            fallas += 1
    print("")
    if fallas == 0:
        print("Felicidades, ganaste")
        break
    tu_letra = input("Ingrese una letra: ")
    tu_palabra += tu_letra

    if tu_letra not in palabra:
        vidas -= 1
        print(f"Lo siento, {tu_letra} no está dentro de la palabra")
        print(f"Tienes {vidas} vidas")
        if vidas == 0:
            print("Perdiste")
    else:
        print("Muy bien")
        
        
        
        