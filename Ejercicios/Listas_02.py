#La real academia española nos pide desarrollar un pequeño programa que contenta el diccionario de la lengua española y su traducción al inglés. Para esto necesitamos un algoritmo que nos permita el ingreso de una palabra en español y su traducción al ingles y guardarlo en una lista. Si la palabra no existe, debemos agregarla, y si la palabra existe debemos informar que la palabra ya existe y su índice dentro del listado, esta carga debe ser hasta que el usuario se canse de ingresar palabras. Al finalizar se debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en inglés. Recordar validar los datos de forma correcta.
# inicializamos las listas vacías
seguir = "s"
palabras_espanol = []
palabras_ingles = []

while seguir == "s":
    # INGRESO DE DATOS Y VALIDACIONES
    while True: 
        palabra_espanol = input("Ingrese una palabra en español: ").lower()
        if palabra_espanol.isalpha():
            break
        else:
            print("ERROR! Se permiten solo palabras. Ingrese una palabra en español.")

    while True :
        palabra_ingles = input("Ingrese la traducción al inglés: ").lower()
        if palabra_ingles.isalpha():
            break
        else:
            print("ERROR! Se permiten solo palabras. Ingrese la traducción al inglés: ").lower()

    # buscamos si la palabra ya existe en la lista de palabras en español
    palabra_encontrada = False
    for i in range(len(palabras_espanol)):
        if palabras_espanol[i] == palabra_espanol:
            palabra_encontrada = True
            indice_palabra = i
            break


    # si la palabra ya existe, informamos su índice en la lista
    if palabra_encontrada == True:
        print(f"La palabra '{palabra_espanol}' ya existe en la lista, en la posición {indice_palabra}.")
    # si la palabra no existe, la agregamos a ambas listas
    else:
        palabras_espanol.append(palabra_espanol)
        palabras_ingles.append(palabra_ingles)
        print(f"La palabra '{palabra_espanol}' ha sido agregada a la lista.")

    # PREGUNTAR SI DESEA CONTINUAR
    seguir = input("Presione 's' para continuar o cualquier tecla para salir: ").lower()

# mostramos la lista de palabras ingresadas
print("Lista de palabras ingresadas:")
for i in range(len(palabras_espanol)):
    print(f"- '{palabras_espanol[i]}' en inglés es '{palabras_ingles[i]}'")
