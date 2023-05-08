# 15. Crear la función es_hora que reciba un string y que devuelva True en caso de
# tratarse de una hora válida y False en el caso contrario. El formato admitido
# es ‘hh:mm:ss’

from re import *

def es_hora(hora:str)->bool:
    """Valida que sea un formato de hora valido

    Args:
        hora (str): La hora a validar

    Returns:
        bool: True si es un formato de hora valida, en caso contrario False
    """
    
    salio_bien = False
    patron_hora = compile("^[0-2][0-3]:[0-5][0-9]:[0-5][0-9]$")
    
    if match(patron_hora,hora):
        salio_bien = True

    return salio_bien
    
print(es_hora("00:00:00"))


