import json
import re

def importar_json(ruta: str) -> list:
    '''
    - Carga un archivo json
    - Recibe como parametro la ruta del archivo
    - Retorna un objeto del tipo lista
    '''

    with open(ruta, 'r') as archivo:
        archivo_pokedex = json.load(archivo)
    return archivo_pokedex

def listar_pokemones(lista: list) -> list:
    '''
    - Lista los pokemones que hay en la lista ingresada.
    - Recibe como parametro una lista.
    - Retorna una lista.
    '''

    copia_de_lista = lista.copy()
    lista_de_pokemones = []
    for pokemon in copia_de_lista:
        lista_de_pokemones.append(pokemon)
    return lista_de_pokemones

def imprimir_pokemones(lista: list) -> str:
    '''
    - Imprime por consola la lista de pokemones.
    - Recibe como parametro la lista de pokemones.
    - Retorna el mensaje de tipo string.
    '''
    for pokemon in lista:
        mensaje = '\n Id: {0} \n Nombre: {1} \n Tipo: {2} \n Evoluciones: {3} \n Poder: {4} \n Fortaleza: {5} \n Debilidad: {6}'
        mensaje = mensaje.format(pokemon['id'], pokemon['nombre'], pokemon['tipo'], pokemon['evoluciones'], pokemon['poder'], pokemon['fortaleza'], pokemon['debilidad'])
        print(mensaje)

def validar_input(lista: list) -> int:
    '''
    - Valida el input ingresado
    - Recibe como parametro la lista de pokemones
    - Retorna el input ingresado como un int
    '''
    input_a_validar = input('Ingrese la cantidad de pokemones a imprimir: Intente con un numero del 0 al {0}. \n> '.format(len(lista)))
    if int(input_a_validar) <= len(lista):
        if input_a_validar == 'all':
            input_a_validar = len(lista)
        else:
            input_a_validar = int(input_a_validar)
    else:
        input_a_validar = -1
    return input_a_validar
      
def respuesta_uno(lista: list) -> str:
    '''
    - Realiza la accion de la respuesta 1 del menu del programa
    - Recibe como parametro una lista
    - Retorna un string con los pokemones a imprimir por consola
    '''
    limite = validar_input(lista)
    if limite != -1:
        lista_a_imprimir = listar_pokemones(lista[:limite])
        mensaje = imprimir_pokemones(lista_a_imprimir)
    else:
        respuesta_uno(lista)
    return mensaje

def ordenar_lista(lista: list, clave: str = 'poder', orden: str = 'asc') -> list:
    '''
    - Ordena la lista de pokemones, por defecto la ordena por porder pero se puede ingresar una clave para ordenar por otro valor numerico. Tambien se ordena por defecto en orden ascendente, en caso contrario el usuario puede optar por imprimirlos en orden descendiente.
    - Recibe como parametro una lista, en caso de ser necesario una clave y el orden a ordenar la lista.
    - Retorna una lista ordenada.
    '''
    lista_a_ordenar = lista.copy()
    lista_derecha = []
    lista_izquierda = []

    if len(lista_a_ordenar) <= 1:
        return lista_a_ordenar
    else:
        pivot = lista_a_ordenar[0]
        for pokemon in lista_a_ordenar[1:]:
            if pokemon[clave] > pivot[clave]:
                lista_derecha.append(pokemon)
            else:
                lista_izquierda.append(pokemon)
    
    lista_izquierda = ordenar_lista(lista_izquierda, clave)
    lista_izquierda.append(pivot)
    lista_derecha = ordenar_lista(lista_derecha, clave)
    lista_ordenada = lista_izquierda + lista_derecha

    if orden == 'desc':
        lista_ordenada.reverse()

    return lista_ordenada

def respuesta_dos_tres(lista: list, clave) -> str:
    '''
    - Realiza la accion de la respuesta 2 del menu del programa
    - Recibe como parametro una lista y una clave (poder / id)
    - Retorna un string con los pokemones a imprimir por consola
    '''
    orden = input('Ordenar de manera ascendente o descendente: (asc / desc) \n> ')
    if orden != 'asc' and orden != 'desc':
        orden = input('Ordenar de manera ascendente o descendente: (asc / desc) \n> ')

    lista_ordenada = ordenar_lista(lista, clave, orden)
    imprimir_pokemones(lista_ordenada)

def calcular_promedio(lista: list, clave: str) -> float:
    '''
    - Calcula el promedio de cualquier key numerica
    - Recibe como parametro una lista y una clave
    - Retorna el promedio obtenido
    '''
    lista_pokemones = lista.copy()
    acumulador = 0
    contador = len(lista_pokemones)
    promedio = 0

    if len(lista_pokemones) > 0:
        for pokemon in lista_pokemones:
            acumulador += pokemon[clave]
    else:
        print('La lista esta vacia.')

    promedio = acumulador / contador
    return promedio

def filtrar_pokemones(lista: list, clave: str, min_max: str):
    lista_filtrada_ordenada = []
    promedio = calcular_promedio(lista, clave)
    for pokemon in lista:
        if min_max == 'max':
            if pokemon[clave] > promedio:
                lista_filtrada_ordenada.append(pokemon)
        elif min_max == 'min':
            if pokemon[clave] < promedio:
                lista_filtrada_ordenada.append(pokemon)
        lista_filtrada_ordenada = ordenar_lista(lista_filtrada_ordenada, clave)
    return lista_filtrada_ordenada

def respuesta_cuatro(lista: list, clave: str):
    '''
    - Realiza la accion de la respuesta 4 del menu del programa
    - Recibe como parametro una lista y una clave
    - Imprime el promedio y la lista de pokemones (filtrada y ordenada)
    '''
    promedio = calcular_promedio(lista, clave)
    print(f'\nEl promedio de pokemones es: {promedio}\n')

    min_max = input('Imprimir los pokemones menores o mayores al promedio? (min / max)\n> ')
    if min_max != 'min' and min_max != 'max':
        min_max = input('Imprimir los pokemones menores o mayores al promedio? (min / max)\n> ')
    
    lista_filtrada = filtrar_pokemones(lista, clave, min_max)

    imprimir_pokemones(lista_filtrada)


def buscar_pokemones(lista: list, clave: str, buscar: str):
    pokemones_encontrados = []
    if type(buscar) == int and (clave == 'poder' or clave == 'id'):
        buscar =  int(buscar)

    for pokemon in lista:
        if buscar in pokemon[clave]:
            pokemones_encontrados.append(pokemon)
    return pokemones_encontrados


def respuesta_cinco(lista: list):
    '''
    - Realiza la accion de la respuesta 5 del menu del programa
    - Recibe como parametro una lista
    - Imprime
    '''
    clave_a_buscar = input('Ingrese el parametro a buscar ("id", "nombre", "tipo", "evoluciones", "poder", "fortaleza" y "debilidad")\n> ')
    buscar = input('Ingrese el dato a buscar: ')

    pokemones_encontrados = buscar_pokemones(lista, clave_a_buscar, buscar)
    imprimir_pokemones(pokemones_encontrados)