import funciones


def funcion_ejecutar_programa():
    lista_heroes = funciones.cargar_json('data_stark.json')
    #print(lista_heroes)
    ruta = 'heroes.csv'
    lista_a_csv = []
    def menu(lista: list):
        '''
        - Menu que llama y ejecuta las funcionalidades de archivos externos
        - Llama a un archivo
        - No retorna
        '''
        while(True):
            print('''\nIngrese una opcion: \n1 - Listar superheroes \n2 - Ordenar lista por altura \n3 - Ordenar lista por peso \n4 - Calcular promedio \n5 - Listar por inteligencia \n6 - Exportar CSV \n7 - Salir''')
            respuesta = input('\n> ')
            if respuesta == '1':
                limite = funciones.cantidad_a_imprimir()
                if limite <= len(lista):
                    lista_a_imprimir = funciones.generar_lista_heroes(lista)[:limite]
                    funciones.imprimir_lista(lista_a_imprimir)
                else:
                    print('El numero ingresado es mayor al largo de la lista.')
                lista_a_csv = lista_a_imprimir
            elif respuesta == '2':
                acd_desc = input('Ordenar de manera ascendente o descendente? asc/desc\n')
                lista_a_imprimir = funciones.ordenar_lista(lista, 'altura', acd_desc)
                funciones.imprimir_lista(lista_a_imprimir)
                lista_a_csv = lista_a_imprimir
            elif respuesta == '3':
                acd_desc = input('Ordenar de manera ascendente o descendente? asc/desc\n')
                lista_a_imprimir = funciones.ordenar_lista(lista, 'peso', acd_desc)
                funciones.imprimir_lista(lista_a_imprimir)
                lista_a_csv = lista_a_imprimir
            elif respuesta == '4':
                clave = funciones.validar_clave()
                filtrar = input('Filtrar por maximo o minimo?\n')
                flotante_retornado = funciones.calcular_promedio(lista, clave)
                funciones.imprimir_mensaje(clave, flotante_retornado)
                lista_promedio = funciones.filtrar_promedio(lista, clave, filtrar)
                lista_promedio = funciones.ordenar_lista(lista_promedio, clave, 'asc')
                funciones.imprimir_lista(lista_promedio)
                lista_a_csv = lista_promedio
            elif respuesta == '5':
                nivel_de_inteligencia = funciones.validar_nivel_de_inteligencia()
                lista_a_imprimir = funciones.buscar_heroes_inteligencia(lista, 'inteligencia', nivel_de_inteligencia)
                funciones.imprimir_lista(lista_a_imprimir)
                lista_a_csv = lista_a_imprimir
            elif respuesta == '6':
                funciones.exportar_a_csv(lista_a_csv, ruta)
            elif respuesta == '7':
                print('\nSi no podemos proteger la Tierra, puedes estar seguro de que la vengaremos\n')
                break
            else:
                print('\nLa opcion ingresada es incorrecta. Intente nuevamento.')
                continue

    menu(lista_heroes)

funcion_ejecutar_programa()