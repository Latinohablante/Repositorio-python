def miFun(email):
    return len(email)

fd = open("Temas de Clase/Archivos/mbox-short.txt", "r")

# cl = 0
setEmail = set() # set() -> crea un conjunto vacio
for linea in fd:
    if linea.startswith("To:"):
        # cl += 1
        # email = linea.split()[1]
        # print(email)
        setEmail.add(linea.split()[1])


fd.close()

cl = len(setEmail)
print("Cantidad de correos de destino distintos:", cl)

# for email in sorted(setEmail, reverse=False, key=lambda x:len(x)):
#     print(email)

for email in sorted(setEmail, reverse=False, key=miFun):
    print(f"{email} enviado [ok]")