# 3) Copa pistón!!!
# Se deberá generar un programa para registrar las estadísticas de los 10 integrantes de una carrera de autos.
# Se pedirá el ingreso de:
# nombre
#  edad (mayor a 18)
# nacionalidad del piloto (argentino, inglés, francés, brasilero, estadounidense)
#  cantidad de carreras ganadas (no pueden ser números negativos)
#  número del vehículo (no puede ser un número negativo)

# se necesita saber:
# *Nacionalidad del piloto más joven.
# *Cantidad de vehículos con número par.
# *Nombre del piloto con menos victorias y el número de auto impar.
# *Cantidad de pilotos mayores de 25 años con número de vehículo impar.
# *Nombre del piloto más joven con más victorias.
# *Nacionalidad del piloto más veterano con menos victorias.
# *Promedio de edad de los pilotos que tiene un vehículo con número par.

#DECLARACION DE VARIABLES
bandera_piloto_nacionalidad_joven = True

#UTILIZO UN BUCLE FOR QUE LE PERMITA CARGAR LOS 10 INTEGRANTES
for i in range(1,4):
    #Ingreso y validacion de datos
    nombre_piloto = input("Ingrese nombre: ")

    edad_piloto = int(input("Ingrese edad [mayor a 18]: "))
    while(edad_piloto < 18):
        edad_piloto = int(input("Reingrese edad [mayor a 18]: "))
    
    nacionalidad_piloto = input("Ingrese nacionalidad [argentino, inglés, francés, brasilero, estadounidense]: ")
    while(nacionalidad_piloto != "argentino" and nacionalidad_piloto != "ingles" and nacionalidad_piloto != "frances" and nacionalidad_piloto != "brasilero" and nacionalidad_piloto != "estadounidense" ):
        nacionalidad_piloto = input("Reingrese nacionalidad [argentino, inglés, francés, brasilero, estadounidense]: ")
    
    cantidad_carreras_ganadas = int(input("Ingrese la cantidad de carreras ganadas [Mayor a 0]: "))
    while(cantidad_carreras_ganadas < 0):
        cantidad_carreras_ganadas = int(input("Reingrese la cantidad de carreras ganadas [Mayor a 0]: "))
    
    numero_vehiculo = int(input("Ingrese numero de vehiculo [Mayor a 0]: "))
    while(numero_vehiculo < 0):
       numero_vehiculo = int(input("Reingrese numero de vehiculo [Mayor a 0]: ")) 

    #Nacionalidad del piloto más joven.
    #Para saber esto necesito:
    #en la primera iteracion guardar la edad del piloto en una variable auxiliar y luego en cada iteracion ir comparando la variable de edad con la auxiliar para ver si es menor. Si es el caso guardo la nacionalidad del piloto mas joven
    if(i == 1):
        piloto_mas_joven = edad_piloto
        nacionalidad_mas_joven = nacionalidad_piloto
    else:
        if(edad_piloto < piloto_mas_joven):
            piloto_mas_joven = edad_piloto
            nacionalidad_mas_joven = nacionalidad_piloto
print("La nacionalidad del piloto mas joven es: ", nacionalidad_mas_joven)