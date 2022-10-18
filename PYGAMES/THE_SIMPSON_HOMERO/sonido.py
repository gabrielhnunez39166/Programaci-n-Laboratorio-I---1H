import pygame


pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)

def buscar_tema(tema: str):
    '''
    - Esta funciona se encarga de buscar y devolver el tema ingresado para cada accion del juego.
    - Recibe como parametro el tema a buscar
    - Retorna el tema encontrado
    '''
    if tema == 'HOMER_DAY':
        HOMER_DAY = 'sonido\Homer_Day.wav'
        tema = HOMER_DAY
    elif tema == 'LOS_SIMPSON':
        LOS_SIMPSON = 'sonido\los_simpson.wav'
        tema = LOS_SIMPSON
    elif tema == 'ME_QUIERO_VOLVER_CHANGO':
        ME_QUIERO_VOLVER_CHANGO = 'sonido\me_quiero_volver_chango.wav'
        tema = ME_QUIERO_VOLVER_CHANGO
    elif tema == 'OUCH':
        OUCH = 'sonido\ouch.wav'
        tema = OUCH
    elif tema == 'CERVEZA':
        CERVEZA = 'sonido\cerveza.wav'
        tema = CERVEZA
    elif tema == 'WOOHOO':
        WOOHOO = 'sonido\WOOHOO.wav'
        tema = WOOHOO
    elif tema == 'INTRO':
        INTRO = 'sonido\intro.wav'
        tema = INTRO
    elif tema == 'TE_BAILO_SABROSO':
        TE_BAILO_SABROSO = 'sonido/te_bailo_sabroso.wav'
        tema = TE_BAILO_SABROSO
    return tema

def encender_audio(encender, tema_a_buscar):
    tema = buscar_tema(tema_a_buscar)
    sonido = pygame.mixer.Sound(tema)
    sonido.set_volume(0.2)
    if encender == '1':
        sonido.play()
    if encender == '0':
        sonido.stop()
