from data_stark import lista_personajes as lista_heroes

#Listas.
pokemones = [
    "newtwo",
    "moltres",
    "pikachu",
    "chamander",
]


#Append
#Agregar un elemento a la lista [Al final de la lista]
'''
print("Lista antes de agregar: {0}".format(pokemones))
pokemones.append("bulbasaur")
print("Lista despues de agregar: {0}".format(pokemones))
'''


#Recorrer elementos de una lista
'''
1 - Posee indices donde estaran ubicados los elementos que contendran
2 - Los indices son numericos (van de 0 a la cantidad de indices -1(ultimo elemento))
3 - Los indices son en base 0
'''

#for clasico
print("\nFor clasico")
for indice in range(0, len(pokemones)): #El rango recorre [0, 7)
    print(pokemones[indice])

#for-each
print("\nFor Each")
for pokemon in pokemones:
    print(pokemon)
    pass
