# 8-
# Escribir un programa que le pida al usuario ingresar una lista de nombres de personas (previamente validada) y luego le pidan 1 solo nombre en específico. Se debe buscar el nombre especifico en la lista de nombres y si esta presente el programa deberá imprimir la posición del nombre en la lista, la posición de memoria donde se encuentra ese nombre y la cantidad de caracteres que tiene el nombre, si no se encuentra, se deberá informar por pantalla.

#PASO 1 pedir al usuario que ingrese una lista de nombres de personas (previamente validada)
#PASO 2 luego le pidan 1 solo nombre en específico.
#PASO 3 buscar el nombre especifico en la lista de nombres
#PASO 4 si esta presente el programa deberá imprimir la posición del nombre en la lista si no se encuentra, se deberá informar por pantalla.
#PASO 5 la posición de memoria donde se encuentra ese nombre
#PASO 6 la cantidad de caracteres que tiene el nombre
# lista_nombres = [Emiliano Federico Julieta Noelia Gisel Teresa Omar Carlos Rodrigo]
flag_posicion = False
flag_nombre_valido = False

while True:

    while True:
        lista_nombres = input("Ingrese una lista de nombres separados por espacios\n").split()
        for nombre in lista_nombres:
            for caracter in nombre:
                pass

    nombre_ingresado = input("Ingrese un nombre a buscar\n")
    for nombre in lista_nombres:
        if nombre == nombre_ingresado:
            posicion = lista_nombres.index(nombre)
            id_nombre = id(nombre)
            tam_nombre = len(nombre)
            flag_posicion = True

    if flag_posicion:
        print(f"La posicion del nombre en la lista es {posicion}")
        print(f"El nombre se encuentra en la posicion de memoria {id_nombre}")
        print(f"El tamaño del nombre es {tam_nombre}")
    else:
        print("No se encuentra ese nombre en la lista")

    seguir = input("Desea[seguir? [s/n]\n")
    if seguir != "s":
        seguir = input("Esta seguro que quiere salir? [s/n]\n")
        if seguir != "s":
            break

