def validar_mail(cadena):
    arroba = 0
    punto = 0
    for letra in cadena:
        if letra == "@":
            arroba += 1
        else:
            if letra == ".":
                punto += 1
    if arroba == 1 and punto >= 1:
        indice_arroba = cadena.index("@")
        indice_punto = cadena.index(".")
        if indice_arroba < indice_punto:
            return True
    return False

def pedir_correo(mensaje_pedir):

    while True:
        correo = input(mensaje_pedir)
        if validar_mail(correo):
            break
        else:
            print(f"Formato de correo erroneo. Usted ingreso {correo}\n")
    
    return correo

def validar_telefono(telefono):
    if len(telefono) != 12:
        return False
    for i in range(12):
        if i == 2 or i == 7:
            if telefono[i] != "-":
                return False
        else:
            if not telefono[i].isdigit():
                return False
    return True

def pedir_telefono(mensaje_pedir):

    while True:
        telefono = input(mensaje_pedir)
        if validar_telefono(telefono):
            break
        else:
            print(f"Formato de telefono erroneo. Usted ingreso {telefono}\n")
    
    return telefono

def validar_fecha(fecha):
    if len(fecha) != 10:
        return False
    for i in range(10):
        if i == 2 or i == 5:
            if fecha[i] != "/":
                return False
        else:
            if not fecha[i].isdigit():
                return False
    return True

def pedir_fecha(mensaje_pedir):
    
    while True:
        fecha = input(mensaje_pedir)
        if validar_fecha(fecha):
            break
        else:
            print(f"Formato de fecha erroneo. Usted ingreso {fecha}\n")
    
    return fecha

def es_string_espacios(cadena):
    flag = True
    for letra in cadena:
        if not letra.isalpha() and letra != " ":
            flag = False 
            break

    return flag

def pedir_cadena_alfabetica_con_espacios(mensaje_pedir):
    
    while True:
        string = input(mensaje_pedir)
        if es_string_espacios(string):
            break
        else:
            print("No es una cadena alfabetica con espacios")
    return string

def pedir_cadena(mensaje_pedir):
    
    while True:
        string = input(mensaje_pedir)
        if string.isalpha():
            break
        else:
            print("No es una cadena alfabetica")

    return string

def pedir_entero(mensaje_pedir):
    while True:
        try:
            numero = int(input(mensaje_pedir))
            break
        except ValueError:
            print("Error de tipo. Ingresaste un caracter alfabetico o string")

    return numero

def pedir_flotante(mensaje_pedir):
    while True:
        try:
            numero = float(input(mensaje_pedir))
            break
        except ValueError:
            print("Error de tipo. Ingresaste un caracter alfabetico o string")

    return numero

def pedir_entero_rango(mensaje_pedir, min, max):
    while True:
        try:
            numero = int(input(mensaje_pedir))
            if (numero > min and numero < max):   
                break
            else:
                print("Numero fuera de rango")
        except ValueError:
            print("Error de tipo. Ingresaste un caracter alfabetico o string")

    return numero