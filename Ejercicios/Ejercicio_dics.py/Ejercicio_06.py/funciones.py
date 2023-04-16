def pedir_string(mensaje_pedir):
    while True:
        string = input(mensaje_pedir)
        if string.isalpha():
            break
        else:
            print(f"Se pidio un string. Usted ingreso {string}")

    return string

def pedir_entero(mensaje_pedir):
    while True:
        try:
            numero = int(input(mensaje_pedir))
            break
        except ValueError:
            print("Error de tipo. Ingresaste un caracter alfabetico o string")

    return numero