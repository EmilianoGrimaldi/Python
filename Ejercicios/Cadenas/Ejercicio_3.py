# 3. Escribir una función que tome dos strings y devuelva un nuevo string que contenga ambos strings concatenados, separados por un espacio.

def concatenar_string(string_a:str,string_b:str)->str:
    """Concatena dos strings con un espacio de por medio

    Args:
        string_a (str): Una cadena de caracteres
        string_b (str): Una cadena de caracteres

    Returns:
        str: Dos cadenas concatenadas con un espacio de por medio
    """
    cadena_con_espacio = string_a + " " + string_b

    return cadena_con_espacio

print(concatenar_string("Hola","mundo"))
