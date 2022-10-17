import json

def cargar_json(path: str) -> list:
    with open(path, 'r') as file: 
        buffer_dict = json.load(file)
    return buffer_dict['paulina']

def mostrar(lista: list):
    for elemento in lista:
        print('{0}-{1}-{2}'.format(elemento['views'], elemento['length'], elemento['title']))


def buscar_minimo(lista: list, key: str) -> int:
    '''
    - Busca un minimo en una lista de elementos dict
    - Recibe una lista de elementos dict con clave -key- y la clave
    - Retorna el indice del elemento encontrado
    '''
    retorno = -1
    if len(lista) > 0:
        i_min = 0
        i = 0
        for i in range(len(lista)):
            if lista[i][key] < lista[i_min][key]:
                i_min = i
    retorno = i_min

    return retorno