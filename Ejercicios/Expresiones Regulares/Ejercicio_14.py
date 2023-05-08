# 14. Crear la función es_fecha que reciba dos string, el primero representa la
# expresión a evaluar y el segundo el separador de la fecha (puede ser la barra /
# o el guión -) y que devuelva True en caso de tratarse de una fecha válida y
# False en el caso contrario. Los formatos admitidos son: ‘dd/mm/aaaa’ o
# ‘dd-mm-aaaa’

from re import *

def es_fecha(fecha:str,separador_fecha:str)->bool:
    """Valida si es una fecha o no

    Args:
        fecha (str): La fecha a validar\n
        separador_fecha (str): El separador de la fecha a validar "/" o "-"

    Returns:
        bool: True si es una fecha valida, False en caso contrario
    """
    
    if not (separador_fecha == "/" or separador_fecha == "-"):
        print("No es un separador valido")
        return False
    else:
        patron_fecha = compile("^([1-3][0-1]|0[1-9]|[1-9])"+ separador_fecha +"(0[1-9]|1[0-2]|[1-9])"+ separador_fecha +"[0-9]{4}$")
        if match(patron_fecha,fecha):
            return True
        else:
            return False

print(es_fecha("08/05/2023","/"))