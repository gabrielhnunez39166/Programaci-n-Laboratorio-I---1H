from data_stark import lista_personajes

""" lista_heroes = [{
"nombre": "Howard the Duck",
"identidad": "Howard (Last name unrevealed)",
"empresa": "Marvel Comics",
"altura": "79.349999999999994",
"peso": "18.449999999999999",
"genero": "M",
"color_ojos": "Brown",
"color_pelo": "Yellow",
"fuerza": "2",
"inteligencia": "average" }] """

# Buscar los nombres de cada superheroe
def buscar_superheroes(lista: list, clave: str, tipo: str) -> list:
    '''
    - Busca los superheroes.
    - Recibe como parametro una lista, la clave y el tipo.
    - Retorna una lista
    '''
    lista_superheroes = []
    for superheroes in lista:
        if (superheroes[clave] == tipo):
            nombre_superheroes = superheroes
            lista_superheroes.append(nombre_superheroes)
    return lista_superheroes

# A - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
# B - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
def imprimir_nombres_superheroes(lista: list, clave: str, genero: str) -> str:
    '''
    - Imprime el nombre de los superheroes
    - Recibe como parametros una lista y el genero
    - Retorna un String
    '''

    lista_superheroes = buscar_superheroes(lista, clave, genero)
    for nombre in lista_superheroes:
        print(nombre['nombre'])

# Calcular maximos y minimos
def calcular_max_min(lista: list, clave: str, tipo: str, genero: str):
    ''' 
        - Calcula el maximo o minimo en base a la clave recibida.
        - Recibe una lista de diccionarios, la clave que se utilizara para calcular, el tipo de calculo a realizar y el genero
        - Retorna el diccionario.
    '''
    lista_superheroes = buscar_superheroes(lista, 'genero', genero)
    if genero == ('F' or 'M'):
        max_min = lista_superheroes[0]

    for superheroe in lista_superheroes:
        if tipo == "maximo" and (float(superheroe[clave]) > float(max_min[clave])):
            max_min = superheroe
        elif tipo == "minimo" and (float(superheroe[clave]) < float(max_min[clave])):
            max_min = superheroe
    return max_min

# Superheroe mas alto o mas bajo
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M
# F. Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F
def imprimir_superheroes_max_min(lista: list, clave: str, tipo: str, genero: str) -> dict:
    print(calcular_max_min(lista, clave, tipo, genero))

# Altura promedio
def calcular_promedio(lista: list, clave: str, genero: str):
    lista_superheroes = buscar_superheroes(lista, clave, genero)
    acumulador = 0
    contador = len(lista_superheroes)
    for superheroe in lista_superheroes:
        acumulador += float(superheroe['altura'])
    promedio = acumulador / contador
    return promedio

# G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
# H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
def imprimir_superheroe_promdio(lista: list, clave: str, genero: str):
    print('La altura promedio es de {0}'.format(calcular_promedio(lista, clave, genero)))


# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores ()
def informar_nombres(lista: list, clave_genero: str, clave_altura: str, genero_m: str, genero_f: str, max: str, min: str) -> str:
    print('\nSuperheroes masculinos: ') 
    imprimir_nombres_superheroes(lista, clave_genero, genero_m)
    print('\nSuperheroes femeninos: ') 
    imprimir_nombres_superheroes(lista, clave_genero, genero_f)

    print('\nSuperheroe masculino mas alto: \n{0}\n'.format(calcular_max_min(lista, clave_altura, max, genero_m)['nombre']))
    print('\nSuperheroe femenino mas alto: \n{0}\n'.format(calcular_max_min(lista, clave_altura, max, genero_f)['nombre']))
    print('\nSuperheroe masculino mas bajo: \n{0}\n'.format(calcular_max_min(lista, clave_altura, min, genero_m)['nombre']))
    print('\nSuperheroe femenino mas bajo: \n{0}\n'.format(calcular_max_min(lista, clave_altura, min, genero_f)['nombre']))

# Determinar el color
def determinar_color(lista: list, clave: str,):
    lista_color = []
    for superheroe in lista:
        lista_color.append(superheroe[clave])

    dict_color = {}
    for color in lista_color:
        if color in dict_color:
            dict_color[color] += 1
        else:
            dict_color[color] = 1

    return dict_color


# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
def imprimir(lista: list, clave: str,):
    color_a_imprimir = determinar_color(lista, clave)

    if clave == 'color_ojos':
        mensaje = f'El color de ojos por cantidad es: {color_a_imprimir}'
    elif clave == 'color_pelo':
        mensaje = f'El color de pelo por cantidad es: {color_a_imprimir}'
    elif clave == 'inteligencia':
        mensaje = f'Superheroes por nivel de inteligencia:\n {determinar_tipo_inteligencia(lista, clave)}'
    print(mensaje)



# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’)
#{'', 'good', 'high', 'average'}


def determinar_tipo_inteligencia(lista: list, clave: str):
    nivel_inteligencia = []
    for superheroe in lista:
        nivel_inteligencia.append(superheroe[clave])

    superheroe_por_nivel_inteligencia = {}
    for inteligencia in nivel_inteligencia:
        if inteligencia in superheroe_por_nivel_inteligencia:
            superheroe_por_nivel_inteligencia[inteligencia] += 1
        else:
            superheroe_por_nivel_inteligencia[inteligencia] = 1
    return superheroe_por_nivel_inteligencia



#Listar todos los superheroes agrupado por color de ojos.
