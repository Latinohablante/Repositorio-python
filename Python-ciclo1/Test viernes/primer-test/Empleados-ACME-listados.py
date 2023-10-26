def leerInt(msg):
    while True:
        try:
            iNum = int(input(msg))
            return iNum
        except ValueError:
            print("_" * 75)
            print("Ingrese un numero entero valido")

def leerString(msg):
    while True:
        try:
            sNom = input(msg)
            if sNom.strip() == "":
                print("\nPor favor ingrese un nombre valido")
                continue
            return sNom
        except Exception as e:
            print("\nError al ingresar un nombre" , e.message)

def menu():
    while True:
        print("_" * 75)
        print("MENU")
        print("\n1. Agregar empleado")
        print("2. Modificar empleado")
        print("3. Buscar empleado")
        print("4. Eliminar empleado")
        print("5. Lista empleados")
        print("6. Listar nomina de un empleado")
        print("7. Listar nomina de todos los empleados")
        print("8. Salir")
        opc = leerInt("\nSeleccione una opción de 1 a 8: ")
        if opc < 1 or opc > 8:
            print("Ingrese una opción valida")
            continue
        return opc

def agregar(lstId, lstNom, lstHor, lstVal, id, nom, horasT, valorH):
    lstId.append(id)
    lstNom.append(nom)
    lstHor.append(horasT)
    lstVal.append(valorH)
    
def modificar(lstId, lstNom, lstHor, lstVal):
    try: 
        id = leerInt("\nIngrese el id del empleado: ")
        e = lstId.index(id)
    except ValueError:
        print("El id no esta registrado")
        return
    print("_"*75)
    print("MENU DE MODIFICACION")
    print("\n1. Nombre")
    print("2. Horas trabajadas")
    print("3. Valor de la hora")
    while True:
        op = leerInt("\nSeleccione el que quiere modificar: ")
        if op < 1 or op > 3:
            print("Ingrese un valor valido")
            continue
        break
    if op == 1:
        print("_" * 75)
        print("Modificar nombre")
        nueNom = leerString("Ingrese el nuevo nombre: ")
        lstNom.pop(e)
        lstNom.insert(e, nueNom)
    elif op == 2:
        print("_" * 75)
        print("Modificar horas trabajadas")
        while True:
            nueHor = leerInt("Ingrese el nuevo numero de horas trabajadas del empleado: ")
            if nueHor < 1 or nueHor > 160:
                print("El numero de horas tiene que estar entre 1 y 160")
                continue
            break
        lstHor.pop(e)
        lstHor.insert(e, nueHor)
    elif op == 3:
        print("_" * 75)
        print("Modificar valor de la hora")
        while True:
            nueValor = leerInt("Ingrese el valor unitario de la hora: ")
            if nueValor < 8000 or nueValor > 150000:
                print("El nuevo valor de la horas tiene que estar entre 8.000 y 150.000")
                continue
            break    
        lstVal.pop(e)          
        lstVal.insert(e, nueValor)

def buscar(lstId, lstNom, lstHor, lstVal): 
    try: 
        id = leerInt("\nIngrese el id del empleado: ")
        e = lstId.index(id)
    except ValueError:
        print("El empleado no esta registrado")
        return
    print(f"\nNombre: {lstNom[e]}"
        f"\nNumero de horas trabajadas: {lstHor[e]}"
        f"\nValor de la hora: ${lstVal[e]:,.0f}")

def eliminar(lstId, lstNom, lstHor, lstVal):
    try: 
        id = leerInt("\nIngrese el id del empleado: ")
        e = lstId.index(id)
        lstId.pop(e)
        lstNom.pop(e)
        lstHor.pop(e)
        lstVal.pop(e)
        print("El empleado ha sido eliminado")
    except ValueError:
        print("El empleado no fue eliminado porque no esta registrado")
        return

def listEmpleados(lstId, lstNom, lstHor, lstVal):
    ini = 0
    fi = 2
    while True:
        for l in range(ini, fi):
            if l >= len(lstId):
                return
            else:    
                print(f"Id: {lstId[l]}\tNombre: {lstNom[l]}\tHoras trabajadas: {lstHor[l]}\tValor horas: {lstVal[l]:,.0f}")
        while True:
            conf = int(input("\nSi desea continuar digite 1, si quiere salir presione 2: "))
            if conf < 1 or conf > 8:
                print("Ingrese una opción valida")
                continue
            break
        if conf == 2:
            return
        ini +=2
        fi +=2    

