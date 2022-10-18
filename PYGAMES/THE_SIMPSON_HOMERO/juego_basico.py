import pygame
import donas
import personaje
import sonido
import config_juego

pygame.init()

#TIMER
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,100)

#PLAYER - DONAS
player = personaje.crear(config_juego.ANCHO_VENTANA/2, config_juego.ALTO_VENTANA-200,200,200)
lista_donas = donas.crear_lista_donas(20)

#BUCLE
def bucle_del_juego(ejecutar_bucle):
    #SONIDO DE FONDO
    sonido.encender_audio('1', 'HOMER_DAY')
    while ejecutar_bucle:

        config_juego.definir_fps(100)
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                ejecutar_bucle = False
                sonido.encender_audio('0', 'HOMER_DAY')

            if evento.type == pygame.USEREVENT:
                if evento.type == timer:
                    donas.update(lista_donas)

        lista_teclas = pygame.key.get_pressed()

        if lista_teclas[pygame.K_a] :
            personaje.update(player,-5)
        if lista_teclas[pygame.K_d] :
            personaje.update(player,5)

        config_juego.ventana.blit(config_juego.fondo, (0, 0))
        personaje.actualizar_pantalla(player, config_juego.ventana)
        donas.actualizar_pantalla(lista_donas, player, config_juego.ventana)
        pygame.display.update()
    pygame.quit()