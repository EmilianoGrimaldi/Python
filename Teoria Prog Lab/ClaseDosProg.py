# Errores de Logica, errores de sintaxis

# Maneras de validar
# Equivalente al do-while (validar enteros)
# while True:  # Siempre va a entrar al bucle
#     edad = int(input("Ingrese edad 18-65: "))
#     if (not (edad < 18 or edad > 65)):
#         break  # para salir del bucle infinito

# print(edad)

# # Validar Strings
# a = "hola"
# try:  # Trata de hacer esto
#     a = int(a)
# except ValueError:  # Si aparece un error ejecuta esto
#     pass  # No significa nada
#     print("Trataste de convertir un entero a una cadena")
# else:  # Sino ejecuta esto
#     print(a)
# finally:  # Se ejecuta si o si
#     print("Estoy en el finally")

# # Ejemplo 2 de validar entero BUENA MANERA DE VALIDAR
# while True:  # Siempre va a entrar al bucle
#     try:
#         edad = int(input("Ingrese edad 18-65: "))
#         if (not (edad < 18 or edad > 65)):
#             break  # para salir del bucle infinito
#         else: 
#             print("Edad fuera de rango")
#     except ValueError:
#         print("Eso no es un numero")

# print(edad)

# #Ejemplo 3 
# a = 30
# b = 15
# try:
#     resultado = a / b
# except ZeroDivisionError:
#     print("No se puede dividir por 0")
# else:
#     print(resultado)

# #str() convierte a string
# a = 20
# try:
#     print("El valor de a es " + a)
# except TypeError:
#     print("No se puede concatenar string con numeros")

#Ejemplo 4
# while(True):
#     edad = input("Ingrese edad 18-65: ")
#     if(edad.isdigit()):
#         edad = int(edad)
#         if(not(edad < 18 or edad > 65)):
#             break
#         else:
#             print("Edad fuera de rango")
#     else:
#         print("Eso no es un numero")

# print(edad)

#CONCATENAR y Mostrar Info
#Ejemplo 5 
# a = "Juan"
# b = 20
#print(a, b) no es concantenar, es para mostrar varios resultados
#Python esta programado en C internamente
# print("Nombre: {} Edad: {}".format(a,b)) # Forma 1
# print("Nombre: %s Edad: %d" %(a, b)) #forma 2
# print(f"Nombre: {a} Edad: {b}") #Forma 3
# print("Esto \"Hola\" ") # para mostrar las comillas como caracter
# print('Esto "es" comilla') #Mostrar comillas como caracteres usando comillas simples
# print("Hola esto es 'comilla'.")
# print("Hola \t como estas") # \t para dejar espacio
# print("Hola \ncomo estas") # \n salto de linea

# Esto no ocupa espacio memoria
# "Esto ocupa espacio en memoria" #Aunque lo pueda usar como comentario
# numero = 30
# print(numero)
