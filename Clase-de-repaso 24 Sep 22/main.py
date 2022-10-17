from funciones import *

#MENU
def paulina_app():
    lista_videos = cargar_json('X')
    print('''
    1 - Listar TOP N videos
    2 - Ordenar videos por duracion (UP/DOWN)
    3 - Ordenar vudeos por cantidad de viwes (UP/DOWS)
    4 - Buscar videos por titulo
    5 - Exportar listas de videos a CSV
    6 - Salir
    ''')
    while True:
        respuesta = input('\nIngrese una opcion: \n> ')
        if respuesta == '1':
            #HACER UNA FUNCION OBTENER ENTERO
            #VALIDAR QUE TOP SEA UN INT Y QUE NO SUPERE EL TAMANIO DE LA LISTA
            top = input('Cantidad de elementos a mostrar?')
            mostrar(lista_videos[:top])
        elif respuesta == '2':
            print('Ordenar videos por duracion (UP/DOWN)')
        elif respuesta == '3':
            print('Ordenar vudeos por cantidad de viwes (UP/DOWS')
        elif respuesta == '4':
            print('Buscar videos por titulo')
        elif respuesta == '5':
            print('Exportar listas de videos a CSV')
        elif respuesta == '6':
            print('Salir')
        else:
            print('La opcion ingresada es incorrecta. Intente nuevamente.')
            continue

paulina_app()