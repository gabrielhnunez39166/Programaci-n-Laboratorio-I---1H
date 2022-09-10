from data_pokemon import pokemones

#01.1
def obtener_nombre_pokemon (pokemon: dict) -> str:
    '''
    - Recibe un dicionario por parametro que repersenta a un pokemon

    - Retorna el valor de la key "nombre" como un string
    '''
    nombre_pokemon = pokemon['nombre']
    return nombre_pokemon

#01.2
def imprimir_pokemones(pokemones: list) -> None:
    '''
    - Recibe la lista de pokemones, obtiene el nombre de cada uno y los imprime uno a uno.

    - Parametros: La lista de diccionarios de pokemones

    - Retorno: None
    '''
    if len(pokemones) > 0:
        for pokemon in pokemones:
            nombre = obtener_nombre_pokemon(pokemon)
            print(nombre)

#02.1
def tiene_id_par(pokemones: dict):
    for pokemon in pokemones:
        if (pokemon['id'] % 2 == 0):
            valor = True
        elif (pokemon['id'] % 2 == 1):
            valor = False
    return valor


#02.2
def obtener_id_pokemon(pokemones: dict) -> str:
    lista_id_pokemon = []

    for pokemon in pokemones:
        id = pokemon['id']
        lista_id_pokemon.append(id)
    lista_id_pokemon
    print(lista_id_pokemon)

