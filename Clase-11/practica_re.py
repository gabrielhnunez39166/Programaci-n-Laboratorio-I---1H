############### EXPRESIONES REGULARES (REGEX) ###############
#Importar el modulo re
import re
from hamcrest import none

from sqlalchemy import false

def validacion_con_regex():
    texto = input('Ingrese un texto: \n > ')
    ############### RE.SPLIT() ###############
    #Primer parametro SEPARADOR y el segundo EL TEXTO A SEPARAR
    texto = re.split('[ ]', texto)

    ############### RE.FINDALL ###############
    #Sirve para extraer algo especifico
    #Primer parametro LO QUE BUSCO y el segundo EL TEXTO A BUSCAR - Ej fecha AAAA-MM-DD
    texto = re.findall('([0-9]{4})-([0-9]{2})-([0-9]{2})', texto)

    print(texto)

validacion_con_regex()