#ORDENAR LISTAS SIMPLE (UNICO CRITERIO) 1ER METODO

lista = [14,5,20,10,23,15,7,16,29,21,-102,99,0]

def buscar_minimo(lista_a_buscar: list) -> int:
    '''
    - Busca un minimo en una lista de elementos dict
    - Recibe una lista de elementos dict
    - Retorna el indice del elemento encontrado
    '''
    minimo = 0
    for i in range(len(lista_a_buscar)):
        if lista_a_buscar[i] < lista_a_buscar[minimo]:
            minimo = i
    return minimo

def ordenar_lista(lista: list) -> list:
    'Creo una copia de la lista'
    copia_lista = lista[:]
    'Creo un lista vacia donde se guardaran los numeros ordenados'
    lista_ordenada = []
    '''La forma de saber cuando el algoritmo termina es
    con un while preguntando si la lista contiene algun numero'''
    while len(copia_lista) > 0:
        minimo = buscar_minimo(copia_lista)
        '''Elimino el numero minimo de la copia de lista
        y se lo agrego a la lista ordenada'''
        lista_ordenada.append(copia_lista.pop(minimo))

    return lista_ordenada

""" lista_ordenada = ordenar_lista(lista)
print(lista_ordenada)
 """


#ORDENAR LISTAS SIMPLE (UNICO CRITERIO) 2DO METODO
def ordenar_lista_dos(lista: list) -> list:
    'Creo una copia de la lista'
    copia_lista = lista[:] #Se puede usar lista.copy()
    flag_swap = True
    'Mientras que el flag_swap sea verdadero se sigue ordenando la lista'
    while flag_swap == True:
        flag_swap = False
        limite = 1
        'Genero un for que recorra el largo de la lista mediante un i(index) y le resto el index final -1'
        for i in range(len(copia_lista) - limite):
            'Si el indice i es mayor al indice siguiente cambio el orden de los indices'
            if copia_lista[i] > copia_lista[i+1]:
                copia_lista[i], copia_lista[i+1] = copia_lista[i+1], copia_lista[i]
                flag_swap = True
        limite += 1

    return copia_lista

""" lista_ordenada_dos = ordenar_lista_dos(lista)
print(lista_ordenada_dos) """


#ORDENAR LISTAS SIMPLE (UNICO CRITERIO) 3ER METODO
#ESTE CONCEPTO SE LLAMA RECURSIVIDAD -> FUNCION QUE SE LLAMA A SI MISMA

def ordenar_lista_recursividad(lista_a_ordenar: list) -> list:
    'Creo dos listas que representan el lado izquierdo y derecho del pivot'
    lista_derecha = []
    lista_izquierda = []
    '''Genero un if, si la cantidad de elementos en la lista es menor o igual a 1 retorno el pivot (en una lista)
    en caso contrario pregunto si es mas grande o mas chico
    en caso de ser mas grande lo agrego a la lista derecha
    en caso de ser mas chico o igual lo agrego a la lista izquierda'''
    if len(lista_a_ordenar) <= 1:
        return lista_a_ordenar
    else:
        'Numero random de la lista que se quiere ordenar'
        pivot = lista_a_ordenar[0]
        for elemento in lista_a_ordenar[1:]:
            if elemento > pivot:
                lista_derecha.append(elemento)
            else:
                lista_izquierda.append(elemento)
    '''
    Para retornar la lista ordenada:
    - Aplico recursividad a la lista izquierda
    - Le agrego el ultimo elemento (pivot) a la lista izquierda
    - Aplico recursividad a la lista derecha
    - Retorno la lista con los numeros ordenados
    '''
    lista_izquierda = ordenar_lista_recursividad(lista_izquierda)
    lista_izquierda.append(pivot)
    lista_derecha = ordenar_lista_recursividad(lista_derecha)
    return lista_izquierda + lista_derecha

print(ordenar_lista_recursividad(lista))




#ORDENAR LISTAS SIMPLE (UNICO CRITERIO) 4TO METODO SWAP