def nomEmpleado(lstId, lstNom, lstHor, lstVal):
    auxi = 0
    try: 
        id = leerInt("\nIngrese el id del empleado: ")
        e = lstId.index(id)
    except ValueError:
        print("El empleado no esta registrado")
        return
    salBru = lstHor[e] * lstVal[e]
    if salBru < 1160000:
        auxi = 140606
    desPen = salBru * 0.04 
    desEPS = salBru * 0.04
    salNet = salBru + auxi - desPen - desEPS

    print(f"Id: {lstId[e]}\tNombre: {lstNom[e]}\tHoras trabajadas: {lstHor[e]}\tValor horas: {lstVal[e]:,.0f}")
    print(f"Salario Bruto: {salBru:,.0f}\tAuxilio: {auxi:,.0f}\tDescuento pensión: -{desPen:,.0f}\tDescuento EPS: -{desEPS:,.0f}\tSalario neto: {salNet:,.0f}")

def nomEmpleados(lstId, lstNom, lstHor, lstVal):
    ini = 0
    fi = 5
    salNet = []
    salBru = []
    desPen = []
    desEPS = []
    auxi = []
    lstId = [1, 2, 3, 4, 5, 6]
    lstNom = ["Daniel", "Elkin", "Lucho", "Mario", "Mateo", "Jesus"]
    lstHor = [10, 20, 30, 40, 50, 60]
    lstVal = [10000, 20000, 30000, 40000, 50000, 60000]
    for i in range(len(lstId)):
        auxi.insert(i, 0)
        salBru.insert(i, (lstHor[i] * lstVal[i]))
        if salBru[i] < 1160000:
            auxi.insert(i, 140606)
        desPen.insert(i, (salBru[i] * 0.04)) 
        desEPS.insert(i, (salBru[i] * 0.04))
        salNet.insert(i, (salBru[i] + auxi[i] - desPen[i] - desEPS[i]))
    while True:
        for l in range(ini, fi):
            if l >= len(lstId):
                return
            else:    
                print(f"\nId: {lstId[l]}\tNombre: {lstNom[l]}\tHoras trabajadas: {lstHor[l]}\tValor horas: {lstVal[l]:,.0f}"
                        f"\nSalario Bruto: {salBru[l]:,.0f}\tAuxilio: {auxi[l]:,.0f}\tDescuento pensión: -{desPen[l]:,.0f}\tDescuento EPS: -{desEPS[l]:,.0f}\tSalario neto: {salNet[l]:,.0f}")
        while True:
            conf = int(input("\nSi desea continuar digite 1, si quiere salir presione 2: "))
            if conf < 1 or conf > 8:
                print("Ingrese una opción valida")
                continue
            break
        if conf == 2:
            return
        ini +=5
        fi +=5  

def salir():
    while True:
        des = leerInt("\nSi desea salir presione 1, si no desea salir presione 2: ")
        if des < 1 or des > 2:
            print("Por favor seleccione una de las dos opciones")
            continue
        return des


ids = []
noms = []
horasTs = []
valorHs = []
while True:
    iOpc = menu()
    if iOpc == 1:
        id = leerInt("\nIngrese el numero de id: ")
        nom = leerString("Ingrese el nombre del empleado: ")
        while True:
            horasT = leerInt("Ingrese el numero de horas trabajadas del empleado: ")
            if horasT < 1 or horasT > 160:
                print("El numero de horas tiene que estar entre 1 y 160")
                continue
            break
        while True:
            valorH = leerInt("Ingrese el valor unitario de la hora: ")
            if valorH < 8000 or valorH > 150000:
                print("El valor de la horas tiene que estar entre 8.000 y 150.000")
                continue
            break   
        agregar(ids, noms, horasTs, valorHs, id, nom, horasT, valorH)
        print("_" * 75)
        print("\nLos datos fueron agregados")
        input("\nPresione cualquier tecla para continuar")
    elif iOpc == 2:
        modificar(ids, noms, horasTs, valorHs) 
        input("\nPresione cualquier tecla para continuar") 
    elif iOpc == 3:
        buscar(ids, noms, horasTs, valorHs)
        input("\nPresione cualquier tecla para continuar")
    elif iOpc == 4:
        eliminar(ids, noms, horasTs, valorHs)
        input("\nPresione cualquier tecla para continuar")
    elif iOpc == 5:
        listEmpleados(ids, noms, horasTs, valorHs)
        input("\nPresione cualquier tecla para continuar")
    elif iOpc == 6:
        nomEmpleado(ids, noms, horasTs, valorHs)
        input("\nPresione cualquier tecla para continuar")
    elif iOpc == 7:
        nomEmpleados(ids, noms, horasTs, valorHs)
        input("\nPresione cualquier tecla para continuar")        
    elif iOpc == 8:
        desi = salir()
        if desi == 1:
            print("\nFIN DEL PROGRAMA")
            break
        else:
            continue