# ⦁	Un bar nos contrato para administrar el consumo de los clientes en las distintas mesas del local.
# Para esto debemos desarrollar un algoritmo que nos permita el ingreso de los siguientes datos:
# a.	Nombre del cliente
# b.	Tipo de bebida (validar cerveza, limonada, gaseosa, nada)
# c.	Tipo de comida (papitas, hamburguesa, rabas, nada)
# 	Los precios del bar son:
# 		Cerveza 500 $
# 		Limonada 300 $
# 		Gaseosa 250 $
# 		Papitas 1200 $
# 		Hamburguesa 2000 $
# 		Rabas 1800 $
# Luego de tomar los datos, se nos pide también realizar algunos datos estadísticos con respecto a las consumiciones hechas durante la jornada de la cual no se sabe exactamente cuanta cantidad de ventas se han realizado, a saber se nos pide
# a.	El tipo de comida más vendido y bebida más vendida si la hay.
# b.	El promedio de clientes que ordena solamente bebida.
# c.	Calcular la recaudación bruta y recaudación neta del local.
# d.	Cuánta gente ordenó comida pero no bebida.
continuar = 1
acumulador_bebida = 0
acumulador_comida = 0
cerveza = 500
limonada = 300
gaseosa = 250
papitas = 1200
hamburguesa = 2000
rabas = 1800
bandera_bebidas = 1
bandera_comidas = 1
acumulador_cervezas = 0
acumulador_limonada = 0
acumulador_gaseosa = 0
acumulador_papita = 0
acumulador_hamburguesa = 0
acumulador_rabas = 0


while(continuar == 1):

    nombre_cliente = input("Ingresar el nombre: ")

    tipo_de_bebida = input(
        "Ingresar el tipo de bebida[cerveza - limonada - gaseosa - nada]: ")
    while (tipo_de_bebida != "cerveza" and tipo_de_bebida != "limonada" and tipo_de_bebida != "gaseosa" and tipo_de_bebida != "nada"):
        tipo_de_bebida = input(
            "Reingresar el tipo de bebida[cerveza - limonada - gaseosa - nada]: ")

    tipo_de_comida = input(
        "Ingresar el tipo de comida[papitas - hamburguesa - rabas - nada]: ")
    while (tipo_de_comida != "papitas" and tipo_de_comida != "hamburguesa" and tipo_de_comida != "rabas" and tipo_de_comida != "nada"):
        tipo_de_comida = input(
            "Reingresar el tipo de comida[papitas - hamburguesa - rabas - nada]: ")
        
    match(tipo_de_bebida):
        case "cerveza":
            acumulador_bebida += 1
            bandera_bebidas = 0
            acumulador_cervezas += 1
        case "limonada":
            acumulador_bebida += 1
            bandera_bebidas = 0
            acumulador_limonada += 1
        case "gaseosa":
            acumulador_bebida += 1
            bandera_bebidas = 0
            acumulador_gaseosa += 1

    match(tipo_de_comida):
        case "papitas":
            acumulador_comida += 1
            bandera_comidas = 0
        case "hamburguesa":
            acumulador_comida += 1
            bandera_comidas = 0
        case "rabas":
            acumulador_comida += 1
            bandera_comidas = 0
# a.	El tipo de comida más vendido y bebida más vendida si la hay.
# b.	El promedio de clientes que ordena solamente bebida.
# c.	Calcular la recaudación bruta y recaudación neta del local.
# d.	Cuánta gente ordenó comida pero no bebida.
    if (bandera_bebidas == 0):
        print("-")
    else:
        print("No se ingresaron bebidas")

    if (bandera_comidas == 0):
        print("Se ingresó comida")
    else:
        print("No se ingresó comida")
    
    continuar = int(input("Para continuar presione 1: "))
