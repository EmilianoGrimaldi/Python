# 2) Se nos pide armar una aplicación para las elecciones, para eso necesitamos ingresar el nombre de los 5 candidatos a presidente de la nación,  la edad de cada uno (mayor a 35 años de edad) y la cantidad de votos (número positivo 0 incluido)  que sacó en las elecciones.
# Informar: 
# •	el candidato con más votos
# •	el candidato con menos votos
# •	el promedio de edades de los candidatos
# •	total de votos emitidos.
# •	el porcentaje de los votos de los 5 candidatos

#Declaracion de variables
contador_de_candidatos = 0
bandera_mas_votos = True
nombre_candidato_con_mas_votos = ""
candidato_con_mas_votos = None
bandera_menos_votos = True
nombre_candidato_con_menos_votos = ""
candidato_con_menos_votos = None
acumulador_edades = 0
votos_totales = 0
porcentaje_de_votos = None
porcentaje_candidato = 0
#Utilizo bucle for al saber las veces que tengo que iterar, sino utilizaria while
for i in range(1,6):
    #Pedido de datos al usuario y validacion
    nombre_de_candidato = input("Ingresar nombre del candidato: ")

    edad_de_candidato = int(input("Ingresar la edad del candidato [Mayor a 35]: ")) #Pido la edad y la paso a entero
    while(edad_de_candidato < 36):
        edad_de_candidato = int(input("Reingresar la edad del candidato [Mayor a 35]: "))

    votos_de_candidato = int(input("Ingresar los votos del candidato [Mayor a 0]: ")) #Pido los votos y lo paso a entero
    while(votos_de_candidato < 0):
        votos_de_candidato = int(input("Reingresar los votos del candidato [Mayor a 0]: "))
    
    if(bandera_mas_votos == True):
        nombre_candidato_con_mas_votos = nombre_de_candidato
        candidato_con_mas_votos = votos_de_candidato
        bandera_mas_votos = False
    else:
        if(votos_de_candidato > candidato_con_mas_votos):
            nombre_candidato_con_mas_votos = nombre_de_candidato
            candidato_con_mas_votos = votos_de_candidato

    if(bandera_menos_votos == True):
        nombre_candidato_con_menos_votos = nombre_de_candidato
        candidato_con_menos_votos = votos_de_candidato
        bandera_menos_votos = False
    else:
        if(votos_de_candidato < candidato_con_menos_votos):
            nombre_candidato_con_menos_votos = nombre_de_candidato
            candidato_con_menos_votos = votos_de_candidato   
    
    match(i):
        case 1:
            votos_candidato_uno = votos_de_candidato
            nombre_canidato_uno = nombre_de_candidato
        case 2:
            votos_candidato_dos = votos_de_candidato
            nombre_canidato_dos = nombre_de_candidato
        case 3: 
            votos_candidato_tres = votos_de_candidato
            nombre_canidato_tres = nombre_de_candidato
        case 4:
            votos_candidato_cuatro = votos_de_candidato
            nombre_canidato_cuatro = nombre_de_candidato
        case 5:
            votos_candidato_cinco = votos_de_candidato
            nombre_canidato_cinco = nombre_de_candidato
    
    acumulador_edades += edad_de_candidato
    votos_totales += votos_de_candidato
    contador_de_candidatos += 1
    
promedio_de_edades_de_candidatos = acumulador_edades / contador_de_candidatos
porcentaje_votos_candidato_uno = (votos_candidato_uno / votos_totales) * 100
porcentaje_votos_candidato_dos = (votos_candidato_dos / votos_totales) * 100
porcentaje_votos_candidato_tres = (votos_candidato_tres / votos_totales) * 100
porcentaje_votos_candidato_cuatro = (votos_candidato_cuatro / votos_totales) * 100
porcentaje_votos_candidato_cinco = (votos_candidato_cinco / votos_totales) * 100

#INFORMES
print("El candidato con mas votos es:", nombre_candidato_con_mas_votos, "con", candidato_con_mas_votos, "votos")
print("El candidato con menos votos es:", nombre_candidato_con_menos_votos, "con", candidato_con_menos_votos, "votos")
print("El promedio de edades de los candidatos es:", promedio_de_edades_de_candidatos)
print("El total de votos emitidos fue:", votos_totales)
print("El porcentaje de", nombre_canidato_uno, "fue:", round(porcentaje_votos_candidato_uno,2),"%")
print("El porcentaje de", nombre_canidato_dos, "fue:", round(porcentaje_votos_candidato_dos,2),"%")
print("El porcentaje de", nombre_canidato_tres, "fue:", round(porcentaje_votos_candidato_tres,2),"%")
print("El porcentaje de", nombre_canidato_cuatro, "fue:", round(porcentaje_votos_candidato_cuatro,2),"%")
print("El porcentaje de", nombre_canidato_cinco, "fue:", round(porcentaje_votos_candidato_cinco,2),"%")