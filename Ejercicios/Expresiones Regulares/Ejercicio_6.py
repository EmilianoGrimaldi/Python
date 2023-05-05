# 6. Crear una función llamada es_alfanumerico que devuelva True en caso de tratarse de solo letras y números y False en el caso contrario (es decir que contenga caracteres especiales)
from re import *

def es_alfanumerico(cadena:str)->bool:
    """Valida que la cadena ingresada sea alfanumerica (solo letras y numeros)

    Args:
        cadena (str): Cadena a validar

    Returns:
        bool: True en caso de ser alfanumerica, False en caso contrario
    """
    salio_bien = False
    patron_alfanumerico = compile("^[0-9A-Za-z]+$")

    if match(patron_alfanumerico,cadena):
        salio_bien = True

    return salio_bien

print(es_alfanumerico("EstoEsUnaCadenaAlfanumerica2023"))