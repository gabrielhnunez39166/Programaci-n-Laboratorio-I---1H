import re

############# VALIDAR #############
def validar_RegEx(a_validar: str, patron_valicion) -> bool: # -> int
    respuesta_validada = re.search(patron_valicion, a_validar, re.IGNORECASE)
    if respuesta_validada != None:
        a_validar = a_validar.lower()
        a_validar = a_validar.replace(" ","")
        return a_validar
    else: 
        return False

