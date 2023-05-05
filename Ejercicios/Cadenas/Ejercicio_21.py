# 21. Crear una función que reciba como parámetro un string y devuelva un diccionario donde cada clave es una palabra y cada valor es un entero que indica cuántas veces aparece esa palabra dentro del string.

# En este ejercicio se te pide que crees una función que tome un string como entrada y devuelva un diccionario que contenga las palabras del string como claves y el número de veces que aparece cada palabra como valores.

def contar_palabras(cadena:str)->dict:
    """Guardar palabras como clave en un diccionario y la cantidad de veces que aparece como valor

    Args:
        cadena (str): Cadena alfabetica

    Returns:
        dict: Diccionario donde cada clave es una palabra y el valor es la cantidad de veces que aparece la palabra
    """
    lista_palabras = cadena.lower().split()
    palabra_cantidad = {}
    for palabra in lista_palabras:
        if palabra not in palabra_cantidad:
            palabra_cantidad[palabra] = 1
        else:
            palabra_cantidad[palabra] += 1
    
    return palabra_cantidad

frase = input("Ingrese una frase\n")
dic_palabras_cantidad = contar_palabras(frase)
for clave,valor in dic_palabras_cantidad.items():
    print(f"{clave} -> {valor}")

