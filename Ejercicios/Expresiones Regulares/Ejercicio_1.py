# 1. Crear una función llamada es_mayuscula que reciba un string y devuelva True en caso de que todas las letras sean mayúsculas o False en el caso contrario

from re import *

def es_mayuscula(string:str)->bool:
    """Verifica que todas las letras del string ingresado sean mayusculas solamente

    Args:
        string (str): La cadena de texto

    Returns:
        bool: True en caso de que todas las letras sean mayusculas o False en caso contrario
    """
    salio_bien = True

    patron = compile("^[A-Z]+$")
    resultado = match(patron,string)
    if not resultado:
        salio_bien = False
    
    return salio_bien


resultado = es_mayuscula("HOLA")
print(resultado)

