fd = open("Temas de Clase/Archivos/mbox-short.txt", "r")

# para hacer el ejercicio con listas y que no se repitan
setEmailListas = []
for linea in fd:
    if linea.startswith("From:"):
        setEmailListas.append(linea.split()[1])

fd.close()

cl = len(setEmailListas)
print("Cantidad de correos de origen distintos:", cl)


# este codigo los ordena por tamaño de caracteres y los imprime
# for email in sorted(setEmail, reverse=False, key=lambda x:len(x)):
#     print(email)


for lista in setEmailListas:
    # comprueba si hay elementos repetidos
    while setEmailListas.count(lista) > 1:
        # si es True, elimina todas las apariciones adicionales exepto 1
        setEmailListas.remove(lista)


for email in reversed(setEmailListas):
    fd.write(f"{email} enviado [ok]")