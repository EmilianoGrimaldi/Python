# 20. Crear una función llamada validar_ip que reciba un string como parámetro y
# verifique si se trata de una dirección IP v4 válida, en caso de serlo retornar
# True de lo contrario retornar False.
# Se considera una dirección IP válida si tiene el formato xxx.xxx.xxx.xxx, donde
# xxx es un número entero entre 0 y 255.

from re import *

def validar_ip(ip:str)->bool:
    """Verifica si se trata de una dirección IP v4 válida

    Args:
        ip (str): La ip a validar

    Returns:
        bool: True en caso de ser ip valida, de lo contrario False.
    """
    patron_ip = compile("^(2[0-5]{2}|1[0-9]{2}|[1-9][0-9]|[0-9])\.(2[0-5]{2}|1[0-9]{2}|[1-9][0-9]|[0-9])\.(2[0-5]{2}|1[0-9]{2}|[1-9][0-9]|[0-9])\.(2[0-5]{2}|1[0-9]{2}|[1-9][0-9]|[0-9])$")
    salio_bien = False
    
    if match(patron_ip,ip):
        salio_bien = True
    
    return salio_bien
        
ip = "255.255.255.255"
print(validar_ip(ip))