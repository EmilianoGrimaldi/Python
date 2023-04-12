# 8-
# Escribir un programa que le pida al usuario ingresar una lista de nombres de personas (previamente validada) y luego le pidan 1 solo nombre en específico. Se debe buscar el nombre especifico en la lista de nombres y si esta presente el programa deberá imprimir la posición del nombre en la lista, la posición de memoria donde se encuentra ese nombre y la cantidad de caracteres que tiene el nombre, si no se encuentra, se deberá informar por pantalla.

#PASO 1 pedir al usuario que ingrese una lista de nombres de personas (previamente validada)
#PASO 2 luego le pidan 1 solo nombre en específico.
#PASO 3 buscar el nombre especifico en la lista de nombres
#PASO 4 si esta presente el programa deberá imprimir la posición del nombre en la lista si no se encuentra, se deberá informar por pantalla.
#PASO 5 la posición de memoria donde se encuentra ese nombre
#PASO 6 la cantidad de caracteres que tiene el nombre

flag_posicion = False
lista_nombres = []

while True:
    
    while True:
        while True:
            nombre = input("Ingrese un nombre\n")
            if nombre.isalpha():
                break
            else:
                print(f"Error! Usted ingreso {nombre}. Se pidio un nombre")
        
        lista_nombres.append(nombre)

        seguir_ingresando = input("Desea seguir cargando mas nombres? [s/n]\n").lower()
        if seguir_ingresando != "s":
            seguir_ingresando = input("Esta seguro que quiere dejar de cargar nombres? [s/n]\n").lower()
            if seguir_ingresando != "s":
                break

    while True:
        nombre_ingresado = input("Ingrese un nombre a buscar\n")
    
        for nombre in lista_nombres:
            if nombre == nombre_ingresado:
                posicion = lista_nombres.index(nombre)
                id_nombre = id(nombre)
                tam_nombre = len(nombre)
                flag_posicion = True
                break

        if flag_posicion:
            print(f"La posicion del nombre en la lista es {posicion}")
            print(f"El nombre se encuentra en la posicion de memoria {id_nombre}")
            print(f"El tamaño del nombre es {tam_nombre}")
        else:
            print("No se encuentra ese nombre en la lista")
        
        buscar_otro = input("Quiere buscar otro nombre? [s/n]\n").lower()
        if buscar_otro != "s":
            buscar_otro = input("Esta seguro que no quiere buscar otro nombre? [s/n]\n").lower()
            if buscar_otro != "s":    
                break

    seguir = input("Desea cargar nombres nuevamente? [s/n]\n")
    if seguir != "s":
        seguir = input("Esta seguro que quiere salir? [s/n]\n")
        if seguir != "s":
            break

print("FIN DEL PROGRAMA")