# 2. Escribir una función que reciba un string y devuelva el mismo string todo en minúsculas
def pasar_string_minuscula(cadena:str)->str:
    """Pasa una cadena toda a minuscula

    Args:
        cadena (str): El string a transformar

    Returns:
        str: Retorna el string entero en minuscula
    """
    return cadena.lower()

print(pasar_string_minuscula("HOLA MUNDO"))