# 12. Escribir una función que tome un número de tarjeta de crédito como input, verificar que todos los caracteres sean numéricos y devolver los últimos cuatro dígitos y los primeros dígitos como asteriscos, por ejemplo: "**** **** **** 1234".

def verificar_tarjeta_credito(numero_tarjeta:int)->int:
    """Verifica que toda la cadena sea numerica y devuelve los ultimos cuatro digitos de la tarjeta y el resto con asteriscos

    Args:
        numero_tarjeta (int): Cadena numerica

    Returns:
        int: Numero de tarjeta con asteristicos y los ultimos cuatro digitos literales
    """
    ultimos_cuatro_digitos = ""
    salio_mal = False
    
    if len(numero_tarjeta) == 16:
        if numero_tarjeta.isdigit():
            for i in range(len(numero_tarjeta)):
                if i+1 > 12:
                    ultimos_cuatro_digitos += numero_tarjeta[i]
                    cadena_completa = f"**** **** **** {ultimos_cuatro_digitos}"
            return cadena_completa
        else:
            print("No son digitos numericos")
            return salio_mal
    else:
        print("Error! No tiene 16 digitos")
        return salio_mal


numero_tarjeta = "1234456789102000"

if verificar_tarjeta_credito(numero_tarjeta):
    print(verificar_tarjeta_credito(numero_tarjeta))
