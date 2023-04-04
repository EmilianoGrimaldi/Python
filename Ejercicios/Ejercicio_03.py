# Ejercicio 03
# Es la gala final de Gran Hermano y la producción nos pide un programa para contar
# los votos de los televidentes y saber cuál será el participante que ganará el juego.
# Los participantes finalistas son: Nacho, Julieta y Marcos.

# El televidente debe ingresar:
# ● Nombre del votante
# ● Edad del votante (debe ser mayor a 13)
# ● Género del votante (masculino, femenino, otro)
# ● El nombre del participante a quien le dará el voto positivo.
# No se sabe cuántos votos entrarán durante la gala.
# Se debe informar al usuario:s
# A. El promedio de edad de las votantes de género femenino. HECHO
# B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta. HECHO
# C. Nombre del votante más joven que votó a Nacho. HECHO
# D. Nombre de cada participante y porcentaje de los votos qué recibió.
# E. El nombre del participante que ganó el reality (El que tiene más votos)

seguir = 1
acumulador_edad_femenino = 0
contador_de_votantes_femenino = 0
cantidad_votantes_masculinos = 0
contador_de_vueltas = 0
bandera_mas_joven_nacho = True
edad_mas_joven = None
nombre_mas_joven = None
contador_votos_nacho = 0
contador_votos_marcos = 0
contador_votos_julieta = 0

while seguir == 1:
    while True:
        nombre_del_votante = input("Nombre del votante: ")
        if (nombre_del_votante.isalpha()):
            # isalpha() Devuelve True si lo que se ingreso es una cadena alfabetica de lo contrario devuelve False
            break
        else:
            print(f"Error! Formato de nombre incorrecto, solo se permiten letras.\nUsted ingreso: {nombre_del_votante}")

    while True:
        try:
            edad_del_votante = int(input("Ingrese su edad [Mayor a 13]: "))
            if (edad_del_votante > 13):
                break
            else:
                print("Error! Debe ingresar una edad mayor a 13")
        except ValueError:
            print("Intento ingresar un string, cuando se pide un entero")

    while True:
        genero_del_votante = input("Ingrese su genero [Masculino - Femenino - Otro]: ")
        if genero_del_votante == "Masculino" or genero_del_votante == "Femenino" or genero_del_votante == "Otro":
            break
        else:
            print("Error! Se ingreso un genero inexistente")

    while True:
        participante_a_votar = input("Ingrese el nombre del participante a votar [Nacho - Julieta - Marcos]: ")
        if participante_a_votar == "Nacho" or participante_a_votar == "Julieta" or participante_a_votar == "Marcos":
            break
        else:
            print("Error! Participante inexistente")

    if genero_del_votante == "Femenino":
                acumulador_edad_femenino += edad_del_votante
                contador_de_votantes_femenino += 1
    else:
         if genero_del_votante == "Masculino":
              if edad_del_votante >= 25 and edad_del_votante <= 40:
                   if participante_a_votar == "Nacho" or participante_a_votar == "Julieta":
                       cantidad_votantes_masculinos += 1 
   
    match participante_a_votar:
        case "Nacho":
            if bandera_mas_joven_nacho == True:
                edad_mas_joven = edad_del_votante
                nombre_mas_joven = nombre_del_votante
                bandera_mas_joven_nacho = False
            else:
                if edad_del_votante < edad_mas_joven:
                    edad_mas_joven = edad_del_votante
                    nombre_mas_joven = nombre_del_votante         
            contador_votos_nacho += 1
        case "Marcos":
            contador_votos_marcos += 1
        case "Julieta":
            contador_votos_julieta += 1

    contador_de_vueltas += 1

    while True:
        try:
            seguir = int(input("¿Hay mas votos para ingresar? Ingrese 1 para confirmar o 0 para salir: "))
            if seguir == 1 or seguir == 0:
                break
            else:
                print("Error! Opcion inexistente")
        except ValueError:
            print("Ingresaste una letra y te pedi un entero")

porcentaje_votos_nacho = (contador_votos_nacho / contador_de_vueltas) * 100
porcentaje_votos_marcos = (contador_votos_marcos / contador_de_vueltas) * 100
porcentaje_votos_julieta = (contador_votos_julieta / contador_de_vueltas) * 100

# A. El promedio de edad de las votantes de género femenino
if(contador_de_votantes_femenino > 0):
    promedio_edad_femenino = acumulador_edad_femenino / contador_de_votantes_femenino
    print(f"El promedio de edad de las votantes de género femenino es {promedio_edad_femenino}")
else:
    print("No se ingresaron votantes femeninos")

# B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta.
print(f"Cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta fueron {cantidad_votantes_masculinos}")

#C. Nombre del votante más joven que votó a Nacho.
print(f"El nombre del votante mas joven que voto a Nacho es {nombre_mas_joven}")

# D. Nombre de cada participante y porcentaje de los votos qué recibió.
print(f"Nacho: {porcentaje_votos_nacho}%\nMarcos: {porcentaje_votos_marcos}%\nJulieta: {porcentaje_votos_julieta}%")

# E. El nombre del participante que ganó el reality (El que tiene más votos)
if contador_votos_nacho > contador_votos_marcos and contador_votos_nacho > contador_votos_julieta:
    print("El ganador del reality fue Nacho")
else:
    if contador_votos_marcos > contador_votos_nacho and contador_votos_marcos > contador_votos_julieta:
        print("El ganador del reality fue Marcos")
    else:
        print("El ganador del reality fue Julieta")