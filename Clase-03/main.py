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

#Superheroe mas alto
altura_maxima_superheroe = lista_personajes[0]
for superheroe in lista_personajes:
  superheroe_float = float(altura_maxima_superheroe['altura'])
  nombre_superhero = altura_maxima_superheroe['nombre']
