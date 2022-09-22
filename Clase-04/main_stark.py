from data_stark import lista_personajes
from libreria_stark import *


def menu_principal(lista: list) -> None:
    '''
    - Es el menu que se muestra por consola y por medio de un input seleccionamos las opciones que brinde el mismo.
    - Recibe como parametro un lista.
    - Retorna: None
    '''

    while True:
        respuesta = input("\nIngrese una opcion: \n1 - Nombre de superheroes masculinos \n2 - Nombre de superheroes femeninos \n3 - Superheroe masculino mas alto \n4 - Superheroe femenino mas alto \n5 - Superheroe masculino mas bajo \n6 - Superheroe femenino mas bajo \n7 - Altura promedio superheroe masculino \n8 - Altura promedio superheroe femenino \n9 - Informa nombres del punto 1 al 8 \n10 - Cantidad de superheroes por color de ojos \n11 - Cantidad de superheroes por color de pelo \n12 - Cantidad de superheroes por nivel de inteligencia \n13 - Salir \n> ")

        if respuesta == "1":
            imprimir_nombres_superheroes(lista, 'genero', "M")
        elif respuesta == "2":
            imprimir_nombres_superheroes(lista, 'genero', "F")
        elif respuesta == "3":
            # C - Recorrer la lista y determinar cuál es el superhéroe más alto de género M
            imprimir_superheroes_max_min(lista, 'altura', 'maximo', 'M')
        elif respuesta == "4":
            # D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
            imprimir_superheroes_max_min(lista, 'altura', 'maximo', 'F')
        elif respuesta == "5":
            # E. Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M
            imprimir_superheroes_max_min(lista, 'altura', 'minimo', 'M')
        elif respuesta == "6":
            # F. Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F
            imprimir_superheroes_max_min(lista, 'altura', 'minimo', 'F')
        elif respuesta == "7":
            # G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
            imprimir_superheroe_promdio(lista, 'genero', 'M')
        elif respuesta == "8":
            # H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
            imprimir_superheroe_promdio(lista, 'genero', 'F')
        elif respuesta == "9":
            # I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores ()
            informar_nombres(lista, 'genero', 'altura', 'M', 'F', 'maximo', 'minimo')
        elif respuesta == "10":
            # J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
            imprimir(lista, 'color_ojos')
        elif respuesta == "11":
            # J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
            imprimir(lista, 'color_pelo')
        elif respuesta == "12":
            imprimir(lista, 'inteligencia')
        elif respuesta == "13":
            print("\nGracias por usar nuestro programa.\n")
            break
        else:
            print("\nLa opcion ingresada es incorrecta, intentalo nuevamente.\n")
            continue

menu_principal(lista_personajes)
