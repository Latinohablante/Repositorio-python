"""Usted acaba de comprar la empresa ACME un empresa comercializadora y distribuidora de
productos, dentro del cual se venden varias variedades de productos. Decide por estrategia de
mercadeo colocar en la entrada los productos con precios más bajos, así que construye un
programa que le ayude a ingresar, consultar, modificar y eliminar para esto cree el siguiente
menú:
==================
PRODUCTOS ACME
==================
1. Agregar producto
2. Modificar producto
3. Eliminar producto
4. Listar varios productos
5. Estrategia de mercadeo
6. Salir
>> ¿Opción [1, 6]?

Opciones
1. Agregar producto. Este opción permite agregar un producto al sistema. El producto consta de
un id, nombre, precio y cantidad (existencias en bodega)
2. Modificar producto. Esta opción permite modificar los datos de un producto ingresando el
código.
3. Eliminar producto. Esta opción permite eliminar un producto a partir del código.
5. Estrategia de mercadeo. Esta opción ordena y lista ascendentemente por precio todos los
productos que hay en bodega y los muestre sus datos en pantalla. Se listan de a 5 productos
usando paginación."""


def leerPrecioProd():
    while True:
        try:
            n = int(input("Ingrese el precio del producto: "))
            if n < 1:# or n > 150000:
                print("Precio del producto inválido. Debe ser mayor que 0.")
                continue
            return n
        except ValueError:
            print("Error al ingresar el precio del producto.")

def leerCantidad():
    while True:
        try:
            n = int(input("Ingrese la cantidad de existencias del producto en bodega: "))
            if n < 0: #or n > 160:
                print("Cantidad inválida.")
                continue
            return n
        except ValueError:
            print("Error al ingresar la cantidad.")

def leerNombreProd():
    while True:
        try:
            nom = input("Ingrese el nombre del producto: ")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def leeridProd():
    while True:
        try:
            n = int(input("Ingrese el ID del producto: "))
            if n < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID. Ingreselo de nuevo.")


"""
Esto no sirve aquí

def nominaEmpleado(dicProductos):
    print("\n\n6. Nómina Empleado\n")
    idProd = leeridProd()
    existEmpl = buscarProducto(dicProductos, idProd)
    if existEmpl == False:
        print("El Empleado con ese código no ha sido ingresado.")
        input()
        return
    
    if dicProductos[idProd]["SalarioBruto"] < 1160000:
        dicProductos[idProd]["SalarioBruto"] = dicProductos[idProd]["SalarioBruto"] + 140606
        return dicProductos
"""


# Esta función revisa si ese producto ya está ingresado
def buscarProducto(dicProductos, idProd):
    # return dicProductos.get(idProd) != None
    return idProd in dicProductos

def eliminarProducto(dicProductos):
    print("\n\n3. Eliminar Producto\n")
    
    idProd = leeridProd()
    existProd = buscarProducto(dicProductos, idProd)
    if existProd == False:
        print("El Producto con ese id no ha sido ingresado.")
        input()
        return
    
    del dicProductos[idProd]

def listarProductos(dicProductos):
    
    if dicProductos == {}:
        input("No hay ningún producto en el sistema. Presione Enter para continuar")
        return 
        
    else:
        for ids, valor in dicProductos.items():
            
            print(f'{ids}\t\t{valor["nombre"]}\t\t{valor["Cantidad"]}\t\t${valor["Precio"]}')
        return dicProductos

def mnuBuscarProducto(dicProductos):
    print("\n\n3. Buscar producto\n")
    
    idProd = leeridProd()
    existEmpl = buscarProducto(dicProductos, idProd)
    if existEmpl == False:
        print("El Producto con ese código no ha sido ingresado.")
        input()
        return
    
    print("\n", "=" * 30)
    print("Nombre:", dicProductos[idProd]["nombre"])
    print("Cantidad de existencias:", dicProductos[idProd]["Cantidad"])
    print("Precio:", dicProductos[idProd]["Precio"])
    #print(f"Salario bruto: ${dicProductos[idProd]['SalarioBruto']:,.2f}")
    input("\n Presione cualquier tecla para volver al menu...")

