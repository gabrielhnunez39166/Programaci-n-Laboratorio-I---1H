"""
Hugo Gabriel Nunez
"""
#
nombre_heroe_ina = ""
edad = 0
sexo = ""
habilidad =""

flag_heroe_fuerza_joven = False
heroe_fuerza_mas_joven = ""
edad_heroe_joven = 0

flag_heroe_mayor_edad = False
sexo_heroe_mayor_edad = ""
nombre_heroe_mayor_edad = ""
edad_heroe_mayor = 0

contador_heroina_Fuer_Mag = 0

contador_heroinas = 0
acumulador_edad_heroinas = 0
promedio_edad_heroinas = 0

contador_heroes = 0
acumulador_edad_heroes = 0
promedio_edad_heroes_fuerza = 0


ingresar_datos = "si"
mensaje = ""

#
while(ingresar_datos == "si"):
    #Nombre del Heroe / Heroina
    nombre_heroe_ina = input("Ingrese el nombre del Heroe o la Heroina: \n")
    while(nombre_heroe_ina == ""):
        nombre_heroe_ina = input("Ingrese el nombre del Heroe o la Heroina: \n")
    
    #Edad
    edad = input("Ingrese la edad: \n")
    edad = int(edad)
    while(edad < 18):
        edad = input("Ingrese la edad: \n")
        edad = int(edad)
    
    #Sexo
    sexo = input("Ingrese el sexo: \n")
    while(sexo != "m" and sexo != "f" and sexo != "nb"):
        sexo = input("Ingrese el sexo: \n")
    
    #Habilidad
    habilidad = input("Ingrese la habilidad: \n")
    while(habilidad != "fuerza" and habilidad != "magia" and habilidad != "inteligencia"):
        habilidad = input("Ingrese la habilidad: \n")

    #A
    if (flag_heroe_fuerza_joven == False and habilidad == "fuerza"):
        flag_heroe_fuerza_joven
        heroe_fuerza_mas_joven = nombre_heroe_ina
        edad_heroe_joven = edad
    else:
        if(habilidad == "fuerza" and edad < edad_heroe_joven):
            heroe_fuerza_mas_joven = nombre_heroe_ina
            edad_heroe_joven = edad


    #B
    if (flag_heroe_mayor_edad == False):
        flag_heroe_mayor_edad = True
        sexo_heroe_mayor_edad = sexo
        nombre_heroe_mayor_edad = nombre_heroe_ina
        edad_heroe_mayor = edad
    else:
        if (edad > edad_heroe_mayor):
            sexo_heroe_mayor_edad = sexo
            nombre_heroe_mayor_edad = nombre_heroe_ina
            edad_heroe_mayor = edad

    if (sexo == "f"): #C y D
        contador_heroinas += 1
        acumulador_edad_heroinas += edad

        if(habilidad == "fuerza" or habilidad == "magia"):
            contador_heroina_Fuer_Mag += 1

    elif (sexo == "m"): #E
        contador_heroes += 1
        acumulador_edad_heroes += edad
    
    ingresar_datos = input("Ingresar datos? si/no \n")

#D
promedio_edad_heroinas = acumulador_edad_heroinas / contador_heroinas
promedio_edad_heroinas = round(promedio_edad_heroinas, 2)

#E
promedio_edad_heroes_fuerza = acumulador_edad_heroes / contador_heroes
promedio_edad_heroes_fuerza = round(promedio_edad_heroes_fuerza, 2)

#Mensaje
mensaje = "El nombre del Heroe / Heroina de Fuerza mas joven es: " + heroe_fuerza_mas_joven + " con " + str(edad_heroe_joven) + ". \n" + "El sexo y nombre del Heroe / Heroina de mayor edad es: " + sexo_heroe_mayor_edad + " " + nombre_heroe_mayor_edad + " con " + str(edad_heroe_mayor) + ". \n" + "La cantidad de Heroinas que tienen habilidades de Fuerza o Magia es: " + str(contador_heroina_Fuer_Mag) + ". \n" + "El promedio de edad entre Heroinas es: " + str(promedio_edad_heroinas) + " años. \n" + "El promedio de edad entre Heroes de Fuerza es: " + str(promedio_edad_heroes_fuerza) + " años. \n"

#Mostrar
print(mensaje)