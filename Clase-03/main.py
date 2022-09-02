from data_stark import lista_personajes

lista_heroes = [
 {
   "nombre": "Howard the Duck",
   "identidad": "Howard (Last name unrevealed)",
   "empresa": "Marvel Comics",
   "altura": "79.349999999999994",
   "peso": "18.449999999999999",
   "genero": "M",
   "color_ojos": "Brown",
   "color_pelo": "Yellow",
   "fuerza": "2",
   "inteligencia": "average"
 },
 {
   "nombre": "Rocket Raccoon",
   "identidad": "Rocket Raccoon",
   "empresa": "Marvel Comics",
   "altura": "122.77",
   "peso": "25.73",
   "genero": "M",
   "color_ojos": "Brown",
   "color_pelo": "Brown",
   "fuerza": "5",
   "inteligencia": "average"
 }
]

def calcular_superheroe_mas_alto():

  #--------------Superheroe mas alto---------------------
  superheroe_mas_alto = lista_personajes[0]

  for superheroe in lista_personajes:
    if( float(superheroe["altura"]) > float(superheroe_mas_alto["altura"])):
      superheroe_mas_alto = superheroe
      nombre_superheroe_mas_alto = superheroe["nombre"]

  print(superheroe_mas_alto)

def calcular_superheroe_mas_bajo():
  #--------------Superheroe mas alto---------------------
  superheroe_mas_bajo = lista_personajes[0]

  for superheroe in lista_personajes:
    if(float(superheroe["altura"]) < float(superheroe["altura"])):
      superheroe_mas_bajo = superheroe
      nombre_superheroe_mas_bajo = superheroe["nombre"]

  print(superheroe_mas_bajo)

def calcular_promedio_de_altura():
  #--------------Promedio de la Altura---------------------
  superheroe_mas_bajo = lista_personajes[0]
  acumulador_altura = 0
  contador_heroes = 0 
  for superheroe in lista_personajes:
    contador_heroes = len(lista_personajes)
    acumulador_altura += float(superheroe["altura"])
  promedio_altura_heroes = acumulador_altura / contador_heroes

  print("{0} / {1} = {2}".format(acumulador_altura, contador_heroes, promedio_altura_heroes))


def mostrar_nombre_superheroe():
  #--------------Promedio de la Altura---------------------
  print("Superheroe mas bajo: {0} /n - Superheroe mas alto: {1}".format(nombre_superheroe_mas_bajo, nombre_superheroe_mas_alto))

def ejecutar_cinco():
  print("5")

def ejecutar_seis():
  print("6")

def ejecutar_siete():
  print("7")



while (True):
    #--------------Menu---------------------
  respuesta = input("/n >")
  if(respuesta == "1"):
    calcular_superheroe_mas_alto()
  if(respuesta == "2"):
    calcular_superheroe_mas_bajo()
  if(respuesta == "3"):
    calcular_promedio_de_altura()
  if(respuesta == "4"):
    mostrar_nombre_superheroe()
  if(respuesta == "5"):
    ejecutar_cinco()
  if(respuesta == "6"):
    ejecutar_seis()
  if(respuesta == "7"):
    ejecutar_siete()
    break

