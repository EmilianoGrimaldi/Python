# 12. Escribir una función que tome un número de tarjeta de crédito como input, verificar que todos los caracteres sean numéricos y devolver los últimos cuatro dígitos y los primeros dígitos como asteriscos, por ejemplo: "**** **** **** 1234".

def verificar_tarjeta_credito(numero_tarjeta:int)->int:
    """Verifica que toda la cadena sea numerica y devuelve los ultimos cuatro digitos de la tarjeta y el resto con asteriscos

    Args:
        numero_tarjeta (int): Cadena numerica

    Returns:
        int: Numero de tarjeta con asteristicos y los ultimos cuatro digitos literales
    """
    flag_bien = False
    ultimos_cuatro_digitos = ""

    if len(numero_tarjeta) == 16:
        if numero_tarjeta.isdigit():
            flag_bien =  True
        else:
            print("No son digitos numericos")
    else:
        print("Error! No tiene 16 digitos")
    
    if flag_bien:
        print(ultimos_cuatro_digitos)
        # for i in range(len(numero_tarjeta)):
        #     ultimos_cuatro_digitos += numero_tarjeta[i]

verificar_tarjeta_credito("1234456789102000")