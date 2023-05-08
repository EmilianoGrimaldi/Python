# 16. Crear la función validar_codigo_postal que reciba un string como parámetro y
# devuelva True en caso de tratarse de código postal válido o False en caso
# contrario.

from re import *

def validar_codigo_postal(codigo_postal:str)->bool:
    """Valida si un codigo postal es valido

    Args:
        codigo_postal (str): El codigo postal a validar

    Returns:
        bool: True si es un codigo postal valido, de lo contrario False
    """
    
    patron = compile("^[A-Z][0-9]{4}[A-Z]{3}$")
    if match(patron,codigo_postal.upper()):   
        return True
    
    return False

print(validar_codigo_postal("b1636fda"))