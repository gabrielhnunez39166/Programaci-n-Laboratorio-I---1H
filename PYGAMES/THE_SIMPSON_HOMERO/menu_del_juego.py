import config_juego
import pygame
import juego_basico
import colores
import sonido

pygame.init()

sonido.encender_audio('1', 'INTRO')

def menu(ejecutando_menu):
    '''
    - Menu del juego.
    - Recibe como parametro un valor booleano que representa la ejecucion del juego (True -> ejecutar)
    - No retorna
    '''

    while ejecutando_menu:
        config_juego.ventana
        config_juego.nombre_juego
        config_juego.icono_juego

        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                ejecutando_menu = False

        lista_teclas = pygame.key.get_pressed()
        if lista_teclas[pygame.K_SPACE] :
            pygame.mixer.stop()
            juego_basico.bucle_del_juego(True)

        if lista_teclas[pygame.K_ESCAPE] :
            pygame.quit()

        #AGREGO EL FONDO DEL MENU Y ACTUALIZO LA VENTANA
        config_juego.dibujar_imagenes(config_juego.fondo_menu, 0, 0)
        config_juego.dibujar_texto('Presione la BARRA para INICIAR', 50, colores.NEGRO, 440, 200)
        config_juego.dibujar_texto('Presione ESC para SALIR', 50, colores.NEGRO, 490, 300)
        pygame.display.update()    
    pygame.quit()
menu(True)