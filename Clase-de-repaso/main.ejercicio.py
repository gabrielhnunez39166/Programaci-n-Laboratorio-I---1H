from data_stark import lista_personajes as lista_heroes

def calcular_max_min_dato(heroes: list, calculo: str, key: str):
    pass

def obtener_nombre_y_dato(heroe: dcit, key: str) -> str:
    pass

def imprimir_dato(texto: str):
    pass

def stark_calcular_imprimir_heroe_genero(heroes: list, calculo: str, key: str):
    if len(heroes) > 0:
        tamanio = 'mayor'
        if calculo == 'minimo':
            tamanio == 'menor'
        
        heroe = calcular_max_min_dato(heroes, calculo, key)
        #imprimir nombre y valor
        heroe_str = obtener_nombre_y_dato(heroe, key)
        mensaje = "{0} {1} - {2}".format(tamanio, key, heroe_str)

        imprimir_dato(mensaje)
