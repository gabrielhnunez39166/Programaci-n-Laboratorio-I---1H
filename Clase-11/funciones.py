import json
import re

def cargar_json(path: str) -> list:
    '''
    - Carga un archivo json
    - Recibe como parametro la ruta del archivo
    - Retorna un objeto del tipo lista
    '''

    with open(path, 'r') as file:
        file_json = json.load(file)
    return file_json['heroes']

def cantidad_a_imprimir(lista: list) -> int:
    '''
    - Recibe mediante un input el numero de heroes que quiere imprimir, si el input recibe un all retorna el maximo de la lista, caso contrario retorna el numero a imprimir.
    - Retorna un int
    '''
    cant_a_imprimir = input('\nIngrese la cantidad a imprimir o ingrese -all- para imprimir la lista completa:\n')
    if cant_a_imprimir == 'all':
        cant_a_imprimir = len(lista)
    else:
        cant_a_imprimir = int(cant_a_imprimir)
    return cant_a_imprimir


def generar_lista_heroes(lista: list) -> list:
    '''
    - Crea una copia de la lista y en base a esta genera una lista nueva a la cual se le agrega todos los elementos de la copia.
    - Recibe como parametro una lista.
    - Retorna una lista.
    '''
    lista_copia = lista.copy()
    lista_nueva = []
    for elemento in lista_copia:
        lista_nueva.append(elemento)
    return lista_nueva


def imprimir_lista(lista: list) -> str:
    '''
    - Imprime la lista de los superheroes.
    - Recibe como parametro la lista de los superheroes
    - Retorna un String mostrando los datos de los superheroes.
    '''
    for heroe in lista:
        mensaje = '\nNombre: {0} \nIdentidad: {1} \nAltura: {2} \nPeso: {3} \nFuerza: {4} \nInteligencia: {5}'
        mensaje = mensaje.format(heroe['nombre'], heroe['identidad'], heroe['altura'], heroe['peso'], heroe['fuerza'], heroe['inteligencia'])
        print(mensaje)

def imprimir_mensaje(clave: str, promedio: float) -> str:
    '''
    - Imprime el mensaje sobre el promedio de los superheroes.
    - Recibe como parametro la clave que es a lo que le sacamos el promedio y el resultado del promedio.
    - Retorna el mensaje como string.
    '''
    mensaje = 'El promedio de {0} es de: {1}'.format(clave, promedio)
    print(mensaje)

def ordenar_lista(lista: list, clave: str, orden: str = 'asc') -> list:
    '''
    - Ordena una lista de menor a mayor y si el usuario lo requiere se devuelve la lista inversa
    - Recibe como parametro una lista, la clave la cual queremos ordenar y el orden en el que quedara la lista.
    - Retorna una lista ordenada.
    '''
    lista_a_ordenar = lista.copy()
    lista_derecha = []
    lista_izquierda = []

    if len(lista_a_ordenar) <= 1:
        return lista_a_ordenar
    else:
        pivot = lista_a_ordenar[0]
        for elemento in lista_a_ordenar[1:]:
            if float(elemento[clave]) > float(pivot[clave]):
                lista_derecha.append(elemento)
            else:
                lista_izquierda.append(elemento)

    lista_izquierda = ordenar_lista(lista_izquierda, clave, orden)
    lista_izquierda.append(pivot)
    lista_derecha = ordenar_lista(lista_derecha, clave, orden)
    lista_ordenada = lista_izquierda + lista_derecha

    if orden == 'desc':
        lista_ordenada.reverse()


    return lista_ordenada


def validar_clave() -> str:
    '''
    - Valida la clave ingresada por el usuario.
    - No recibe paramertos.
    - Retorna la clave validada como un string.
    '''
    clave = input('Que promedio calcular? (altura / peso / fuerza)\n')
    while clave != 'altura' and clave != 'peso' and clave != 'fuerza':
        clave = input('Que promedio calcular? (altura / peso / fuerza)\n')
    return str(clave)


def calcular_promedio(lista: list, clave: str) -> float:
    '''
    - Calcula el promedio de la lista en base a la clave ingresada.
    - Recibe como parametro la lista y la clave a la cual se le calcula el promedio.
    - Retorna el promedio como float.
    '''
    promedio = 0
    cantidad = 0
    contador = len(lista)

    if len(lista) > 0:
        for elementos in lista:
            cantidad += elementos[clave]
        
        promedio = cantidad / contador

    return promedio


def filtrar_promedio(lista: list, clave: str, max_min: str) -> list:
    '''
    - Filtra una lista en base a un promedio y devuelve los elementos mayores o menores al promedio obtenido.
    - Recibe como parametro una lista, la clave a promediar y la opcion de maximo o minimo a devolver como lista.
    - Retorna una lista filtrada segun lo pedido por el usuario.
    '''
    lista_filtrada = []
    for elemento in lista:
        if max_min == 'maximo':
            if elemento[clave] > calcular_promedio(lista, clave):
                lista_filtrada.append(elemento)
        elif max_min == 'minimo':
            if elemento[clave] < calcular_promedio(lista, clave):
                lista_filtrada.append(elemento)
    return lista_filtrada


def buscar_heroes_inteligencia(lista: list, clave: str, nivel_inteligencia: str) -> list:
    '''
    - Busca en una lista los heroes en base a su inteligencia la cual es ingresada por el usuario.
    - Recibe como parametro una lista, la clave (es inteligencia pero queda como clave para una futura modificacion) y el nivel de inteligencia por el que se quiere imprimir.
    - Retorna una lista filtrada por el nivel de inteligencia pedido.
    '''
    lista_inteligencia = []

    for elemento in lista:
        if elemento[clave] == nivel_inteligencia:
            lista_inteligencia.append(elemento)
    return lista_inteligencia
            
def validar_nivel_de_inteligencia() -> str:
    '''
    - Valida el nivel de inteligencia ingresado por el usuario.
    - No recibe ningun parametro.
    - Retorna el nivel de inteligencia como string.
    '''
    nivel_de_inteligencia = input('Ingrese el nivel de inteligencia a buscar: (sin nivel | good | average | high\n')
    if nivel_de_inteligencia == 'sin nivel':
        nivel_de_inteligencia = ''
    elif nivel_de_inteligencia != 'good' and nivel_de_inteligencia != 'average' and nivel_de_inteligencia != 'high':
        nivel_de_inteligencia = input('Ingrese el nivel de inteligencia a buscar: ('' | good | average | high\n')

    return nivel_de_inteligencia



def exportar_a_csv(lista: list, ruta: str):
    '''
    - Exporta a csv la lista ingresada.
    - Recibe como parametro una lista y la ruta donde se exporta el archivo scv.
    - Retorna el archivo csv.
    '''
    with open(ruta, 'w') as file:
        for heroe in lista:
            file.write('{0}, {1}, {2}, {3}, {4}, {5}\n'.format(heroe['nombre'], heroe['identidad'], heroe['altura'], heroe['peso'], heroe['fuerza'], heroe['inteligencia']))


