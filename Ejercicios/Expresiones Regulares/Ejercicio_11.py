# 11. Crear una función que reciba un texto y devuelva una la lista de palabras encuentra que comienzan con una vocal
from re import *

def filtrar_vocal(texto:str)->list:
    """Filtra en un texto las palabras que empiezan con una vocal

    Args:
        texto (str): El texto a evaluar

    Returns:
        list: Una lista con todas las palabras filtradas que comienzan con vocal
    """
    lista_palabras = split(" ",texto)
    patron_vocales = compile("^[aeiouAEIOU]")
    lista_palabras_filtradas = []

    for palabra in lista_palabras:
        if match(patron_vocales,palabra):
            lista_palabras_filtradas.append(palabra)
    
    return lista_palabras_filtradas

print(filtrar_vocal("Hola mundo elegante"))