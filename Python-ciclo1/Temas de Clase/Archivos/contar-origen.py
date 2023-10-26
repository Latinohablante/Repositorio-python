# programa que cuente la cantidad de usuarios que están enviando correos de origen que sean usuarios diferentes

def miFun(email):
    return len(email)

fd = open("Temas de Clase/Archivos/mbox-short.txt", "r")

# cl = 0
setEmail = set() # set() -> crea un conjunto vacio
for linea in fd:
    if linea.startswith("From:"):
        # cl += 1
        # email = linea.split()[1]
        # print(email)
        setEmail.add(linea.split()[1])

fd.close()

cl = len(setEmail)
print("Cantidad de correos de origen distintos:", cl)

# for email in sorted(setEmail, reverse=False, key=lambda x:len(x)):
#     print(email)

for email in sorted(setEmail, reverse=False, key=miFun):
    print(email)