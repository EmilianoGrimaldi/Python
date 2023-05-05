# 13. Escribir una función que tome un correo electrónico y elimine cualquier carácter después del símbolo @, por ejemplo: "usuario@gmail.com" ->"usuario".

def obtener_usuario(correo:str)->str:
    """Obtiene el nombre de usuario de un correo

    Args:
        correo (str): El correo electronico

    Returns:
        str: El usuario del correo
    """
    
    usuario = ""
    
    for i in range(len(correo)):
        if correo[i] == "@":
            posicion_arroba = i
            
    for i in range(len(correo)):
        if i < posicion_arroba:
            usuario += correo[i]
    
    return usuario

print(obtener_usuario("emi.grima@gmail.com"))
            