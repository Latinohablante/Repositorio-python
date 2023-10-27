archivo = open("Temas de Clase/Archivos/salas.txt", "w")
# busca un archivo si no existe lo crea en la ubicacion

archivo.write("sputnik\n\t")
archivo.write("apolo")
archivo.write("\nNave espacial")

archivo.writelines(["\nhouston\n", "artemis\n"])

archivo.close()