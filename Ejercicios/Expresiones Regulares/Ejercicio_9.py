# 9. Crear una función que reciba un texto y devuelva una lista con las palabras que contienen entre 3 y 6 caracteres de largo

from re import *

def palabras_filtradas_largo(cadena:str)->list:
    """Filtra las palabras por largo entre 3 y 6

    Args:
        cadena (str): Cadena a evaluar

    Returns:
        list: Lista filtrada con las palabras
    """

    cadenas = split(" ",cadena)
    patron = compile(f"^[A-Za-z]+$")
    lista_filtrada_largo = []
    
    for cadena in cadenas:
        if match(patron,cadena) and len(cadena) >= 3 and len(cadena) <= 6 :
            lista_filtrada_largo.append(cadena)
    
    return lista_filtrada_largo
            
    

print(palabras_filtradas_largo("Hola mundo"))