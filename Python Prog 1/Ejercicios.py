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

#DEFINO LOS PRECIOS DE LOS PRODUCTOS
precio_cerveza = 500
precio_limonada = 300
precio_gaseosa = 250
precio_papitas = 1200
precio_hamburguesa = 2000
precio_rabas = 1800

#VARIABLES ESTADISTICAS
bebidas_vendidas = 0
comidas_vendidas = 0
cervezas_vendidas = 0
limonadas_vendidas = 0
gaseosas_vendidas = 0
papitas_vendidas = 0
hamburguesas_vendidas = 0
rabas_vendidas = 0
recaudacion_bruta = 0
contador_de_clientes = 0
solo_bebidas = 0
solo_comida = 0
promedio_de_bebidas = None
recaudacion_bruta = 0
recaudacion_neta = 0
promedio_de_comida = None

while (continuar == 1):

    #INGRESO DE DATOS
    nombre_cliente = input("Ingresar el nombre: ")
    #PIDO LOS DATOS AL USUARIO Y VALIDO QUE EL INGRESO DE DATOS SEA EL CORRECTO 
    tipo_de_bebida = input("Ingresar el tipo de bebida[cerveza - limonada - gaseosa - nada]: ")
    while (tipo_de_bebida != "cerveza" and tipo_de_bebida != "limonada" and tipo_de_bebida != "gaseosa" and tipo_de_bebida != "nada"):
        tipo_de_bebida = input("Reingresar el tipo de bebida[cerveza - limonada - gaseosa - nada]: ")

    tipo_de_comida = input("Ingresar el tipo de comida[papitas - hamburguesa - rabas - nada]: ")
    while (tipo_de_comida != "papitas" and tipo_de_comida != "hamburguesa" and tipo_de_comida != "rabas" and tipo_de_comida != "nada"):
        tipo_de_comida = input("Reingresar el tipo de comida[papitas - hamburguesa - rabas - nada]: ")

    #UTILIZO UN MATCH PARA LLEVAR UN CONTROL DEL PEDIDO SEGUN LO PEDIDO POR EL CLIENTE
    match(tipo_de_bebida):
        case "cerveza":
            bebidas_vendidas += 1
            cervezas_vendidas += 1
            recaudacion_bruta += precio_cerveza
        case "limonada":
            bebidas_vendidas += 1
            limonadas_vendidas += 1
            recaudacion_bruta += precio_limonada
        case "gaseosa":
            bebidas_vendidas += 1
            gaseosas_vendidas += 1
            recaudacion_bruta += precio_gaseosa

    match(tipo_de_comida):
        case "papitas":
            comidas_vendidas += 1
            papitas_vendidas += 1
            recaudacion_bruta += precio_papitas
        case "hamburguesa":
            comidas_vendidas += 1
            hamburguesas_vendidas += 1
            recaudacion_bruta += precio_hamburguesa
        case "rabas":
            comidas_vendidas += 1
            rabas_vendidas += 1
            recaudacion_bruta += precio_rabas

    #CONTROLAR SI LOS CLIENTES PIDIERON SOLO COMIDA O SOLO BEBIDA
    if(bebidas_vendidas > 0 and tipo_de_comida == "nada"):
        solo_bebidas += 1

    if(comidas_vendidas > 0 and tipo_de_bebida == "nada"):
        solo_comida += 1

    contador_de_clientes += 1
    continuar = int(input("Para continuar presione 1: "))

promedio_de_bebidas = solo_bebidas / contador_de_clientes
recaudacion_neta = recaudacion_bruta #NO SE ESPECIFICA NINGUN DESCUENTO O COSTO ADICIONAL EN EL EJERCICIO POR LO TANTO LA RECAUDACION NETA ES IGUAL A LA BRUTA
promedio_de_comida = solo_comida / contador_de_clientes

# a.	El tipo de comida más vendido y bebida más vendida si la hay.
if (bebidas_vendidas < 0):
    if (cervezas_vendidas > gaseosas_vendidas and cervezas_vendidas > limonadas_vendidas):
        print("La cerveza es la bebida mas vendida")
    else:
        if (gaseosas_vendidas > cervezas_vendidas and gaseosas_vendidas > limonadas_vendidas):
            print("La gaseosa es la bebida mas vendida")
        else:
            print("La limonada es la bebida mas vendida")
else:
    print("No se ingresaron bebidas")

if (comidas_vendidas < 0):
    if (papitas_vendidas > hamburguesas_vendidas and papitas_vendidas > rabas_vendidas):
        print("Las papitas es la comida mas vendida")
    else:
        if (hamburguesas_vendidas > papitas_vendidas and hamburguesas_vendidas > rabas_vendidas):
            print("La hamburguesa es la comida mas vendida")
        else:
            print("Las rabas es la comida mas vendida")
else:
    print("No se ingresó comida")

# b.	El promedio de clientes que ordena solamente bebida.
print("El promedio de clientes que ordenan solo bebida es: ", promedio_de_bebidas)
# c.	Calcular la recaudación bruta y recaudación neta del local.
print("La recaudacion bruta del local es: $",recaudacion_bruta)
print("La recaudacion neta del local es: $",recaudacion_neta)
# d.	Cuánta gente ordenó comida pero no bebida.
print("El promedio de clientes que ordenan solo comida es: ", promedio_de_comida)

