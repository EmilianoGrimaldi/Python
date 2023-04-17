import os
# Ejercicio con Menú de Opciones
# Realizar un programa utilizando los conceptos de la clase del lunes:
# Opciones del menú:
# 1 cargar una lista con 10 números
# 2 mostrar el total de los números ingresados
# 3 mostrar el promedio
# 4 mayor
# 5 menor
# 6 pedir un número y decir si está en la lista
# 7 pedir un número e informar todos los índices donde aparece
# 8 informar cuantos números pares y cuantos impares hay en la lista
# 9 informar cuantos positivos, cuantos negativos y cuantos ceros hay en la lista
# 10 vaciar lista
# 11 Salir
# Para utilizar las opciones 2 a la 10 hay que cargar los números en la opción 1
# Si se vacía la lista con la opción 10 se deben bloquear nuevamente las opciones hasta que se cargue de nuevo los números con la opción 1

bandera_hay_numeros = False
lista_numeros = []
indices_numeros = []
total = 0
bandera_maximo = False
bandera_minimo = False
bandera_mismo_num = False
bandera_indice = False
contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0
contador_ceros = 0

while True:
    os.system("cls")
    while True:
        try:
            opcion = int(input("########                MENU DE OPCIONES                 ########\n\n1 --> Cargar una lista con 10 números\n2 --> Mostrar el total de los números ingresados\n3 --> Mostrar el promedio\n4 --> Mayor\n5 --> Menor\n6 --> Pedir un número y decir si está en la lista\n7 --> Pedir un número e informar todos los índices donde aparece\n8 --> Informar cuantos números pares y cuantos impares hay en la lista\n9 --> Informar cuantos positivos, cuantos negativos y cuantos ceros hay en la lista\n10--> Vaciar lista\n11--> Salir\n\n"))
            if opcion >= 1 and opcion <= 11:
                break
            else:
                print("Error! Opcion inexistente\n")
        except ValueError:
            print(f"Error de tipo. Ingrese una opcion numerica\n")

    match opcion:
        case 1:
            if not bandera_hay_numeros:
                for carga_numeros in range(1, 11):
                    while True:
                        try:
                            numero = int(input("Ingrese un numero\n"))
                            break
                        except ValueError:
                            print(f"Error de tipo")
                    lista_numeros.append(numero)

                if len(lista_numeros) == 10:
                    bandera_hay_numeros = True
            else:
                print("Ya cargaste los 10 numeros en la lista")

        case 2:
            if bandera_hay_numeros:
                if total == 0:
                    for numero in lista_numeros:
                        total += numero
                print(f"El total de los numeros ingresados es --> {total}")
            else:
                print("No se cargaron los numeros en la opcion 1")

        case 3:
            if bandera_hay_numeros:
                if total == 0:
                    for numero in lista_numeros:
                        total += numero
                promedio = total / len(lista_numeros)
                print(
                    f"El promedio de los numeros ingresados es --> {promedio}")
            else:
                print("No se cargaron los numeros en la opcion 1")

        case 4:
            if bandera_hay_numeros:
                for numero in lista_numeros:
                    if bandera_maximo == False or numero > numero_maximo:
                        bandera_maximo = True
                        numero_maximo = numero
                print(f"El numero maximo ingresado es --> {numero_maximo}")
                # Muestro y vuelvo a resetear los valores
                bandera_maximo = False
                numero_maximo = None
            else:
                print("No se cargaron los numeros en la opcion 1")

        case 5:
            if bandera_hay_numeros:
                for numero in lista_numeros:
                    if bandera_minimo == False or numero < numero_minimo:
                        bandera_minimo = True
                        numero_minimo = numero
                print(f"El numero minimo ingresado es --> {numero_minimo}")
                # Muestro y vuelvo a resetear los valores
                bandera_minimo = False
                numero_minimo = None
            else:
                print("No se cargaron los numeros en la opcion 1")

        case 6:
            if bandera_hay_numeros:
                while True:
                    try:
                        pedir_numero = int(input("Ingresa numero a buscar\n"))
                        break
                    except ValueError:
                        print(f"Error de tipo")

                for numero in lista_numeros:
                    if pedir_numero == numero:
                        bandera_mismo_num = True
                        break

                if bandera_mismo_num:
                    print("El numero ingresado esta en la lista")
                    bandera_mismo_num = False
                else:
                    print("El numero ingresado no esta en la lista")
            else:
                print("No se cargaron los numeros en la opcion 1")

        case 7:
            if bandera_hay_numeros:
                while True:
                    try:
                        pedir_numero = int(input("Ingresa numero a buscar\n"))
                        break
                    except ValueError:
                        print(f"Error de tipo")

                for i in range(len(lista_numeros)):
                    if lista_numeros[i] == pedir_numero:
                        indices_numeros.append(i)
                        bandera_indice = True

                if bandera_indice:
                    print(
                        f"El numero ingresado aparece en los siguientes indices --> {indices_numeros}")
                    bandera_indice = False
                    indices_numeros.clear()
                else:
                    print(f"El numero ingresado no se encuentra")
            else:
                print("No se cargaron los numeros en la opcion 1")

        case 8:
            if bandera_hay_numeros:
                for numero in lista_numeros:
                    if numero % 2 == 0:
                        contador_pares += 1
                    else:
                        contador_impares += 1
                print(
                    f"En la lista de numeros ingresada hay {contador_pares} --> numeros pares, {contador_impares} --> numeros impares")
                contador_pares = 0
                contador_impares = 0
            else:
                print("No se cargaron los numeros en la opcion 1")

        case 9:
            if bandera_hay_numeros:
                for numero in lista_numeros:
                    if numero > 0:
                        contador_positivos += 1
                    else:
                        if numero < 0:
                            contador_negativos += 1
                        else:
                            contador_ceros += 1
                print(
                    f"En la lista hay {contador_positivos} --> numeros positivos, {contador_negativos} --> numeros negativos y {contador_ceros} --> ceros")
                contador_positivos = 0
                contador_negativos = 0
                contador_ceros = 0
            else:
                print("No se cargaron los numeros en la opcion 1")

        case 10:
            if bandera_hay_numeros:
                confirmar_limpiar_lista = input(
                    "Esta seguro que queres limpiar la lista? [s/n]\n").lower()
                if confirmar_limpiar_lista == "s":
                    lista_numeros.clear()
                    total = 0
                    bandera_hay_numeros = False
            else:
                print("No se cargaron los numeros en la opcion 1")

        case 11:
            if opcion == 11:
                confirmacion = input(
                    "Esta seguro que salir del programa? [s/n]\n").lower()
                if confirmacion == "s":
                    break
    os.system("pause")
print("FIN DEL PROGRAMA")
