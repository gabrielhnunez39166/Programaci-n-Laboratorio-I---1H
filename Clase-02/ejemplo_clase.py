#Listas
lista_nombres = []
lista_apellidos = []
CANTIDAD_EMPLEADOS = 2
""" for i in range(CANTIDAD_EMPLEADOS):
    nombre = input("Ingrese un nombre: \n")
    apellido = input("Ingrese un apellido: \n")
    lista_nombres.append(nombre)
    lista_apellidos.append(apellido)

i = 0
for i in range(CANTIDAD_EMPLEADOS):
    print("{0} - {1} - {2}".format(i, lista_nombres[i], lista_apellidos[i]))
    i += 1 """

#Diccionario
lista_empleados = []
for i in range(CANTIDAD_EMPLEADOS):
    dic_empleado = {}
    nombre = input("Ingrese un nombre: \n")
    apellido = input("Ingrese un apellido: \n")
    dni = input("Ingrese un DNI: \n")
    #Validar lo que se pide por input
    dic_empleado["nombre"] = nombre
    dic_empleado["apellido"] = apellido
    dic_empleado["dni"] = dni
    lista_empleados.append(dic_empleado)

for empleado in lista_empleados:
    print(empleado["nombre"])

print(lista_empleados)