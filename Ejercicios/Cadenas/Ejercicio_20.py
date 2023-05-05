# 20. Escribir una función que tome una lista de direcciones de correo electrónico y las una en una sola cadena separada por punto y coma, por ejemplo: ["juan@gmail.com", "maria@hotmail.com"] -> "juan@gmail.com;maria@hotmail.com".

lista = ["pcoll0@globo.com","nleverette1@printfriendly.com", "bvagges2@icio.us", "abirk3@google.co.uk","vpilsbury4@altervista.org", "cmcgrirl5@sourceforge.net","jreubbens6@goo.ne.jp", "ckemmis7@facebook.com","vdondon8@phoca.cz","pcopnall9@wiley.com"]

def unir_correos_una_cadena(lista_correos:list)->str:
    """Toma una lista de direcciones de correo electrónico y las une en una sola cadena separada por punto y coma

    Args:
        lista_correos (list): La lista de correos electronicos

    Returns:
        str: Cadena con todos los correos separados por punto y coma " ; "
    """
    # separador = ";"
    # cadena = separador.join(lista_correos)
    cadena_aux = ""
    ultimo_elemento = lista_correos[-1]
    for elemento in range(len(lista_correos)-1):
        cadena_aux += f"{lista_correos[elemento]};"

    cadena_completa = f"{cadena_aux}{ultimo_elemento}"

    return cadena_completa

print(unir_correos_una_cadena(lista))