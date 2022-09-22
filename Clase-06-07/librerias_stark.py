from data_stark import lista_personajes
import re


def extraer_iniciales(nombre_heroe: str) -> str:
    if nombre_heroe.count('the'):
        lista_nombre = nombre_heroe.replace('the', ' ')
        lista_nombre = lista_nombre.strip('  ')
        lista_nombre = lista_nombre.split(' ')
        primer_inicial = lista_nombre[0][:1]
        segunda_inicial = lista_nombre[3][:1]
        print(f'{primer_inicial}.{segunda_inicial}')

    elif nombre_heroe.count('-'):
        lista_nombre = nombre_heroe.replace('-', ' ')
        lista_nombre = lista_nombre.split(" ")
        primer_inicial = lista_nombre[0][:1]
        segunda_inicial = lista_nombre[1][:1]
        print(f'{primer_inicial}.{segunda_inicial}.')

    elif nombre_heroe.count(' '):
        lista_nombre = nombre_heroe.split(" ")
        primer_inicial = lista_nombre[0][:1]
        segunda_inicial = lista_nombre[1][:1]
        print(f'{primer_inicial}.{segunda_inicial}.')
    elif nombre_heroe == '':
        print('N/A')


def definir_iniciales_nombre (heroe: dict):
    # Agregar clave 'iniciales' y el valor sera 'extraer_iniciales'
    