"""
Hugo Gabriel Nunez
"""
#
flag_mas_caro = False
precio_barbijo_mas_caro = 0
acumulador_unidad_mas_cara = 0
fabricante_unidad_mas_cara = ""

acumulador_cantidad_barbijo = 0
acumulador_cantidad_jabon = 0
acumulador_cantidad_alcohol = 0

item_con_mas_unidades = ""
fabricante_con_mas_unidades = ""

mensaje = ""



#Carga de 5 productos
for i in range(5):

    #Tipo
    tipo = input("Ingrese el tipo: ")
    while(tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol"):
        tipo = input("Ingrese el tipo: ")
    
    #Precio
    precio = input("ingrese el precio (entre 100 y 300): ")
    precio = float(precio)
    while(precio < 100 or precio > 300):
        precio = input("ingrese el precio (entre 100 y 300): ")
        precio = float(precio)
    
    #Cantidad de unidades
    cantidad_de_unidades = input("Ingrese la cantidad de unidades: ")
    cantidad_de_unidades = int(cantidad_de_unidades)
    while(cantidad_de_unidades < 1 or cantidad_de_unidades > 1000):
        cantidad_de_unidades = input("Ingrese la cantidad de unidades: ")
        cantidad_de_unidades = int(cantidad_de_unidades)
    
    #Marca
    marca = input("Ingrese la marca: ")
    while(marca == ""):
        marca = input("Ingrese la marca: ")
    
    #Fabricante
    fabricante = input("Ingrese el fabricante: ")
    while(fabricante == ""):
        fabricante = input("Ingrese el fabricante: ")
    
    #Match por tipo
    if(tipo == "barbijo"):
                if(flag_mas_caro == False):
                    flag_mas_caro = True
                    precio_barbijo_mas_caro = precio
                    acumulador_cantidad_barbijo += cantidad_de_unidades
                    fabricante_unidad_mas_cara = fabricante
                elif(precio > precio_barbijo_mas_caro):
                    precio_barbijo_mas_caro = precio
                    acumulador_cantidad_barbijo += cantidad_de_unidades
                    fabricante_unidad_mas_cara = fabricante
    elif(tipo == "jabon"):
            acumulador_cantidad_jabon += cantidad_de_unidades

    elif(tipo == "alcohol"):
            acumulador_cantidad_alcohol += cantidad_de_unidades

#Item con mas unidades
if (acumulador_cantidad_barbijo > acumulador_cantidad_alcohol and acumulador_cantidad_barbijo > acumulador_cantidad_jabon):
    item_con_mas_unidades = tipo
    fabricante_con_mas_unidades = fabricante
elif(acumulador_cantidad_alcohol > acumulador_cantidad_barbijo and acumulador_cantidad_alcohol > acumulador_cantidad_jabon):
    item_con_mas_unidades = tipo
    fabricante_con_mas_unidades = fabricante
elif(acumulador_cantidad_jabon > acumulador_cantidad_barbijo and acumulador_cantidad_jabon > acumulador_cantidad_alcohol):
    item_con_mas_unidades = tipo
    fabricante_con_mas_unidades = fabricante

#Mensaje
mensaje = "El mas caro de los barbijos tiene una cantidad de: " + str(acumulador_cantidad_barbijo) + " y es fabricado por: " + fabricante_unidad_mas_cara + ". \n" +"El item con mas unidades es: " + item_con_mas_unidades + " y es: " + fabricante_con_mas_unidades + ". \n" + "La cantidad de jabones es: " + str(acumulador_cantidad_jabon) + ". \n" + "Gracias por usar el programa."

#Mostrar
print(mensaje)