#9) Realizar un programa que pida una cadena de texto al usuario y le pida una cadena de texto y determine que la cadena ingresada es un palíndromo o no. De serlo deberá imprimir la palabra por consola.
while True:
    palabra = input("Ingrese una palabra\n").lower()
    if palabra.isalpha():
        break
    else:
        print(f"Error! Usted ingreso {palabra}. Se pidio una cadena alfabetica")

if palabra == palabra[::-1]: 
    print(f"{palabra} es un palíndromo")
else:
    print("No es un palíndromo")

# [inicio-fin-paso][::-1] en Python se utiliza para invertir una cadena (o cualquier secuencia iterable, como una lista).Si se omite el valor de inicio, se toma por defecto el inicio de la secuencia (índice 0). Si se omite el valor de fin, se toma por defecto el final de la secuencia (el último índice). Y si se omite el valor de paso, se toma por defecto un paso de 1. En el caso de palabra[::-1], se omite el valor de inicio y de fin, y se especifica un paso de -1. Esto significa que se selecciona toda la secuencia (la palabra completa en este caso), pero en orden inverso.