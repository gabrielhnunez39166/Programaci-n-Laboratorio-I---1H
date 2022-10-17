from data_stark import lista_personajes

'''
"nombre": "Howard the Duck",
    "identidad": "Howard (Last name unrevealed)",
    "empresa": "Marvel Comics",
    "altura": "79.349999999999994",
    "peso": "18.449999999999999",
    "genero": "M",
    "color_ojos": "Brown",
    "color_pelo": "Yellow",
    "fuerza": "2",
    "inteligencia": ""
'''

lista_vacia = []
def stark_normalizar_datos(lista: list) -> list:
    '''
    - Normaliza los datos de la lista importada.
    - Recibe como parametro una lista.
    - Retorna un lista con los datos normalizados.
    '''
    if len(lista) > 0:
        lista_personajes_normalizado = []
        for superheroe in lista:

            while type(superheroe['altura']) != float:
                superheroe['altura'] = float(superheroe['altura'])

            while type(superheroe['peso']) != float:
                superheroe['peso'] = float(superheroe['peso'])
            
            while type(superheroe['fuerza']) != int:
                superheroe['fuerza'] = int(superheroe['fuerza'])
            
            lista_personajes_normalizado.append(superheroe)
            
            """ mensaje = '\nNombre: {0} \nIdentidad: {1}  \n Empresa: {2}\n Altura: {3}\n Peso: {4}\n Genero: {5}\n Color de ojos: {6}\n Color de pelo: {7}\n Fuerza: {8}\n Inteligencia: {9}\n'

            print(mensaje.format(superheroe['nombre'], superheroe['identidad'], superheroe['empresa'], superheroe['altura'], superheroe['peso'], superheroe['genero'], superheroe['color_ojos'], superheroe['color_pelo'], superheroe['fuerza'], superheroe['inteligencia'])) """
    else:
        print('\nError: Lista de héroes vacía\n')
    
    return lista_personajes_normalizado


def obtener_nombre(heroe: dict) -> str:
    '''
    - Recibe por parametro un diccionario heroe

    - Retorna un string "Nombre: Howard the Duck"
    '''

    lista_nombre = []
    for nombre_del_hero in heroe:
        nombre = nombre_del_hero['nombre']
        lista_nombre.append(nombre)
    return lista_nombre




def imprimir_dato(dato: str):
    '''
    - Recibe por parametro un string
    - Imprime el string recibido
    - No tiene retorno
    '''
    for nombre in dato:
        cadena = f'Nombre: {nombre}'
        print(cadena)


def stak_imprimir_nombres_heroes(lista_heroes: list):
    if len(lista_heroes) > 0:
        nombres = obtener_nombre(lista_heroes)
        print(imprimir_dato(nombres))
    else:
        print('-1')



def obtener_nombre_y_dato(heroe: dict, dato: str) -> str:
    '''
    - Recibe por parametro un diccionario que representa al heroe y
      un dato (altura, peso, fuerza, etc)
    - Retorna un string (Nombre: nombre | dato: dato)
    '''

    for nombre_y_dato in heroe:
        nombre = nombre_y_dato['nombre']
        dato_obtenido = nombre_y_dato[dato]
        cadena = f'Nombre: {nombre} | {dato}: {dato_obtenido}'
        print(cadena)


def stark_imprimir_nombres_alturas(lista_heroes: list):
    '''
    - Recibe por parametro la lista de heroes
    - Itera e imprime el nombre usando la funcion obtener_nombre_y_dato()
    - Imprime el nombre y la altura del heroe, en caso que la lista este vacia imprime -1
    '''

    if len(lista_heroes) > 0:
        nombre_y_altura = obtener_nombre_y_dato(lista_heroes, "altura")
        print(nombre_y_altura)
    else:
        print('-1')



def calcular_max(lista_heroes: list, dato: str) -> list:
    '''
    - Recibe como parametro la lista de heroes y una key la cual representa el dato a ser evaluado.
    - calcula el dato ingresado y devuelve el maximo (peso, altura y fuerza).
    - Retorna al heroe que tenga el dato mas alto.
    '''

    maximo = lista_heroes[0]
    for heroe in lista_heroes:
        if float(heroe[dato]) > float(maximo[dato]):
            maximo = heroe
    return maximo


def calcular_min(lista_heroes: list, dato: str) -> list:
    '''
    - Recibe como parametro la lista de heroes y una key la cual representa el dato a ser evaluado.
    - calcula el dato ingresado y devuelve el minimo (peso, altura y fuerza).
    - Retorna al heroe que tenga el dato mas bajo.
    '''

    minimo = lista_heroes[0]
    for heroe in lista_heroes:
        if float(heroe[dato]) < float(minimo[dato]):
            minimo = heroe
    return minimo



def calcular_max_min_dato(lista_heroes: list, tipo_de_calculo: str, dato: str):
    '''
    - Recibe como parametro la lista de heroes, el calculo a realizar y la key del dato a calcular.
    - Se calcula el maximo / minimo del dato ingresado.
    - Retorna el heroe que cumpla con la condicion pedida.
    '''
    
    if tipo_de_calculo == 'maximo':
        heroe_a_retornar = calcular_max(lista_heroes, dato)
    elif tipo_de_calculo == 'minimo':
        heroe_a_retornar = calcular_min(lista_heroes, dato)
    return heroe_a_retornar


print('Fuerza maxima: {0} \n'.format(calcular_max_min_dato(lista_personajes, 'maximo', 'fuerza')))
print('Fuerza minima: {0} \n'.format(calcular_max_min_dato(lista_personajes, 'minimo', 'fuerza')))
print('Altura maxima: {0} \n'.format(calcular_max_min_dato(lista_personajes, 'maximo', 'altura')))
print('Altura minima: {0} \n'.format(calcular_max_min_dato(lista_personajes, 'minimo', 'altura')))
print('Fuerza maxima: {0} \n'.format(calcular_max_min_dato(lista_personajes, 'maximo', 'peso')))
print('Fuerza minima: {0} \n'.format(calcular_max_min_dato(lista_personajes, 'minimo', 'peso')))