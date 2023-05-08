# 19. Crear una función llamada validar_password que reciba un string y verifique si
# se trata de una contraseña cumple con los requisitos mínimos de seguridad:
# ○ Al menos 8 caracteres
# ○ Al menos una letra mayúscula y una letra minúscula
# ○ Un número
# ○ Un carácter especial
# En caso de no cumplir con alguno de los requisitos, imprimir un mensaje
# informando cual no se cumplio

from re import *

def validar_password(password:str)->str:
    """Validar si es una contraseña valida informando si se cumplen o no los requisitos de seguridad

    Args:
        password (str): La contraseña a evaluar

    Returns:
        str: Si se cumplio o no con los requisitos minimos de seguridad
    """
    
     # La contraseña debe tener al menos 8 caracteres
    if len(password) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return False

    # La contraseña debe tener al menos una letra mayúscula y una letra minúscula
    patron_mayuscula = compile('[A-Z]')
    patron_minuscula = compile('[a-z]')
    if not (search(patron_mayuscula, password) and search(patron_minuscula, password)):
        print("La contraseña debe tener al menos una letra mayúscula y una letra minúscula.")
        return False

    # La contraseña debe tener al menos un número
    patron_numero = compile('\d')
    if not search(patron_numero, password):
        print("La contraseña debe tener al menos un número.")
        return False

    # La contraseña debe tener al menos un carácter especial
    patron_caracter_especial = compile('\W')
    if not search(patron_caracter_especial, password):
        print("La contraseña debe tener al menos un carácter especial.")
        return False

    # Si se cumplen todas las condiciones, la contraseña es válida
    return True
        
contraseña = ""
validar_password(contraseña)