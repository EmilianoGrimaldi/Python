# 9. Escribir una función que tome una lista de nombres y los una en una sola cadena separada por un salto de línea, por ejemplo: ["Juan", "María", "Pedro"] -> "Juan\nMaría\nPedro".

lista = ["Juan", "María", "Pedro"]

def unir_cadena(lista_nombres:list)->str:
    """Une una lista de nombres en una sola cadena separadas por un salto de linea

    Args:
        lista_nombres (list): Una lista de nombres
    Returns:
        str: Los nombres unidos en una sola cadena
    """

    separador = "\n"
    cadena = separador.join(lista_nombres)

    return cadena

print(unir_cadena(lista))