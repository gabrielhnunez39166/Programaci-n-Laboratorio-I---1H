'''
Hugo Gabriel Nunez
'''

peso = 0 #Entre 10 y 100 kilos
precio_por_kilo = 0 #Mayor a cero
tipo_validad = "" #"v", "a", "m" (vegetal, animal, mezcla)

ingresar_datos = "si"

mensaje = ""

importe_bruto = 0
descuento = 0
importe_con_descuento = 0

acumulador_peso = 0

flag_alimento_mas_caro = False
tipo_alimento_mas_caro = ""
precio_alimento_mas_caro = 0

promedio_precio_por_kilo = 0
acumulador_precio_por_kilo = 0
contador_productos = 0

#
while(ingresar_datos == "si"):
    #Peso
    peso = input("Ingrese el peso del producto: ")
    peso = float(peso)
    while(peso < 10 or peso > 100):
        peso = input("Ingrese el peso del producto: ")
        peso = float(peso)

    #Precio por kilo
    precio_por_kilo = input("Ingrese el precio del producto: ")
    precio_por_kilo = float(precio_por_kilo)
    while(precio_por_kilo < 1):
        precio_por_kilo = input("Ingrese el precio del producto: ")
        precio_por_kilo = float(precio_por_kilo)

    #Tipo validad
    tipo_validad = input("Ingrese el tipo de producto (v (verdura), a (animal), m (mezcla): ")
    while(tipo_validad != "v" and tipo_validad != "a" and tipo_validad != "m"):
        tipo_validad = input("Ingrese el tipo de producto (v (verdura), a (animal), m (mezcla): ")

    #A
    importe_bruto += precio_por_kilo
    
    #B
    acumulador_peso += peso

    #C
    if (flag_alimento_mas_caro == False):
        flag_alimento_mas_caro = True
        tipo_alimento_mas_caro = tipo_validad
        precio_alimento_mas_caro = precio_por_kilo
    elif (precio_por_kilo > precio_alimento_mas_caro):
        tipo_alimento_mas_caro = tipo_validad
        precio_alimento_mas_caro = precio_por_kilo

    #D
    contador_productos += 1
    acumulador_precio_por_kilo += precio_por_kilo

    ingresar_datos = input("Ingresar otro dato? si/no => ")

#B
if (acumulador_peso > 100):
    descuento = importe_bruto * 15 / 100
    importe_con_descuento = importe_bruto - descuento
    importe_con_descuento = round(importe_con_descuento, 2)
elif (acumulador_peso > 300):
    descuento = importe_bruto * 25 / 100
    importe_con_descuento = importe_bruto - descuento
    importe_con_descuento = round(importe_con_descuento, 2)

#D
promedio_precio_por_kilo = acumulador_precio_por_kilo / contador_productos
promedio_precio_por_kilo = round(promedio_precio_por_kilo, 2)

#Mensaje
mensaje = "El importe bruto es $" + str(importe_bruto) + "\n" + "El descuento es del " + str(descuento) + "% \n" + "El importe con descuento es $" + str(importe_con_descuento) + "% \n" + "El tipo de alimento mas caro es: " + tipo_alimento_mas_caro + "\n" + "El promedio de precio por kilo es: $" + str(promedio_precio_por_kilo) + "\n"

print(mensaje)