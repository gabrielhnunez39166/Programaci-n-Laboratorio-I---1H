""" 
respuesta = input ("Numero? ")
respuesta = int(respuesta)

while (respuesta != 1):
    if (respuesta == 10):
        print(respuesta)
    else:
        print("No es 10")
    respuesta = input("Numero? ")
    respuesta = int(respuesta)
 """

while (True):
    respuesta = input ("Numero? ")
    respuesta = int(respuesta)

    if (respuesta == 1): #Rompe la iteracion
        break

    if (respuesta == 10):
        print(respuesta)
    elif (respuesta == 11):
        print(respuesta)
    elif (respuesta == 11):
        print("Ninia Bonita")
    else:
        print("No es 10")

