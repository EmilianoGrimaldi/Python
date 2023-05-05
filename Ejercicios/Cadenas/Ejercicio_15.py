# 15. Escribir una función que tome una cadena de texto y devuelva solo los caracteres alfabéticos, eliminando cualquier número o símbolo (sólo son válidos letras y espacios), por ejemplo: "H0l4, m4nd0!" -> "Hl mnd”

def devolver_caracteres_alfabeticos(cadena:str)->str:
    """Elimina los numeros y simbolos de una cadena, dejando letras y espacios solamente

    Args:
        cadena (str): La cadena de texto

    Returns:
        str: La cadena solo con letras y espacios
    """
    palabra = ""
    
    for caracter in cadena:
        if (caracter >= "A" and caracter <= "Z") or (caracter >= "a" and caracter <= "z") or (caracter == " "):
            palabra += caracter
    
    return palabra

print(devolver_caracteres_alfabeticos("H0l4, m4nd0!"))