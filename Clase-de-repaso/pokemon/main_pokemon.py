from data_pokemon import pokemones
from libreria_pokemon import *

while True:
    #Imprimimos menu
    #Tomar el dato
    #Switchear opciones

    respuesta = int(input('\nIngresa una opcion: \nOpcion 1: Imprimir nombre de pokemones \nOpcion 2:  \nOpcion 3: Salir \n> '))
    
    if respuesta == 1:
        imprimir_pokemones(pokemones)
    elif respuesta == 2:
        obtener_id_pokemon(pokemones)
    elif respuesta == 3:
        print('Gracias por usar el programa.')
        break
    else:
        print('Opcion incorrecta, ingrese nuevamente.')
        continue
