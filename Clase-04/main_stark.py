from data_stark import lista_personajes
from libreria_stark import *


def menu_principal(lista: list) -> None:
    '''
    - Es el menu que se muestra por consola y por medio de un input seleccionamos las opciones que brinde el mismo.
    - Recibe como parametro un lista.
    - Retorna: None
    '''

    while True:
        respuesta = input("\nIngrese una opcion: \n1 - Nombres de superheroes masculinos \n2 - Nombres de superheroes femeninos \n3 - Superheroe masculino mas alto \n4 - Superheroe femenino mas alto \n5 - Salir \n> ")

        if respuesta == "1":
            imprimir_nombres_superheroes(lista, "M")
        elif respuesta == "2":
            imprimir_nombres_superheroes(lista, "F")
        elif respuesta == "3":
            # C - Recorrer la lista y determinar cuál es el superhéroe más alto de género M
            imprimir_maximo_minimo(lista, "M", "Maximo")
        elif respuesta == "4":
            # C - Recorrer la lista y determinar cuál es el superhéroe más alto de género F
            imprimir_maximo_minimo(lista, "F", "Minimo")
        elif respuesta == "5":
            print("\nGracias por usar nuestro programa.\n")
            break
        else:
            print("\nLa opcion ingresada es incorrecta, intentalo nuevamente.\n")
            continue

menu_principal(lista_personajes)