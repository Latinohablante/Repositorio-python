fd = open("Temas de Clase/Archivos/mbox-short.txt", "r")

fd2 = open("Temas de Clase/Archivos/envio-emails.txt", "w")

lstEmails = [] # creamos una lista vacia
for linea in fd:
    if linea.startswith("From:"):
        email = linea.split()[1]
        if email not in lstEmails:
            lstEmails.append(email)


for i in range(len(lstEmails)-1, -1,-1):

    #Enviar correo
    msj = f"{lstEmails[i]} enviado ok"
    print(msj)
    fd2.write(msj+"\n")

fd.close()
fd2.close()