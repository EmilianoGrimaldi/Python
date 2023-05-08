# 17. Crear la función validar_patente que reciba un string como parámetro y
# devuelva True en caso de tratarse de un número de patente válido o False en
# caso contrario. Debe poder admitir estos dos tipos:

from re import *

def validar_patente(patente:str)->bool:
    """Valida si el formato de la patente es correcto

    Args:
        patente (str): La patente a validar

    Returns:
        bool: True en caso de ser correcta la patente, False en caso contrario
    """
    
    patron_patente_valida = compile("^([A-Z]{2} [0-9]{3} [A-Z]{2})|([A-Z]{3} [0-9]{3})$")
    
    if match(patron_patente_valida,patente):
        return True
    
    return False

patente = "AB 123 CD"

print(validar_patente(patente))