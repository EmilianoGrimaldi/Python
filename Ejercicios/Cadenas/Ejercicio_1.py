# 1. Escribir una función que reciba un string y devuelva el mismo string todo en mayúsculas.

def pasar_string_mayuscula(cadena:str)->str:
    """Pasa una cadena toda a mayuscula

    Args:
        cadena (str): El string a transformar

    Returns:
        str: Retorna el string entero en mayuscula
    """
    return cadena.upper()

print(pasar_string_mayuscula("hola mundo"))