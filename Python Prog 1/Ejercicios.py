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



nombre_cliente = input("Ingresar el nombre: ")

tipo_de_bebida = input("Ingresar el tipo de bebida[cerveza - limonada - gaseosa]: ")
while(tipo_de_bebida != "cerveza" and tipo_de_bebida != "limonada" and tipo_de_bebida != "gaseosa"):
    tipo_de_bebida = input("Ingresar el tipo de bebida[cerveza - limonada - gaseosa]: ")

tipo_de_comida = input("Ingresar el tipo de comida[papitas - hamburguesa - rabas]: ")
while(tipo_de_comida != "papitas" and tipo_de_comida != "hamburguesa" and tipo_de_comida != "rabas"):
    tipo_de_comida = input("Ingresar el tipo de comida[papitas - hamburguesa - rabas]: ")

acumulador_bebida = 0
acumulador_comida = 0
match(tipo_de_bebida):
    case "cerveza":
        acumulador_bebida += 1
    case "limonada":
        acumulador_bebida += 1
    case "gaseosa":
        acumulador_bebida += 1

match(tipo_de_comida):
    case "cerveza":
        acumulador_comida += 1
    case "limonada":
        acumulador_comida += 1
    case "gaseosa":
        acumulador_comida += 1