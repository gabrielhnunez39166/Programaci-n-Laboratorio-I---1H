import funciones

def iniciar_programa():
    '''
    - Funcion con el objetivo de iniciar el programa y ocultar las funcionalidades dentro de ella.
    - No recibe parametros.
    - No retorna ningun valor.
    '''
    ############ Archivo pokedex del tipo lista ############
    archivo_pokedex = funciones.importar_json('pokedex.json')
    archivo_pokedex = archivo_pokedex['pokemones']
    #print(archivo_pokedex)

    def menu(lista: list):
        while True:
            print('''\nIngrese una opcion: \n1 - Listar pokemones \n2 - Ordenar por poder \n3 - Ordenar por id \n4 - Ordenar por mayor o menor al promedio \n5 - Buscar pokemones \nn - Salir''')
            respuesta = input('\n> ')
            if respuesta == '1':
                funciones.respuesta_uno(lista)
            elif respuesta == '2':
                funciones.respuesta_dos_tres(lista, 'poder')
            elif respuesta == '3':
                funciones.respuesta_dos_tres(lista, 'id')
            elif respuesta == '4':
                funciones.respuesta_cuatro(lista, 'poder')
            elif respuesta == '5':
                funciones.respuesta_cinco(lista)
            elif respuesta == 'n':
                break


    menu(archivo_pokedex)
iniciar_programa()