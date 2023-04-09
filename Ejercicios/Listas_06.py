#6-Se nos pide realizar un programa que le pida al usuario una N cantidad de veces y calcular la máxima diferencia en la secuencia de números ingresada.

continuar = "y"
lista_numeros = []
bandera_minimo = False
bandera_maximo = False

while continuar == "y":
    #Validacion de ingreso de numeros
    while True:
        try:
            numero = int(input("Ingrese un numero\n"))
            break
        except ValueError:
            print("Error de tipo! Solo se permiten enteros")
    #agrego los numeros a la lista
    lista_numeros.append(numero)
    #Busco el minimo en la lista 
    for numero in lista_numeros:
        if bandera_minimo == False or numero < numero_minimo:
            numero_minimo = numero
            bandera_minimo = True
    #Busco el maximo en la lista
    for numero in lista_numeros:
        if bandera_maximo == False or numero > numero_maximo:
            numero_maximo = numero
            bandera_maximo = True

    continuar = input("Para continuar presione 'y'. Para salir cualquier tecla.\n").lower()

diferencia_maxima = abs(numero_maximo - numero_minimo)
#abs lo utilizo para que la diferencia siempre sea un valor positivo
print(f"La diferencia maxima en la secuencia de numeros es {diferencia_maxima}")