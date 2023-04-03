# Ejercicio 02
# Debemos hacer un programa para que el usuario recuerde las reglas de estilo de
# python, entonces debemos pedirle al usuario un número entre el 1 y el 8,
# al ingresar el número debemos mostrarle que regla de estilo representa y su
# descripción (Sacar la información de las diapositivas de las reglas de estilo).
# En caso de que ingrese un numero fuera del rango deberá mostrarle al usuario “Error,
# regla de estilo inexistente”

# 1 Pedir entero al usuario entre 1 - 8 y validar que haya ingresado un entero
# 2 con un match agregar en cada case con un print agregar la descripcion de cada regla de estilo y lo que representa
# 3 un default para mostrarle al usuario que esa regla de estilo no existe

while(True):
    try:
        entero_regla_estilo = int(input("Ingrese una opcion entre [1 - 8] para mostrar la regla de estilo correspondiente: "))
        if(entero_regla_estilo >= 1 and entero_regla_estilo <= 8):
            break
        else:
            print("Error! Opcion fuera de rango")
    except ValueError:
        print("Error! Solo numeros")
        
match(entero_regla_estilo):
    case 1:
        print("Regla de estilo #1: Utiliza 4 espacios para la indentación")
        print("Esta regla indica que debemos usar 4 espacios para la indentación en lugar de tabulaciones.")
    case 2:
        print("Regla de estilo #2: Limita la longitud de las líneas a 79 caracteres")
        print("Esta regla sugiere que las líneas de código no deben tener más de 79 caracteres para mejorar la legibilidad.")
    case 3:
        print("Regla de estilo #3: Utiliza líneas en blanco para separar funciones y clases")
        print("Esta regla sugiere que debemos usar líneas en blanco para separar funciones y clases y mejorar la legibilidad del código.")
    case 4:
        print("Regla de estilo #4: Usa comentarios para explicar el código")
        print("Esta regla sugiere que debemos usar comentarios para explicar el código y hacerlo más legible y fácil de entender.")
    case 5:
        print("Regla de estilo #5: Sigue la convención de nombres de variables")
        print("Esta regla sugiere que debemos seguir la convención de nombres de variables de Python para mejorar la legibilidad del código.")
    case 6:
        print("Regla de estilo #6: Utiliza espacios alrededor de los operadores")
        print("Esta regla sugiere que debemos usar espacios alrededor de los operadores para mejorar la legibilidad del código.")
    case 7:
        print("Regla de estilo #7: No uses espacios al final de las líneas")
        print("Esta regla sugiere que no debemos dejar espacios al final de las líneas para evitar problemas con algunos editores de texto.")
    case 8:
        print("Regla de estilo #8: Utiliza la herramienta de formato automático")
        print("Esta regla sugiere que debemos utilizar la herramienta de formato automático para mejorar la legibilidad del código.")
    case _:
        print("Error, regla de estilo inexistente")
