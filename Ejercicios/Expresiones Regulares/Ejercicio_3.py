from re import *

#3. Crear una función llamada es_entero que reciba un string y devuelva True en caso de que se trate de un número entero y False en caso contrario.

def es_entero(string:str)->bool:
    """Valida que la cadena ingresada sea entero

    Args:
        string (str): La cadena a validar

    Returns:
        bool: Si es entero True, de lo contrario False
    """
    salio_bien = True
    patron = compile("^[0-9]+$")

    if not match(patron,string):
        salio_bien = False
    
    return salio_bien

print(es_entero("1234"))