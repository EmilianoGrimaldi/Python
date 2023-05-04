# 4. Escribir una función que tome un string y devuelva el número de caracteres que tiene el string.
def contar_caracteres(cadena:str)->int:
    """Cuenta los caracteres de una cadena

    Args:
        cadena (str): Cadena de caracteres

    Returns:
        int: Cantidad de caracteres
    """
    return len(cadena) ## cuenta los espacios en blanco tambien

print(contar_caracteres("Hola mundo"))