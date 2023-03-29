#################### PEDIR DATOS AL USUARIO ##########################

edad = int(input("Ingrese edad: "))
print(type(edad), edad)
# # Al separar con "," puede mostrar mas de un valor
# # type para ver el tipo de dato

################# IF #################
if (edad >= 18):
    print("Sos mayor de edad")
else:
    if (edad >= 13):
        print("Sos adolecente")
    else:
        print("Sos menor de edad")
# Para pedir datos al usuario uso input
# shift + alt + f para acomodar el codigo
# control + } para comentar todo lo marcado
# int() para pasar str a entero
# float() para pasar str a decimal
# // para hacer division entera
# / para div con decimal
# ** para potencia
# la variable valor va tomar el primer valor 0

########## FOR ############
for valor in range(10):
    print(valor)
for valor in range(10):
    print(valor + 1)
for valor in range(1,10):
    print(valor)
# range comienza desde 0 y es iterable
# Primer parametro desde donde empieza a iterar
# Segundo parametro las veces que va a iterar
# Tercer parametro va a mostrar cada x numero
for valor in range(1,10,2):
    print(valor)

#################### SWITCH ##################
valor = 20
match ():
    case 1:
        print("Uno")
    case 2:
        print("Dos")
    case 3:
        print("Tres")
    case 4:
        print("Cuatro")
    case 5:
        print("Cinco")
    case _:
        print("Default")
        