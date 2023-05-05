# 4. Crear una función llamada es_solo_texto que reciba un string y devuelva True en caso de que trate solo de caracteres alfabéticos y el espacio y False en el caso contrario
from re import *
def es_solo_texto(cadena:str)->bool:
    """Valida que la cadena ingresada sea solo caracteres alfabeticos con espacios

    Args:
        cadena (str): La cadena a validar

    Returns:
        bool: True si es solo texto alfabetico con espacios, False en caso contrario
    """
    salio_bien = True
    patron = compile("^[A-Z a-z]+$")

    if not match(patron,cadena):
        salio_bien = False
    
    return salio_bien

print(es_solo_texto("Hola mundo"))