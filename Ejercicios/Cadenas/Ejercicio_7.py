# 7. Escribir una función que tome un string y devuelva el mismo string con los espacios eliminados

def eliminar_espacios(cadena:str)->str:
    """Elimina los espacios en blanco de una cadena

    Args:
        cadena (str): Cadena alfabetica

    Returns:
        str: Cadena con los espacios eliminados
    """
    
    return cadena.replace(" ","")


def eliminar_espacios_v2(cadena):
    resultado = ""
    for caracter in cadena:
        if caracter != " ":
            resultado += caracter
    return resultado

print(eliminar_espacios("Hola mundo cruel 2023"))
print(eliminar_espacios_v2("Hola mundo cruel 2024"))