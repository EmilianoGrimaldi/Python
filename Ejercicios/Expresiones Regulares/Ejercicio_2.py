# 2. Crear una función llamada es_minuscula que reciba un string y devuelva True en caso de que todas las letras sean mayúsculas o False en el caso contrario
from re import *

def es_minuscula(string:str)->bool:
    """Verifica que todas las letras del string ingresado sean minusculas solamente

    Args:
        string (str): La cadena de texto

    Returns:
        bool: True en caso de que todas las letras sean minusculas o False en caso contrario
    """
    salio_bien = True
    patron = compile("^[a-z]+$")
    resultado = match(patron,string)

    if not resultado:
        salio_bien = False
    
    return salio_bien

print(es_minuscula("hola"))
    