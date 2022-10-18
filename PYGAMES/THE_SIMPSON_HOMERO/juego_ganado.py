import pygame
import colores
import config_juego
import sonido

pygame.init()

def ventana_juego_ganado(ejecutando_fin_juego):
    '''
    - Pantalla de fin del juego.
    - Recibe como parametro un valor booleano (True -> ejecutar)
    - No retorna
    '''
    
    sonido.encender_audio('1', 'TE_BAILO_SABROSO')
    
    while ejecutando_fin_juego:
        config_juego.ventana
        config_juego.nombre_juego
        config_juego.icono_juego

        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                ejecutando_fin_juego = False

        lista_teclas = pygame.key.get_pressed()
        if lista_teclas[pygame.K_ESCAPE] :
            pygame.mixer.stop()
            pygame.quit()

        #AGREGO EL FONDO DEL MENU Y ACTUALIZO LA VENTANA
        config_juego.dibujar_imagenes(config_juego.fondo_juego_ganado, 0, 0)
        config_juego.dibujar_texto('Felicitaciones!!!', 60, colores.NEGRO, 70, 20)
        config_juego.dibujar_texto('Has Ganado el Juego!', 60, colores.NEGRO, 70, 60)
        config_juego.dibujar_texto('Presione ESC para SALIR', 30, colores.NEGRO, 10, 650)
        pygame.display.update()

    pygame.quit()




