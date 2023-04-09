#7- 
# Un grupo de cinco amigos se juntan para jugar una partida de CS:GO, deciden que van a jugar 10 partidas y necesitan realizar datos estadísticos sobre las partidas jugadas. Para eso necesitan ingresar los siguientes datos en el siguiente orden especifico: nombre, edad, bajas confirmadas (el murió), muertes confirmadas (el mate a otro jugador). Con esos datos se necesita saber:
# • Nombre del jugador más joven.
# • Jugador que más bajas tuvo.
# • Jugador con menos muertes
# • El promedio de bajas del equipo
# • La cantidad de jugadores que tienen entre 20 y 30 años cuyas bajas estan entre 10 y 20
# • El nombre y edad del jugador que más muertes tuvo (MVP)
# Nota: los datos tienen que ingresar en 1 solo string separado por espacios, y ser almacenados en una lista, investigar que función les permite lograrlo y como hacer una lista de listas.

#iterar 10 veces pidiendo los datos
lista_partidas = []
bandera_joven = False
bandera_mas_bajas = False
bandera_menos_muertes = False
acumulador_bajas = 0

for partidas in range(1,11):
    estadisticas_jugador = input("Nombre -- Edad -- Bajas -- Muertes\n")
    un_jugador = estadisticas_jugador.split()
    lista_partidas.append(un_jugador) # Lista de listas
    
    for jugador in lista_partidas:
        if bandera_joven == False or jugador[1] < edad_joven:
            nombre_joven = jugador[0]
            edad_joven = jugador[1]
            bandera_joven = True
    
    for jugador in lista_partidas:
        if bandera_mas_bajas == False or jugador[2] > mas_bajas:
            mas_bajas = jugador[2]
            nombre_mas_bajas = jugador[0]
            bandera_mas_bajas = True
    
    for jugador in lista_partidas:
        if bandera_menos_muertes == False or jugador[3] < menos_muertes:
            menos_muertes = jugador[3]
            nombre_menos_muertes = jugador[0]
            bandera_menos_muertes = True

    acumulador_bajas += int(un_jugador[2])
    
print(f"El nombre mas joven es {nombre_joven} y tiene {edad_joven} años")
print(f"Jugador que más bajas tuvo es {nombre_mas_bajas}")
print(f"Jugador con menos muertes es {nombre_menos_muertes}")
print(f"Las bajas totales fueron {acumulador_bajas}")
# for jugador in lista_partidas:
#     print(jugador)