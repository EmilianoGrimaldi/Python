# 13. Crear una función que reciba un texto como parámetro y que corrija los errores de ortografía que no cumplan con la regla ortográfica que indica que antes de V se escribe N y que antes de B se escribe M. Por ejemplo, si el texto es: "Mi comvicción me hace sentir que es el momento de imvertir tiempo para finalmente enbarcar en esta nueva aventura." La función debería devolver: “Mi convicción me hace sentir que es el momento de invertir tiempo para finalmente embarcar en esta nueva aventura."

from re import *

def corregir_errores_ortograficos(cadena:str)->str:
    """Corrije los errores que no cumplan con las reglas ortograficas

    Args:
        cadena (str): La cadena a corregir

    Returns:
        str: La cadena ya correjida 
    """

    patron_mv = compile("mv")
    patron_nb = compile("nb")
    patron_corregido_parte_1 = sub(patron_mv,"nv",cadena)
    patron_corregido_completo = sub(patron_nb,"mb",patron_corregido_parte_1)
    
    return patron_corregido_completo

texto = "Mi comvicción me hace sentir que es el momento de imvertir tiempo para finalmente enbarcar en esta nueva aventura."

print(corregir_errores_ortograficos(texto))