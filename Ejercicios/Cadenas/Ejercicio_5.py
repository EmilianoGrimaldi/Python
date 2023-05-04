# 5. Escribir una función que tome un string y un carácter y devuelva el número de veces que aparece ese carácter en el string.

def contar_ocurrencias_string(cadena:str,caracter:str)->int:
    """Cuenta la cantidad de veces que se repite un caracter

    Args:
        cadena (str): Una cadena de caracteres
        caracter (str): El caracter en especifico

    Returns:
        int: La cantidad de veces que aparece ese caracter
    """
    return cadena.count(caracter)

print(contar_ocurrencias_string("Hola mundo","o"))