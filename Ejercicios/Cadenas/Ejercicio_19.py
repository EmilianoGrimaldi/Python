# 19. Escribir una función que tome una cadena de caracteres y cuente la cantidad de dígitos que contiene, por ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.

def contar_digitos(cadena:str)->int:
    """Toma una cadena de caracteres y cuenta la cantidad de dígitos que contiene

    Args:
        cadena (str): La cadena a evaluar

    Returns:
        int: La cantidad de digitos que contiene
    """
    
    cantidad_digitos = 0
    
    for caracter in cadena:
        if caracter.isdigit():
            cantidad_digitos += 1
    
    return cantidad_digitos

cantidad_digitos = contar_digitos('1234 Hola Mundo')
print(f"Contiene {cantidad_digitos} digitos")