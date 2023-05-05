# 16. Escribir una función que tome una cadena de texto y la convierta en un acrónimo, tomando la primera letra de cada palabra, por ejemplo: "Universidad Tecnológica Nacional Facultad Regional Avellaneda" -> "UTNFRA”.

def obtener_acronimo(cadena:str)->str:
    """Toma una cadena de texto y la convierte en un acrónimo

    Args:
        cadena (str): La cadena a convertir

    Returns:
        str: Acronimo en una cadena de texto
    """
    acronimo = ""
    
    for caracter in cadena:
        if caracter >= "A" and caracter <= "Z":
            acronimo += caracter
    
    return acronimo

print(obtener_acronimo("Universidad Tecnológica Nacional Facultad Regional Avellaneda"))