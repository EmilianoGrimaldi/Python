def pedir_string(mensaje_pedir):
    while True:
        string = input(mensaje_pedir)
        if string.isalpha():
            break
        else:
            print(f"Se pidio un string. Usted ingreso {string}")

    return string

def pedir_string_espacio(mensaje_pedir):
    while True:
        string = input(mensaje_pedir).strip()
        if len(string) > 0:
            return string
        else:
            print("El string no puede ser vacío o contener solo espacios en blanco.")

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