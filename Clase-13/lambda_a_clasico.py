# MIT License
#
# Copyright (c) 2022 [UTN FRA](https://fra.utn.edu.ar/) All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

lista_palabras = [
    "goKU", "vEgETa", "FrIEzA", "CELl", "BeERuS", 'kriLLin'
]


############### Refactorizar a la version clasica de la funcion ###############
superficie_circulo = lambda x: pow(x, 2) * 3.1415
#print(f'Superficie de circulo: {round(superficie_circulo(15), 2)}')

def superficie_del_circulo(x: int):
    base = x
    exponente = 2
    pi = 3.1415
    sup_circulo = (base ** exponente) * pi
    print(f'Superficie del circulo: {round(sup_circulo, 2)}')

#superficie_del_circulo(15)



############### Refactorizar a la version clasica ###############
minisculizar = lambda x: str(x).lower()
#print(f'Lista Minuscula: {minisculizar(lista_palabras)}')

def minusculizar(lista: list):
    palabras_minusculas = []
    for palabra in lista:
        minuscula = palabra.lower()
        palabras_minusculas.append(minuscula)
    print(f'Lista Minuscula: {palabras_minusculas}')

#minusculizar(lista_palabras)


############### Refactorizar a la version clasica ###############
capitalizar = lambda x: str(x).capitalize()
lista_mapeada = list(map(capitalizar, lista_palabras))
#print(f'Lista Capitalizada: {lista_mapeada}')

heroes = [
    "goKU", "vEgETa", 'kriLLin'
]

villanos = [
    "FrIEzA", "CELl", "Majin Buu"
]

ataques = [
    "Kame hame ha", "Final flash", "Kienzan"
]

for heroe, ataque, villano in zip(heroes, ataques, villanos):
    pass
    #print(f'{heroe.capitalize()} Lanza un {ataque.capitalize()} a {villano.capitalize()}')


def capitalizar_y_mapear_lista(lista_1: list, lista_2: list, lista_3: list):
    for elemento_1, elemento_2, elemento_3 in zip(lista_1, lista_2, lista_3):
        print(f'{elemento_1.capitalize()} lanza un {elemento_2.capitalize()} a {elemento_3.capitalize()}')

#capitalizar_y_mapear_lista(heroes, ataques, villanos)