# 8. Escribir una función que reciba dos string (nombre y apellido) y devuelva un diccionario con el nombre y apellido, eliminando los espacios del comienzo y el final y colocando la primer letra en mayúscula

def convertir_nombre_apellido(nombre:str,apellido:str)->dict:
    """Elimina los espacios en blanco del comienzo y final de la cadena y coloca la primer letra en mayuscula

    Args:
        nombre (str): Cadena alfabetica representa el nombre
        apellido (str): Cadena alfabetica representa el apellido

    Returns:
        dict: Un diccionario con el nombre y el apellido
    """
    persona = {}

    persona["Nombre"] = nombre.strip().capitalize()
    persona["Apellido"] = apellido.strip().capitalize()

    return persona

aux = convertir_nombre_apellido(" emiliano "," grimaldi ")
for clave,valor in aux.items():
    print(f"{clave} : {valor}")