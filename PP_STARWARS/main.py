'''
1 - Listar los personajes ordenados por altura
2 - Mostrar el personaje mas alto de cada genero
3 - Ordenar los personajes por peso
4 - Armar un buscador de personajes 
5 - Exportar lista personajes a CSV
6 - Salir
'''
import funciones

def starwars_app():
    lista_personajes = funciones.cargar_json("data.json")
    
    while(True):
        print("1 - Listar los personajes ordenados por altura\n2 - Mostrar el personaje mas alto de cada genero\n3 - Ordenar los personajes por peso\n4 - Armar un buscador de personajes\n5 - Exportar lista personajes a CSV\n6 - Salir\n")
        respuesta = input()
        if(respuesta=="1"):
            funciones.imprimir_personajes(lista_personajes, 'height')
        elif(respuesta=="2"):
            genero = input('Ingrese el genero del personaje: (male, n/a, female)\n> ')
            if genero != 'male' and genero != 'n/a' and genero != 'female':
                genero = input('Ingrese el genero del personaje: (male, n/a, female)\n> ')
            personaje = funciones.buscar_personaje_mas_alto_genero(lista_personajes, genero)
            personaje = '\nName: {0}\nHeight: {1}\nMass: {2}\nGender: {3}\n'.format(personaje['name'], personaje['height'] ,personaje['mass'], personaje['gender'])
            print(personaje)
        elif(respuesta=="3"):
            funciones.imprimir_personajes(lista_personajes, 'mass')
        elif(respuesta=="4"):
            print("4 - Armar un buscador de personajes \n")
        elif(respuesta=="5"):
            print("5 - Exportar lista personajes a CSV\n")
        elif(respuesta=="6"):
            break


starwars_app()

