# 11. Escribir una función que tome una lista de palabras y devuelva un string que contenga todas las palabras concatenadas con comas y "y" antes de la última palabra. Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"], el string resultante debería ser "manzanas, naranjas y bananas".

lista = ["manzanas", "naranjas", "bananas", "uvas"]

def concatenar_lista(lista_palabras:list)->str:
    """Transformar una lista de palabras en una cadena con comas de por medio, y una 'y' antes de la ultima palabra

    Args:
        lista_palabras (list): Una lista de palabras

    Returns:
        str: Una cadena de palabras formateadas con comas de por medio y una 'y' antecediento la ultima palabra
    """
    if len(lista_palabras) > 0:
        ultimo_elemento = lista_palabras[-1]
        separador = ", "
        lista_aux = []

        for i in range(len(lista_palabras)-1):
           lista_aux.append(lista_palabras[i])
        
        cadena_completa = f"{separador.join(lista_aux)} y {ultimo_elemento}"        
        
        return cadena_completa
    else:
        print("Error! Lista vacia")

print(concatenar_lista(lista))