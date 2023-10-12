def miFun(email):
    return len(email)

fd = open("Temas de Clase/Archivos/mbox-short.txt", "r")

# para hacer el ejercicio con listas y que no se repitan
setEmailListas = []
for linea in fd:
    if linea.startswith("To:"):
        setEmailListas.append(linea.split()[1])

fd.close()

cl = len(setEmailListas)
print("Cantidad de correos de origen distintos:", cl)

# for email in sorted(setEmail, reverse=False, key=lambda x:len(x)):
#     print(email)

for email in sorted(setEmailListas, reverse=False, key=miFun):
    print(f"{email} enviado [ok]")