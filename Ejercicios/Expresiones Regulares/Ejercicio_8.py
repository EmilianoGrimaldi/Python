# 8. Crear una función que reciba una lista de palabras y devuelva otra lista con las palabras que comienzan con la letra ‘U’

from re import *

def filtrar_palabras_letra(lista_palabras:list)->list:
    """Filtra las palabras de una lista que comienzan con x letra

    Args:
        lista_palabras (list): Lista de palabras

    Returns:
        list: Lista que contiene todas las palabras filtradas
    """
    patron = compile("^[uU]")
    lista_palabras_filtradas = []

    for elemento in lista_palabras:
        if match(patron,elemento):
            lista_palabras_filtradas.append(elemento)
    
    return lista_palabras_filtradas

lista = ["Emiliano","Urias","Emanuel","urinario"]
print(filtrar_palabras_letra(lista))