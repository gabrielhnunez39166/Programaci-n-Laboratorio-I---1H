from data_stark import lista_personajes

lista_heroes =[
 {
   "nombre": "Howard the Duck",
   "identidad": "Howard (Last name unrevealed)",
   "empresa": "Marvel Comics",
   "altura": "79.349999999999994",
   "peso": "18.449999999999999",
   "genero": "M",
   "color_ojos": "Brown",
   "color_pelo": "Yellow",
   "fuerza": "2",
   "inteligencia": "average"
 }
]

# B - Recorrer la lista imprimiendo por consola el nombre de cada superheroe
def mostrar_nombre_superheroes():
    for nombres_superheroes in lista_personajes:
        nombre_superheroe = nombres_superheroes["nombre"]
        print(nombre_superheroe)


# C - Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
def mostrar_nombre_altura_superheroes():
    for nombres_altura_superheroes in lista_personajes:
        nombre_superheroe = nombres_altura_superheroes["nombre"]
        altura_superheroes = nombres_altura_superheroes["altura"]
        print("Nombre: {0} - Altura: {1}".format(nombre_superheroe,altura_superheroes))


# D - Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
def calcular_superheroe_mas_alto():
    superheroe_mas_alto = lista_personajes[0]
    #print(superheroe_mas_alto)
    
    for altura_de_superheroes in lista_personajes:
        if(float(altura_de_superheroes["altura"]) > float(superheroe_mas_alto["altura"])):
            superheroe_mas_alto = altura_de_superheroes
    print("El superheroe mas alto es: {0} con una altura de: {1}".format(superheroe_mas_alto["nombre"], superheroe_mas_alto["altura"]))


# E - Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
def calcular_superheroe_mas_bajo():
    superheroe_mas_bajo = lista_personajes[0]
    #print(superheroe_mas_bajo)

    for altura_de_superheroes in lista_personajes:
        if (float(altura_de_superheroes["altura"]) < float(superheroe_mas_bajo["altura"])):
            superheroe_mas_bajo = altura_de_superheroes
    print("El superheroe mas bajo es: {0} con una altura de: {1}".format(superheroe_mas_bajo["nombre"], superheroe_mas_bajo["altura"]))


# F - Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
def calcular_promedio_altura_superheroes():
    acumulador_altura_superheroes = 0
    contador_superheroes = 0

    for altura_de_superheroes in lista_personajes:
        contador_superheroes = len(altura_de_superheroes)
        acumulador_altura_superheroes += float(altura_de_superheroes["altura"])
    promedio_altura_superheroes = acumulador_altura_superheroes / contador_superheroes
    print("La altura promedio de los superheroes es: {0}".format(promedio_altura_superheroes))
    return promedio_altura_superheroes


# G - Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO y PROMEDIO)
def informar_nombres_superheroes_MMP():
    calcular_superheroe_mas_alto()
    calcular_superheroe_mas_bajo()
    promedio_altura_superheroes = calcular_promedio_altura_superheroes()
    #print("La altura promedio de los supeheroes es de: {0}".format(promedio_altura_superheroes))

    for superheroe in lista_personajes:
        if (float(superheroe["altura"]) == promedio_altura_superheroes):
            nombre_superheroe_altura_promedio = superheroe["altura"]
        else:
            nombre_superheroe_altura_promedio = "No existe un superheroe con altura promedio"
    print("Superheroe con altura promedio: {0}".format(nombre_superheroe_altura_promedio))


# H - Calcular e informar cual es el superhéroe más pesado.
def calcular_heroe_mas_pesado():
    superheroe_mas_pesado = lista_personajes[0]

    for superheroe in lista_personajes:
        if (float(superheroe["peso"]) > float(superheroe_mas_pesado["peso"])):
            superheroe_mas_pesado = superheroe
    print("El superheroe mas pesado es: {0} con un peso de: {1}".format(superheroe_mas_pesado["nombre"], superheroe_mas_pesado["peso"]))


# H - Calcular e informar cual es el superhéroe menos pesado.
def calcular_heroe_menos_pesado():
    superheroe_menos_pesado = lista_personajes[0]

    for superheroe in lista_personajes:
        if (float(superheroe["peso"]) < float(superheroe_menos_pesado["peso"])):
            superheroe_menos_pesado = superheroe
    print("El superheroe menos pesado es: {0} con un peso de: {1}".format(superheroe_menos_pesado["nombre"], superheroe_menos_pesado["peso"]))


# J - Construir un menú que permita elegir qué dato obtener

while(True):
    respuesta = input("\n\n 1. Mostrar nombre de los superheroes. \n\
                            2. Mostrar nombre y altura de los superheroes. \n\
                            3. Mostrar el superheroe mas alto. \n\
                            4. Mostrar el superheroe mas bajo. \n\
                            5. Mostrar el promedio de altura de los superheroes. \n\
                            6. Nombres superheroes (MAXIMO, MINIMO, PROMEDIO). \n\
                            7. Superheroe mas pesado. \n\
                            8. Superheroe menos pesado. \n\
                            9. Superheroe menos pesado. \n\
                            9. Salir.\n\n>")

    if (respuesta == "1"):
        mostrar_nombre_superheroes()
    elif (respuesta == "2"):
        mostrar_nombre_altura_superheroes()
    elif (respuesta == "3"):
        calcular_superheroe_mas_alto()
    elif (respuesta == "4"):
        calcular_superheroe_mas_bajo()
    elif (respuesta == "5"):
        calcular_promedio_altura_superheroes()
    elif (respuesta == "6"):
        informar_nombres_superheroes_MMP()
    elif (respuesta == "7"):
        calcular_heroe_mas_pesado()
    elif (respuesta == "8"):
        calcular_heroe_mas_pesado()
    elif (respuesta == "9"):
        calcular_heroe_menos_pesado()
    elif (respuesta == "10"):
        print("Gracias por usar nuestro programa.")
        break
