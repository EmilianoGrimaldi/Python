import re

"""
- preguntar si un texto coincide con un patron
"""

""" 
COINCIDENCIAS BASICAS
. -> Cualquier caracter, excepto nueva linea
\d -> Cualquier digito
\D -> No es un digito
\w -> Caracter palabra (a-z, A-Z, 0-9, _)
\W -> No es caracter palabra
\s -> Espacios de cualquier tipo (espacio, tab, nueva linea)
\S -> No es espacio, Tab o nueva linea

LIMITES
\b limite de palabra

"""

# patron_patente_vieja = re.compile("[A-Z]{3} [0-9]{3}")
# match = patron_patente_vieja.match("ABC 123") #buscar si en el texto hay alguna coincidencia de ese patron
# if match:
#     print("patente valida: ",match.group())
# else:
#     print("No hubo coincidencias")
    
# frase = "Esto es un 102 texto de prueba para. 7practicar expresiones. 94 regulares en textos y no hay pretexto"

# patron = re.compile("\d")
# lista = patron.findall(frase)
# print(lista)

patron_entero = re.compile("[0-9]+")
patron_flotante = re.compile("[0-9]+.[0-9]+")
match = patron_flotante.match("12.12") #buscar si en el texto hay alguna coincidencia de ese patron
if match:
    print("flotante valido: ",match.group())
else:
    print("No hubo coincidencias")