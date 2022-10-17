from data_stark import lista_personajes
from librerias_stark import *


def menu_principal(lista: list) -> None:
    '''
    - Es el menu que se muestra por consola y por medio de un input seleccionamos las opciones que brinde el mismo.
    - Recibe como parametro un lista.
    - Retorna: None
    '''

    while True:
        respuesta = input("\nIngrese una opcion: \n1 - Mostrar iniciales \n9 - Salir \n> ")

        if respuesta == "1":
            extraer_iniciales('Primer Inicial')
        elif respuesta == "2":
            definir_iniciales_nombre (lista)
        elif respuesta == "3":
            pass
        elif respuesta == "4":
            pass
        elif respuesta == "5":
            pass
        elif respuesta == "6":
            pass
        elif respuesta == "7":
            pass
        elif respuesta == "8":
            pass
        elif respuesta == "9":
            print("\nGracias por usar nuestro programa.\n")
            break
        else:
            print("\nLa opcion ingresada es incorrecta, intentalo nuevamente.\n")
            continue

menu_principal(lista_personajes)
