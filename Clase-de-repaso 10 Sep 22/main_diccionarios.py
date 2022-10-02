from data_stark import lista_personajes as lista_heroes

#Diccionarios

#Busca e imprime un heroe
'''
heroe_ejemplo = lista_heroes[7]
print(heroe_ejemplo)

{'nombre': 'Gamora',
'identidad': 'Gamora Zen Whoberi Ben Titan',
'empresa': 'Marvel Comics',
'altura': '183.65000000000001',
'peso': '77.769999999999996',
'genero': 'F',
'color_ojos': 'Yellow',
'color_pelo': 'Black',
'fuerza': '85',
'inteligencia': 'good'
}
'''

####################################################################################################
'''
heroe_ejemplo = lista_heroes[7]
# NO se pueden repetir las keys en los diccionarios (en caso de hacerlo reemplaza la key original)

dict_los_argento = {
    "nombre": "pepe",
}

nombres = ["Paola Argento", "Fatiga"]

for nombre in nombres:
    persona = dict_los_argento["nombre"]
    #los_argento["nombre"] += nombre --> concatena los nombres. En caso de ser numeros los suma.
    #los_argento["nombre"] += nombre --> reemplaza el nombre por cada nombre iterado
print(persona)

'''


####################################################################################################
'''
dict_numeros = {
    "numeros" : [1, 3, 12, 24 ,45 ,50]
}

lista_valores = dict_numeros["numeros"] #Accedo a los numeros de la lista (diccionario)

lista_pares = [] #Se crea antes del for.

for numero in lista_valores:
    #lista_aux = [] #ERROR... con cada iteracion la lista vielve a estar vacia.
    # numero pares
    if numero %2 == 0:
        # Lo guardo en un lista auxiliar
        lista_pares.append(numero)

#Tenemos la lista con numeros pares = lista_pares
# dict_numeros["numeros"] = lista_pares --> Reemplaza el dict con la lista_pares
dict_numeros["numeros_pares"] = lista_pares #--> Agrega al dict la lista_pares

print(dict_numeros)
'''

#########################################-FUNCIONES-#################################################
dict_numeros = {
    "numeros" : [1, 3, 12, 24 ,45 ,50]
}

lista_valores = dict_numeros["numeros"]

def calcular_numeros_par_impar(lista_numeros: list, resto: int) -> int:
    '''
    - Calcula los numeros pares de una lista pasada por parametro
    y los guardara en una lista auxiliar que solo contenga numeros pares.

    - Parametros:
        lista_numeros: la lista original a iterar
        resto: el valor que voy a evaluar para que me devuelva pares o impares

    - Retorna:
        una lista con numeros pares si lo hay, en caso contrario retorna una lista vacia
    '''
    lista_numeros_filtrados = []
    for numero in lista_numeros:
        if numero %2 == resto:
            lista_numeros_filtrados.append(numero)

    return lista_numeros_filtrados

lista_pares = calcular_numeros_par_impar(lista_valores, 0)
lista_impares = calcular_numeros_par_impar(lista_valores, 1)

dict_numeros["numeros_pares"] = lista_pares
dict_numeros["numeros_impares"] = lista_impares

print(dict_numeros)