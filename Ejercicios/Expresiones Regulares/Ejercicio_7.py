# 7. Crear una función llamada es_binario que devuelva True en caso de un número binario válido (solo ceros y unos) o False en el caso contrario

from re import *

def es_binario(cadena:str)->bool:
    """Valida que la cadena ingresada sea un numero binario

    Args:
        cadena (str): La cadena a validar

    Returns:
        bool: True en caso de ser binario, False en caso contrario
    """

    salio_bien = False
    patron_binario = compile("^[01]+$")

    if match(patron_binario,cadena):
        salio_bien = True

    return salio_bien

print(es_binario("011010101"))