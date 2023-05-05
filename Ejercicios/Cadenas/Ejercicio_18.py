# 18. Escribir una función que tome una cadena de caracteres y reemplace todas las letras mayúsculas por letras minúsculas y todas las letras minúsculas por letras mayúsculas, por ejemplo: "HoLa" -> "hOlA"

def intercambiar_minuscula_mayuscula(cadena:str)->str:
    """Toma una cadena de caracteres y reemplaza todas las letras mayúsculas por letras minúsculas y todas las letras minúsculas por letras mayúsculas

    Args:
        cadena (str): La cadena a evaluar

    Returns:
        str: Cadena con los intercambios minuscula a mayuscula o viceversa
    """
    
    cadena_modificada = ""
    
    for caracter in cadena:
        if caracter.isupper():
            cadena_modificada += caracter.lower()
        else:
            if caracter.islower():
                cadena_modificada += caracter.upper()
    
    return cadena_modificada

print(intercambiar_minuscula_mayuscula("HoLa"))