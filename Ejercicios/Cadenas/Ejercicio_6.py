# 6. Escribir una función que tome un string y un carácter y devuelva una lista con todas las palabras en el string que contienen ese carácter.

def listar_palabras_caracter(cadena:str,caracter:str)->list:
    """Listar todas las palabras que contengan el mismo caracter

    Args:
        cadena (str): Cadena de caracteres
        caracter (str): Caracter en especifico

    Returns:
        list: Lista de palabras
    """
    palabras = cadena.split()
    palabras_contiene_caracter = []

    for palabra in palabras:
        if caracter in palabra:
            palabras_contiene_caracter.append(palabra)
        
    return palabras_contiene_caracter

print(listar_palabras_caracter("Hola mundo","a"))