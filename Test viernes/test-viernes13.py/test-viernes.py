
nombreArchivo = input("Enter the file name: ")
fd = open(f"Test viernes/test-viernes13.py/{nombreArchivo}", "r")
 
def promedioSpam(lstSpamEmails):
    contador = 0
    acumulativo = 0
    
    for linea in fd:
        if linea.startswith("X-DSPAM-Confidence:"):
            email = linea.split()[1]
            if email not in lstSpamEmails:
                lstSpamEmails.append(email)
                contador += 1

    for elemento in lstSpamEmails:
        acumulativo += float(elemento)

    promedio = acumulativo/contador
    return promedio

lstSpamEmails = []

print(f"Average spam confidence: {promedioSpam(lstSpamEmails)}")

fd.close()



