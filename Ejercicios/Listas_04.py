# 4-
# Debemos desarrollar un algoritmo que permita computar los votos del Senado de Berlinberlín. Se deberá ingresar el nombre de cada senador y si está Presente o no en la sesión. Si el senador está presente, se deberá pedir el valor del voto
# El voto de los senadores berliberlineses puede ser Afirmativo, Negativo o Abstención (validar). El valor por defecto para los senadores ausentes será Abstención.
# Se deberá Informar:
# o Cantidad total de senadores.
# o Cantidad de senadores presentes.
# o Cantidad y porcentaje de votos afirmativos.
# o Cantidad y porcentaje de votos negativos.
# o Cantidad y porcentaje de abstenciones.
# o Generar una lista de senadores por cada tipo de voto y mostrarlas por pantalla.
continuar = "s"
senadores_totales = 0
senadores_presentes = 0
cantidad_senadores_afirmativos = 0
cantidad_senadores_negativos = 0
cantidad_senadores_abstenciones = 0
lista_votos_afirmativos = []
lista_votos_negativos = []
lista_votos_abstenciones = []

while continuar == "s":
    #Pedir en pantalla el nombre de cada senador
    while True:
        nombre_senador = input("Ingrese el nombre del senador\n")
        if nombre_senador.isalpha():
            break
        else:
            print("Error! Solo se permiten caracteres alfabeticos")

    while True:
        presencia_senador = input("Ingrese si esta [presente - ausente]\n").lower()
        if presencia_senador == "presente" or presencia_senador == "ausente":
            break
        else:
            print("Error! Ingreso una opcion inexistente") 

    #Verificar si esta presente o no en la sesion
    # si (esta presente):
    if presencia_senador == "presente":
        #pido el valor del voto
        while True:
            voto_senador = input("Ingrese el valor del voto [afirmativo - negativo]\n").lower()
            if voto_senador == "afirmativo" or voto_senador == "negativo":
                break
            else:
                print("Error! Ingreso una opcion inexistente") 
        #cantidad de senadores presentes
        senadores_presentes += 1
        # si (afirmativo):
        if voto_senador == "afirmativo":
            #cuento la cantidad y calculo el porcentaje
            cantidad_senadores_afirmativos += 1
            lista_votos_afirmativos.append(nombre_senador)
        # si (negativo):
        else:
            if voto_senador == "negativo":
                #cuento la cantidad y calculo el porcentaje
                cantidad_senadores_negativos += 1
                lista_votos_negativos.append(nombre_senador)
    # sino:
    else:
        #el voto sera abstencion
        voto_senador = "abstencion"
        cantidad_senadores_abstenciones += 1
        lista_votos_abstenciones.append(nombre_senador)
        #cuento la cantidad y calculo el porcentaje
    
    continuar = input("Para continuar ingrese 's'. Para salir cualquier tecla\n" )
#calculos
senadores_totales = cantidad_senadores_afirmativos + cantidad_senadores_negativos + cantidad_senadores_abstenciones
porcentaje_votos_afirmativos = (cantidad_senadores_afirmativos * 100)/senadores_totales
porcentaje_votos_negativos = (cantidad_senadores_negativos * 100)/senadores_totales
porcentaje_votos_abstenciones = (cantidad_senadores_abstenciones * 100)/senadores_totales
#informes

# o Cantidad total de senadores.
print(f"Cantidad total de senadores: {senadores_totales}")
# o Cantidad de senadores presentes.
print(f"Cantidad de senadores presentes: {senadores_presentes}")
# o Cantidad y porcentaje de votos afirmativos.
print(f"Cantidad votos afirmativos: {cantidad_senadores_afirmativos}. Porcentaje de votos afirmativos: %{porcentaje_votos_afirmativos}")
# o Cantidad y porcentaje de votos negativos.
print(f"Cantidad votos negativos: {cantidad_senadores_negativos}. Porcentaje de votos negativos: %{porcentaje_votos_negativos}")
# o Cantidad y porcentaje de abstenciones.
print(f"Cantidad de abstenciones: {cantidad_senadores_abstenciones}. Porcentaje de abstenciones: %{porcentaje_votos_abstenciones}")
# o Generar una lista de senadores por cada tipo de voto y mostrarlas por pantalla.
print("######### LISTA SENADORES VOTOS AFIRMATIVOS #############")
for senador in lista_votos_afirmativos:
    print(senador)
print("######### LISTA SENADORES VOTOS NEGATIVOS #############")
for senador in lista_votos_negativos:
    print(senador)
print("######### LISTA SENADORES ABSTENCIONES #############")
for senador in lista_votos_abstenciones:
    print(senador)