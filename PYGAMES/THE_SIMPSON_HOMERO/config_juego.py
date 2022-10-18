import pygame
import os
import colores

pygame.init()

#CONFIG VENTANA
ANCHO_VENTANA = 1024
ALTO_VENTANA = 720
#VENTANA
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
#FONDO
fondo = pygame.transform.scale(pygame.image.load(os.path.join('imagenes/fondo.jpg')), (ANCHO_VENTANA, ALTO_VENTANA)).convert()
#NOMBRE DEL JUEGO
nombre_juego = pygame.display.set_caption("PYGAME HOMERO COME DONAS")
#ICONO DEL JUEGO
img_icono = pygame.image.load('imagenes\icono.png')
icono_juego = pygame.display.set_icon(img_icono)
#FONDO DEL MENU
fondo_menu = pygame.transform.scale(pygame.image.load(os.path.join('imagenes/fondo_menu.png')), (ANCHO_VENTANA, ALTO_VENTANA)).convert()
#FONDO DE FIN DEL JUEGO
fondo_fin_del_juego = pygame.transform.scale(pygame.image.load(os.path.join('imagenes/fin_del_juego.jpeg')), (ANCHO_VENTANA, ALTO_VENTANA)).convert()
#FONDO DE FIN DEL JUEGO
fondo_juego_ganado = pygame.transform.scale(pygame.image.load(os.path.join('imagenes/ganador.jpg')), (ANCHO_VENTANA, ALTO_VENTANA)).convert()

#VARIABLES PARA LA FUNCION DIBUJAR TEXTO
color_texto = colores.GRIS
posicion_x = ANCHO_VENTANA // 2
posicion_y = ALTO_VENTANA // 4

#DIBUJAR TEXTO
def dibujar_texto(texto, tamanio_letra, color_texto, x, y):
    '''
    - Esta funcion se ocupa de dibujar en la pantalla el texto que le pasemos por parametro.
    - Recibe por parametro el texto, la fuente, el color del texto, posicion x e y.
    - No Retorna
    '''
    fuente = pygame.font.SysFont("Arial Narrow", tamanio_letra)
    img = fuente.render(texto, True, color_texto)
    ventana.blit(img, (x, y))

#DIBUJAR IMAGENES
def dibujar_imagenes(img, x, y):
    '''
    - Esta funcion se encarga de posicionar las imagenes estaticas del fondo del juego.
    - Recibe como parametro la imgen, la posicion x e y.
    - No retorna
    '''
    ventana.blit(img, (x, y))

#FPS
def definir_fps(fps: int) -> None:
    '''
    - Define la cantidad de fotogramas por segundo en la que se ejecuta e juego.
    - Recibe como parametro la cantidad de FPS.
    - No retorna.
    '''
    clock = pygame.time.Clock()
    clock.tick(fps)













