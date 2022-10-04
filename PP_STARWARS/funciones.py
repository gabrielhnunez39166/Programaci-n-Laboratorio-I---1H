import json

def cargar_json(ruta: str) -> list:
    '''
    - Carga un archivo json y devuelve una lista.
    - Recibe como parametro la ruta del archivo
    - Retorna una lista
    '''
    with open(ruta, 'r') as archivo:
        archivo_starwars = json.load(archivo)
    return archivo_starwars['results']

def ordenar_lista(lista: list, clave: str):
    '''
    - Ordena una lista en orden ascendente mediante una clave que indica en base a que se ordena.
    - Recibe como parametro una lista y una clave.
    - Retorna una lista ordenada.
    '''
    lista_a_ordenar = lista.copy()
    lista_derecha = []
    lista_izquierda = []

    if len(lista_a_ordenar) < 1:
        return lista_a_ordenar
    else:
        pivot = lista_a_ordenar[0]
        for personaje in lista_a_ordenar[1:]:
            if personaje[clave] > pivot[clave]:
                lista_derecha.append(personaje)
            else:
                lista_izquierda.append(personaje)
    
    lista_izquierda = ordenar_lista(lista_izquierda, clave)
    lista_izquierda.append(pivot)
    lista_derecha = ordenar_lista(lista_derecha, clave)
    return lista_izquierda + lista_derecha

def imprimir_personajes(lista: list, clave: str) -> str:
    '''
    - Imprime una lista mediante un formato en especifico, la lista se recibe por parametro.
    - Recibe como parametro un lista y una clave
    - Retorna un 
    '''
    lista_a_imprimir = ordenar_lista(lista, clave)

    for personaje in lista_a_imprimir:
        mensaje = '\nName: {0}\nHeight: {1}\nMass: {2}\nGender: {3}\n'
        mensaje = mensaje.format(personaje['name'], personaje['height'] ,personaje['mass'], personaje['gender'])
        print(mensaje)


def buscar_personaje_mas_alto_genero(lista: list, genero: str):
    '''
    - Busca el personaje mas alto de cada genero
    - Recibe como parametro una lista y una clave (genero)
    - Retorna el personaje mas alto
    '''
    lista_genero = []
    for personaje in lista:
        if personaje['gender'] == genero:
            lista_genero.append(personaje)
    
    lista_personaje_mas_alto = ordenar_lista(lista_genero, 'height')
    personaje_mas_alto = lista_personaje_mas_alto[-1]
    return personaje_mas_alto

def buscar_personaje(lista: list, personaje_a_buscar: str):
    '''
    - Busca el nombre del personaje que ingreso el usuario
    - Recibe como parametro una lista y el personaje a buscar
    - Retorna los datos del personaje si lo encuentra, n caso contrario un mensaje.
    '''
    personaje_encontrado = []
    for personaje in lista:
        if personaje_a_buscar == personaje['name']:
            personaje_encontrado.append(personaje)
    imprimir_personajes(personaje_encontrado, 'height')
