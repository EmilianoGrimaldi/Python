# 11. Crear una función que reciba un texto y devuelva una la lista de palabras encuentra que comienzan con una vocal
from re import *

def filtrar_vocal(texto:str)->list:
    """Filtra en un texto las palabras que empiezan con una vocal

    Args:
        texto (str): El texto a evaluar

    Returns:
        list: Una lista con todas las palabras filtradas que comienzan con vocal
    """
    
    patron_vocales = compile("\\b[aeiouAEIOU][A-Za-z]+\\b")
    lista_palabras = findall(patron_vocales,texto)
    return lista_palabras

print(filtrar_vocal("Hola mundo elegante"))