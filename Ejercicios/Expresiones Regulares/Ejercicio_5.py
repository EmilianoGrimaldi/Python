# 5. Crear una función llamada es_decimal que reciba dos strings: el primero representa la expresión a evaluar y el segundo el separador decimal (puede ser punto . o coma ,). Debe devolver True en caso que se trate de un número decimal y False en el caso contrario.

from re import *

def es_decimal(expresion:str,separador_decimal:str)->bool:
    """
        Valida que la expresion ingresada sea un decimal
    Args:
        expresion (str): Expresion a validar\n
        separador_decimal (str): Separador decimal " . " o " , "

    Returns:
        bool: True en caso de ser decimal y False en caso contrario
    """
    salio_bien = False
    tiene_separador = False
    
    separadores_decimales = compile("[,.]")

    if match(separadores_decimales,separador_decimal):
        patron_es_decimal = compile(f"^[-0-90-9]+[" + separador_decimal + "][0-9]+$")
        tiene_separador = True
        if match(patron_es_decimal, expresion) and tiene_separador:
            salio_bien = True
    
    return salio_bien

    
print(es_decimal("33.14","."))