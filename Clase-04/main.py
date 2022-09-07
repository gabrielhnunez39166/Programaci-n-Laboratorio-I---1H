from turtle import color
from data_stark import lista_personajes

'''
lista_heroes =
[
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

'''

# A
def mostrar_nombre_personajes_m():
    for nombre_de_personajes in lista_personajes:
        if (nombre_de_personajes["genero"] == "M"):
            nombre_personaje_masculino = nombre_de_personajes["nombre"]
            print(nombre_personaje_masculino)

# B
def mostrar_nombre_personaje_f():
    for nombre_de_personajes in lista_personajes:
        if (nombre_de_personajes["genero"] == "F"):
            nombre_personaje_femenino = nombre_de_personajes["nombre"]
            print(nombre_personaje_femenino)


# C
def buscar_primer_masculino():
    primer_personaje_masculino = {}
    for personaje in lista_personajes:
        if (personaje["genero"] == "M"):
            primer_personaje_masculino = personaje
            break
    return primer_personaje_masculino

def calcular_personaje_m_alto():
    superheroe_masculino_alto = buscar_primer_masculino()
    for personaje in lista_personajes:
        if ((personaje["genero"] == "M") and (float(personaje["altura"]) > float(superheroe_masculino_alto["altura"]))):
            superheroe_masculino_alto = personaje
            nombre_superheroe_mas_alto = personaje["nombre"]
            break
    print(nombre_superheroe_mas_alto, superheroe_masculino_alto["altura"])


# D
def buscar_primer_femenina():
    primer_personaje_femenino = {}
    for personaje in lista_personajes:
        if (personaje["genero"] == "F"):
            primer_personaje_femenino = personaje
    return primer_personaje_femenino
        
def calcular_personaje_f_mas_alto():
    superheroe_femenino_alto = buscar_primer_femenina()
    for personaje in lista_personajes:
        if ((personaje["genero"] == "F") and (float(personaje["altura"]) > float(superheroe_femenino_alto["altura"]))):
            superheroe_femenino_alto = personaje
            nombre_superheroe_femenino_alto = superheroe_femenino_alto["nombre"]
    print(nombre_superheroe_femenino_alto, superheroe_femenino_alto["altura"])


# E
def calcular_personaje_m_bajo():
    superheroe_masculino_bajo = buscar_primer_masculino()
    for personaje in lista_personajes:
        if ((personaje["genero"] == "M") and (float(personaje["altura"]) < float(superheroe_masculino_bajo["altura"]))):
            superheroe_masculino_bajo = personaje

    print(superheroe_masculino_bajo["nombre"], superheroe_masculino_bajo["altura"])

# F
def calcular_personaje_f_mas_bajo():
    superheroe_femenino_bajo = buscar_primer_femenina()
    for personaje in lista_personajes:
        if ((personaje["genero"] == "F") and (float(personaje["altura"]) < float(superheroe_femenino_bajo["altura"]))):
            superheroe_femenino_bajo = personaje
    print(superheroe_femenino_bajo["nombre"], superheroe_femenino_bajo["altura"])

# G
def calcular_altura_promedio_m():
    acumulador_altura = 0
    contador_personajes = 0 
    for personajes in lista_personajes:
        if (personajes["genero"] == "M"):
            contador_personajes = len(lista_personajes)
            acumulador_altura += float(personajes["altura"])
    promedio_altura_personajes_m = acumulador_altura / contador_personajes

    print(str(contador_personajes) + "\n")
    print(str(acumulador_altura) + "\n")
    print(str(promedio_altura_personajes_m) + "\n")


# H
def calcular_altura_promedio_f():
    acumulador_altura = 0
    contador_personajes = 0 
    for personajes in lista_personajes:
        if (personajes["genero"] == "F"):
            contador_personajes = len(lista_personajes)
            acumulador_altura += float(personajes["altura"])
    promedio_altura_personajes_f = acumulador_altura / contador_personajes

    print(str(contador_personajes) + "\n")
    print(str(acumulador_altura) + "\n")
    print(str(promedio_altura_personajes_f) + "\n")


# I
""" Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F) """

# J
def determinar_cantidad_color_ojos():
    lista_color_ojos = []
    
    for personaje in lista_personajes:
        lista_color_ojos.append(personaje["color_ojos"])

    set_color_ojos = set(lista_color_ojos)

    lista_color = []
    for color_ojos in set_color_ojos:
        dict_color = {"color": color_ojos, "cantidad": 1}
        for personaje in color_ojos:
            if (personaje["color"] == color_ojos):
