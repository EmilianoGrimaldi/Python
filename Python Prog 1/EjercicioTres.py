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
contador_vehiculos_numero_par = 0
bandera_piloto_menos_victorias = True
contador_piloto_mayor_25 = 0
bandera_piloto_mas_veterano = True
acumulador_edad_vehiculos_par = 0

#UTILIZO UN BUCLE FOR QUE LE PERMITA CARGAR LOS 10 INTEGRANTES
for i in range(1,11):
    #Ingreso y validacion de datos
    nombre_piloto = input("Ingrese nombre: ")

    edad_piloto = int(input("Ingrese edad [mayor a 18]: "))
    while(edad_piloto < 19):
        edad_piloto = int(input("Reingrese edad [mayor a 18]: "))
    
    nacionalidad_piloto = input("Ingrese nacionalidad [argentino, inglés, francés, brasilero, estadounidense]: ")
    while(nacionalidad_piloto != "argentino" and nacionalidad_piloto != "ingles" and nacionalidad_piloto != "frances" and nacionalidad_piloto != "brasilero" and nacionalidad_piloto != "estadounidense" ):
        nacionalidad_piloto = input("Reingrese nacionalidad [argentino, inglés, francés, brasilero, estadounidense]: ")
    
    cantidad_carreras_ganadas = int(input("Ingrese la cantidad de carreras ganadas [Mayor a 0]: "))
    while(cantidad_carreras_ganadas < 1):
        cantidad_carreras_ganadas = int(input("Reingrese la cantidad de carreras ganadas [Mayor a 0]: "))
    
    numero_vehiculo = int(input("Ingrese numero de vehiculo [Mayor a 0]: "))
    while(numero_vehiculo < 1):
       numero_vehiculo = int(input("Reingrese numero de vehiculo [Mayor a 0]: ")) 

    if(i == 1):
        piloto_mas_joven = edad_piloto
        nacionalidad_mas_joven = nacionalidad_piloto
        nombre_piloto_mas_joven = nombre_piloto
        piloto_joven_mas_victorias = cantidad_carreras_ganadas
        piloto_mas_veterano = edad_piloto
        nacionalidad_mas_veterano = nacionalidad_piloto  
        piloto_veterano_menos_victorias = cantidad_carreras_ganadas
    else:
        if(edad_piloto < piloto_mas_joven):
            piloto_mas_joven = edad_piloto
            nacionalidad_mas_joven = nacionalidad_piloto
            
            if(cantidad_carreras_ganadas > piloto_joven_mas_victorias):
                nombre_piloto_mas_joven = nombre_piloto
                piloto_joven_mas_victorias = cantidad_carreras_ganadas
                
        if(edad_piloto > piloto_mas_veterano):
            if(cantidad_carreras_ganadas < piloto_veterano_menos_victorias):
                piloto_mas_veterano = edad_piloto
                nacionalidad_mas_veterano = nacionalidad_piloto      
                piloto_veterano_menos_victorias = cantidad_carreras_ganadas 
    
    if(numero_vehiculo % 2 == 0):
        contador_vehiculos_numero_par += 1
        acumulador_edad_vehiculos_par += edad_piloto
    else:
        if(bandera_piloto_menos_victorias == True):
            piloto_menos_victorias = cantidad_carreras_ganadas
            nombre_piloto_menos_victorias = nombre_piloto
            bandera_piloto_menos_victorias = False
        else:
            if(cantidad_carreras_ganadas < piloto_menos_victorias):
                piloto_menos_victorias = cantidad_carreras_ganadas
                nombre_piloto_menos_victorias = nombre_piloto
        if(edad_piloto > 25):
            contador_piloto_mayor_25 += 1

promedio_edad_vehiculo_par = acumulador_edad_vehiculos_par /  contador_vehiculos_numero_par


# *Nacionalidad del piloto más joven.
print("Nacionalidad del piloto más joven:", nacionalidad_mas_joven)
# *Cantidad de vehículos con número par.
print("Cantidad de vehículos con número par:", contador_vehiculos_numero_par)
# *Nombre del piloto con menos victorias y el número de auto impar.
print("Nombre del piloto con menos victorias y el número de auto impar:", nombre_piloto_menos_victorias)
# *Cantidad de pilotos mayores de 25 años con número de vehículo impar.
print("Cantidad de pilotos mayores de 25 años con número de vehículo impar:", contador_piloto_mayor_25)
# *Nombre del piloto más joven con más victorias.
print("Nombre del piloto más joven con más victorias:", nombre_piloto_mas_joven)
# *Nacionalidad del piloto más veterano con menos victorias.
print("Nacionalidad del piloto más veterano con menos victorias:", nacionalidad_mas_veterano)
# *Promedio de edad de los pilotos que tiene un vehículo con número par.
print("El promedio de edad de los pilotos que tienen un vehiculo con numero par es:", promedio_edad_vehiculo_par)