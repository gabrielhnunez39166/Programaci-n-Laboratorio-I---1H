import pygame
import random
import sonido
from sklearn.utils import shuffle
import fin_del_juego
import juego_ganado

def crear(x, y, ancho, alto, tipo):
    # Leer una imagen
    if tipo == 'cerveza':
        tipo_de_dona = tipo
        imagen_dona = pygame.image.load("imagenes\cerveza.png")
        imagen_dona = pygame.transform.scale(imagen_dona,(ancho,alto))
    elif tipo == 'crema_rosa':
        tipo_de_dona = tipo
        imagen_dona = pygame.image.load("imagenes\dona.png")
        imagen_dona = pygame.transform.scale(imagen_dona,(ancho,alto))
    elif tipo == 'envenenada':
        tipo_de_dona = tipo
        imagen_dona = pygame.image.load("imagenes\dona_envenenada.png")
        imagen_dona = pygame.transform.scale(imagen_dona,(ancho,alto))
    rect_dona = imagen_dona.get_rect()
    rect_dona.x = x 
    rect_dona.y = y
    dict_dona = {}
    dict_dona["surface"] = imagen_dona
    dict_dona["tipo"] = tipo_de_dona
    dict_dona["rect"] = rect_dona
    dict_dona["visible"] = True
    dict_dona["speed"] = random.randrange (10,20,1)
    return dict_dona

def update(lista_donas):
    for dona in lista_donas:
        rect_dona = dona["rect"]
        rect_dona.y = rect_dona.y + dona["speed"]


def actualizar_pantalla(lista_donas,personaje,ventana):
    for dona in lista_donas:
        if(personaje["rect"].colliderect(dona["rect"]) and dona["tipo"] == 'cerveza'):
            #Si el personaje colisiona con la CERVEZA y la vida esta entre 1 y 3, se regenera 1 punto de vida.
            if (personaje['health'] >= 3 or personaje['health'] <= 0):
                sonido.encender_audio('1', 'CERVEZA')
                restar_dona(dona)
            else:
                sonido.encender_audio('1', 'CERVEZA')
                personaje["health"] = personaje["health"] + 1
                restar_dona(dona)
        elif(personaje["rect"].colliderect(dona["rect"]) and dona["tipo"] == 'crema_rosa'):
            #Si el personaje colisiona con la DONA ROSA, aumenta el contador en 100 puntos.
            personaje["score"] = personaje["score"] + 100
            restar_dona(dona)
        elif(personaje["rect"].colliderect(dona["rect"]) and dona["tipo"] == 'envenenada'):
            #Si el personaje colisiona con la DONA ENVENENADA, pierde 100 puntos del score y 1 punto de vida.
            if personaje['score'] > 0 and personaje['health'] > 1:
                personaje["score"] = personaje["score"] - 100
                personaje["health"] = personaje["health"] - 1
                sonido.encender_audio('1', 'OUCH')
                restar_dona(dona)
            #Si el personaje colisiona con la DONA ENVENENADA y este tiene 0 de score o 1 de vida, se pierde el juego (GAME OVER).
            elif personaje['score'] == 0 or personaje['health'] == 1:
                restar_dona(dona)
                pygame.mixer.stop()
                sonido.encender_audio('1', 'ME_QUIERO_VOLVER_CHANGO')
                fin_del_juego.ventana_fin_del_juego(True)

        #DIFICULTAD DEL JUEGO (VARIA LA VELOCIDAD DE LAS DONAS)
        if personaje['score'] == 2500:
            dona["speed"] = random.randrange (35,40,1)
        elif personaje['score'] == 2000:
            dona["speed"] = random.randrange (30,35,1)
        elif personaje['score'] == 1500:
            dona["speed"] = random.randrange (25,30,1)
        elif personaje['score'] == 1000:
            dona["speed"] = random.randrange (20,25,1)  
        elif personaje['score'] == 500:
            dona["speed"] = random.randrange (15,20,1)
        
        #GANAR JUEGO
        if personaje['score'] >= 3000:
            pygame.mixer.stop()
            juego_ganado.ventana_juego_ganado(True)
                
        if(dona["rect"].y > 780):
            restar_dona(dona)
        ventana.blit(dona["surface"],dona["rect"])

    font = pygame.font.SysFont("Arial Narrow", 50)
    score = font.render("PUNTAJE: {0}".format(personaje["score"]), True, (255, 0, 0))
    healt = font.render("VIDAS: {0}".format(personaje["health"]), True, (255, 0, 0))
    ventana.blit(score,(0,0))
    ventana.blit(healt,(300,0))

def crear_lista_donas(cantidad):
    lista_donas = []
    lista_donas_envenenadas = []
    contador_envenenadas = 0
    for i in range(cantidad):
        y = random.randrange (-1000,0,60)
        x = random.randrange (70,740,60)
        if (i % 2 == 0):
            contador_envenenadas = contador_envenenadas + 1
            if contador_envenenadas == 10:
                contador_envenenadas = 0
                lista_donas_envenenadas.append(crear(x,y,60,60,'cerveza'))
            elif contador_envenenadas != 10:
                lista_donas_envenenadas.append(crear(x,y,60,60,'envenenada'))
        elif (i % 2 == 1):
            lista_donas.append(crear(x,y,60,60,'crema_rosa'))

    lista_donas = lista_donas + lista_donas_envenenadas
    lista_donas = shuffle(lista_donas)
    return lista_donas

def restar_dona(dona):
    dona["rect"].x = random.randrange (35,960,60)
    dona["rect"].y = random.randrange (-1000,0,60)
