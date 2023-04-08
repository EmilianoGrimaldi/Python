#La real academia española nos pide desarrollar un pequeño programa que contenta el diccionario de la lengua española y su traducción al inglés. Para esto necesitamos un algoritmo que nos permita el ingreso de una palabra en español y su traducción al ingles y guardarlo en una lista. Si la palabra no existe, debemos agregarla, y si la palabra existe debemos informar que la palabra ya existe y su índice dentro del listado, esta carga debe ser hasta que el usuario se canse de ingresar palabras. Al finalizar se debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en inglés. Recordar validar los datos de forma correcta.
seguir = "s"
lista_palabras = []
while seguir == "s":
    while True:
        palabra_espanol = input("Ingrese una palabra en español: ")
        if palabra_espanol.isalpha() :
            break
        else:
            print("ERROR! Se permiten solo palabras")

    while True:
        palabra_ingles = input("Ingrese la traduccion al ingles: ")
        if palabra_ingles.isalpha() :
            break
        else:
            print("ERROR! Se permiten solo palabras")
    
    while True:
        seguir = input("'s' para continuar y 'n' para salir\n")
        if(seguir == "s" or seguir == "n"):
            break
        else:
            print("ERROR! Opcion incorrecta.")

# for palabras in lista_palabras:
#     print(f"Palabra Español: {lista_palabras[0][palabras]} Palabra Ingles: {lista_palabras[1][palabras]}")