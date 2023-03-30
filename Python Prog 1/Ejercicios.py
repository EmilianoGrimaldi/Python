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
acumulador_precio_cerveza = 0
acumulador_precio_limonada = 0
acumulador_precio_gaseosa = 0
acumulador_precio_papitas = 0
acumulador_precio_hamburguesa = 0
acumulador_precio_rabas = 0
bandera_bebidas = True
bandera_comidas = True
acumulador_cervezas = 0
acumulador_limonadas = 0
acumulador_gaseosas = 0
acumulador_papitas = 0
acumulador_hamburguesas = 0
acumulador_rabas = 0
contador_de_clientes = 0
promedio_de_bebidas = None
recaudacion_bruta = None
promedio_de_comida = None

while (continuar == 1):

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
            acumulador_cervezas += 1
            acumulador_precio_cerveza += 500
            bandera_bebidas = False
        case "limonada":
            acumulador_bebida += 1
            acumulador_limonadas += 1
            acumulador_precio_limonada += 300
            bandera_bebidas = False
        case "gaseosa":
            acumulador_bebida += 1
            acumulador_gaseosas += 1
            acumulador_precio_gaseosa += 250
            bandera_bebidas = False

    match(tipo_de_comida):
        case "papitas":
            acumulador_comida += 1
            acumulador_papitas += 1
            acumulador_precio_papitas += 1200
            bandera_comidas = False
        case "hamburguesa":
            acumulador_comida += 1
            acumulador_hamburguesas += 1
            acumulador_precio_hamburguesa += 2000
            bandera_comidas = False
        case "rabas":
            acumulador_comida += 1
            acumulador_rabas += 1
            acumulador_precio_rabas += 1800
            bandera_comidas = False

    contador_de_clientes += 1
    continuar = int(input("Para continuar presione 1: "))

# a.	El tipo de comida más vendido y bebida más vendida si la hay.
if (bandera_bebidas == False):
    if (acumulador_cervezas > acumulador_gaseosas and acumulador_cervezas > acumulador_limonadas):
        print("La cerveza es la bebida mas vendida")
    else:
        if (acumulador_gaseosas > acumulador_cervezas and acumulador_gaseosas > acumulador_limonadas):
            print("La gaseosa es la bebida mas vendida")
        else:
            print("La limonada es la bebida mas vendida")
else:
    print("No se ingresaron bebidas")

if (bandera_comidas == False):
    if (acumulador_papitas > acumulador_hamburguesas and acumulador_papitas > acumulador_rabas):
        print("Las papitas es la comida mas vendida")
    else:
        if (acumulador_hamburguesas > acumulador_papitas and acumulador_hamburguesas > acumulador_rabas):
            print("La hamburguesa es la comida mas vendida")
        else:
            print("Las rabas es la comida mas vendida")
else:
    print("No se ingresó comida")
# b.	El promedio de clientes que ordena solamente bebida.

# c.	Calcular la recaudación bruta y recaudación neta del local.
recaudacion_bruta = acumulador_precio_cerveza + acumulador_precio_gaseosa + acumulador_precio_limonada + acumulador_precio_hamburguesa + acumulador_precio_papitas + acumulador_precio_rabas
print("La recaudacion bruta del local es: ",recaudacion_bruta,"$")
# Falta calcular la recaudacion neta del local

# d.	Cuánta gente ordenó comida pero no bebida.
