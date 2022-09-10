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
def buscar_nombres_superheroes(lista: list, clave: str, tipo: str) -> list:
    '''
    - Busca el nombre de superheroes.
    - Recibe como parametro una lista, la clave y el tipo.
    - Retorna una lista
    '''
    lista_superheroes = []
    for superheroes in lista:
        if (superheroes[clave] == tipo):
            nombre_superheroes = superheroes['nombre']
            lista_superheroes.append(nombre_superheroes)
    return lista_superheroes

# A - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
# B - Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
def imprimir_nombres_superheroes(lista: list, genero: str) -> str:
    '''
    - Imprime el nombre de los superheroes
    - Recibe como parametros una lista y el genero
    - Retorna un String
    '''
    if (genero == "M"):
        nombre = buscar_nombres_superheroes(lista, "genero", "M")
        print("\nSuperheroes masculinos: {0} \n".format(nombre))
    elif (genero == "F"):
        nombre = buscar_nombres_superheroes(lista, "genero", "F")
        print("\nSuperheroes femeninos: {0} \n".format(nombre))

# Calcular maximos y minimos
def calcular_max_min_m(lista: list, clave: str, tipo: str, genero: str) -> str:
    ''' 
        - Calcula el maximo o minimo en base a la clave recibida.

        - Recibe una lista de diccionarios, la clave que se utilizara para calcular, el tipo de calculo a realizar y el genero

        - Retorna el diccionario.
    '''
    maximo_minimo_m = lista[0]
    for superheroe in lista:
        if (genero == 'M'):
            if (tipo == "Maximo" and (float(superheroe[clave]) > float(maximo_minimo_m[clave]))):
                maximo_minimo_m = superheroe
            elif (tipo == "Minimo" and (float(superheroe[clave]) < float(maximo_minimo_m[clave]))):
                maximo_minimo_m = superheroe
    return maximo_minimo_m

def calcular_max_min_f(lista: list, clave: str, tipo: str, genero: str) -> str:
    maximo_minimo_f = lista[0]
    for superheroe in lista:
        if (genero == 'F'):
            if (tipo == "Maximo" and (float(superheroe[clave]) > float(maximo_minimo_f[clave]))):
                maximo_minimo_f = superheroe
            elif (tipo == "Minimo" and (float(superheroe[clave]) < float(maximo_minimo_f[clave]))):
                maximo_minimo_f = superheroe
    return maximo_minimo_f
             
#Imprimir maximo-minimo segun el genero
def imprimir_maximo_minimo(lista: list, genero: str, tipo: str) -> str:
    if genero == 'M':
        if (tipo == "Maximo"):
            print(calcular_max_min_m(lista, "altura", "Maximo", genero))
        elif (tipo == "Minimo"):
            print(calcular_max_min_m(lista, "altura", "Minimo", genero))
    elif genero == "F":
        if (tipo == "Maximo"):
            print(calcular_max_min_f(lista, "altura", "Maximo", genero))
        elif (tipo == "Minimo"):
            print(calcular_max_min_f(lista, "altura", "Minimo", genero))



