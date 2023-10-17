import random

numeroRandom = random.randint(1,1000)
diccionario = {}
nombre = input("Ingrese su nombre: ")
intento = 0
diccionario[f"{nombre}"] = intento

while True:
    for i in range (1,11):
        numeroUsuario = int(input("Ingrese un número del 1 al 1000: "))
        if numeroRandom == numeroUsuario:
            print(f"Intento {i}/10")
            print("Felicitaciones, ganaste\n")
            diccionario[f"{nombre}"] = i
            break

        elif numeroRandom > numeroUsuario:
            print(f"Intento {i}/10")
            print("\nNo lo lograste el número es mayor\n")
            diccionario[f"{nombre}"] = i
            continue
        elif numeroRandom < numeroUsuario:
            print(f"Intento {i}/10")
            print("No lo lograste el número es menor\n")
            diccionario[f"{nombre}"] = i
            continue
        else:
            diccionario[f"{nombre}"] = i
            print("Lo sentimos no lo conseguiste")


    print("¿Desea continuar? Ingrese 'S' para continuar.")
    continuar = input("Si desea terminar presione Enter: ")

    if continuar.lower() != "s":
        print("\nAdios. Gracias por usar la aplicación")    
        break
    else:
        print("\nVamos a continuar")
        input("Presione Enter para continuar\n")
        continue