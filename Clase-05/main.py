from data_stark import lista_personajes

def menu(lista):
    while(True):
        respuesta = input('\nIngrese una opcion \n 1 - opcion 1 \n 0 - Salir \n > ')
        if respuesta == '1':
            pass
        elif respuesta == '0':
            print('\nGracias por usar nuestro programa.\n')
            break
        else:
            print('\nLa opcion ingresada no es correcta. Intente nuevamente.\n')
            continue

menu(lista_personajes)