# 10. Escribir una función que tome un nombre y un apellido y devuelva un email en formato "inicial_nombre.apellido@utn-fra.com.ar".

def transformar_a_email(nombre:str,apellido:str)->str:
    """Genera un email a partir de un nombre y apellido

    Args:
        nombre (str): cadena alfabetica que representa el nombre\n
        apellido (str): cadena alfabetica que representa el apellido

    Returns:
        str: El email formateado
    """
    inicial = nombre[0].lower()
    email = f"{inicial}_{nombre.lower()}.{apellido.lower()}@utn-fra.com.ar"
    return email

print(transformar_a_email("Juan","Gonzales"))