def modificarProducto(dicProductos):
    print("\n\n2. Modificar producto\n")
    
    idProd = leeridProd()
    existProd = buscarProducto(dicProductos, idProd)
    if existProd == False:
        print("El id del producto no existe.")
        input()
        return
    
    print("\n")
    while True:
        op = int(input("\n1. Nombre\n2. Cantidad de existencias\n3. Precio\nOpcion? "))
        if op < 1 or op > 3:
            print("Opción inválida")
            input()
            continue
        break
    
    if op == 1:
        nombre = leerNombreProd()
        dicProductos[idProd]["nombre"] = nombre
    elif op == 2:
        cantProd = leerCantidad()
        dicProductos[idProd]["Cantidad"] = cantProd
        
    elif op == 3:
        precioProd = leerPrecioProd()
        dicProductos[idProd]["Precio"] = precioProd
        
    #dicProductos[idProd]["SalarioBruto"] = dicProductos[idProd]["PrecioProd"] * dicProductos[idProd]["Cantidad"]

def agregarProducto(dicProductos):
    print("\n\n*** 1. Agregar producto\n")
    dicDatos = {}
    id = leeridProd()
    if buscarProducto(dicProductos, id) == True:
        input("El producto ya existe en el sistema. Presione Enter para continuar")
        return
    
    dicDatos["nombre"] = leerNombreProd()
    dicDatos["Cantidad"] = leerCantidad()
    dicDatos["Precio"] = leerPrecioProd()
    #dicDatos["SalarioBruto"] = dicDatos["Precio"] * dicDatos["Cantidad"]
    
    dicProductos[id] = dicDatos

def menu():
    while True:
        try:
            print("*** PRODUCTOS ACME ***".center(40))
            print("MENU".center(40))
            print("1. Agregar producto")
            print("2. Modificar producto")
            print("3. Eliminar producto")
            print("4. Listar varios productos")
            print("5. Estrategia de mercadeo")
            print("6. Salir")
            #print("7. ")
            #print("8. ")
            op = int(input(">>> Opción (1-6)? "))
            if op < 1 or op > 6:
                print("Opción no válida. Escoja de 1 a 6.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 6.")
            input("Presione cualquier tecla para continuar...")

## PROGRAMA PRINCIPAL
dicProductos= {}
while True:
    op = menu()
    if op == 1:
        agregarProducto(dicProductos)
        print("")
        # print(dicProductos)
        # input()
    elif op == 2:
        modificarProducto(dicProductos)
        print("")
        # print(dicProductos)
        # input()
    elif op == 3:
        eliminarProducto(dicProductos)
    elif op == 4:
        print("ID\t\tNOMBRE\t\tCANT\t\tPRECIO")
        listarProductos(dicProductos)
        print("")
    elif op == 5:
        input("Mantenimiento, regrese más tarde. Presione Enter para continuar")
        continue
    elif op == 6:
        print("¿Desea salir de la aplicación? Ingrese 's' para Salir.")
        salir = input("Si desea regresar al menú presione Enter: ")

        if salir.lower() != "s":
            print("\nVamos a continuar")
            continue
        else:
            print("\nAdios. Gracias por usar la aplicación")
            input("Presione Enter para terminar\n")
            break
    # elif op == 7:
        # mnuBuscarProducto(dicProductos)
        # print(dicProductos)
        # input()
        pass
    # elif op == 8:
        pass
        # nominaEmpleado(dicProductos)

"""
Planteamiento ejercicio 5

crear un contador

contador = 0

si el contador % 5 = 0

imprima los productos desde n hasta contador

¿Cómo páginar de a cinco productos cada vez?
¿Cómo ordenar los productos en orden ascendente en un diccionario?
¿Cómo pasar los datos de un diccionario a una lista para ordenarlos ahí y mostrarlos en pantalla?


"""