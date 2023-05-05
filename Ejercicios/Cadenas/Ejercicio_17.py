# 17. Escribir una función que tome un número binario y lo convierta en una cadena de 8 bits, rellenando con ceros a la izquierda si es necesario, por ejemplo: "101" -> "00000101".

def obtener_binario_8_bits(numero_bin:str)->str:
    """Toma un número binario y lo convierte en una cadena de 8 bits, rellenando con ceros a la izquierda si es necesario

    Args:
        numero_bin (str): Cadena numerica binaria

    Returns:
        str: La cadena binaria con 8 bits
    """
    
    cadena_binaria = ""
    bits = 8
    es_binario = True
    
    for digito in numero_bin:
        if (not digito == "0") and (not digito == "1"):
            es_binario = False
            break
    
    if es_binario:
        if len(numero_bin) <= 8:
            cadena_binaria = numero_bin.zfill(bits)
        else:
            print("Error! Tiene mas de 8 digitos")
    else:
        print("Error! No es numero binario")
    
    return cadena_binaria

print(obtener_binario_8_bits("101"))