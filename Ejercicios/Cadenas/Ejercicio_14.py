# 14. Escribir una función que tome una URL y devuelva solo el nombre de dominio, por ejemplo: "https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..
def obtener_dominio(url:str)->str:
    """Obtiene el dominio de una url

    Args:
        url (str): La url a obtener el dom

    Returns:
        str: El dominio de la url
    """
    
    dominio = ""

    for i in range(len(url)):
        if url[i] == "." and url[i-1] == "w":
            posicion_primer_punto = i
        
        if url[i] == "." and url[i+1] == "c":
            posicion_segundo_punto = i
    
    for i in range(len(url)):
        if i > posicion_primer_punto and i < posicion_segundo_punto:
            dominio += url[i] 
    
    return dominio
    
print(obtener_dominio("https://www.google.com.ar/"))