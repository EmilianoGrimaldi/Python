# Ejercicio 04
# La división de alimentos está trabajando en un pequeño software para cargar las
# compras de ingredientes para la cocina de Industrias Wayne.
# Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
# para preparar comida al por mayor. En total, sabemos que se realizarán 15 compras
# de ingredientes.
# Se registra por cada compra:
# 1. PESO: (entre 10 y 100 kilos)
# 2. PRECIO POR KILO: (mayor a 0 [cero]).
# 3. TIPO VARIEDAD: (vegetal, animal, mezcla).

# Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de
# descuento sobre el precio bruto, o si compro más de 300 kilos en total, tengo un 25%
# de descuento sobre el precio bruto.

# Se desea saber:
# A. El importe total a pagar, BRUTO sin descuento. HECHO
# B. El importe total a pagar con descuento (Solo si corresponde). HECHO
# C. Informar el tipo de alimento más caro. HECHO
# D. El promedio de precio por kilo en total.
descuento = 0
acumulador_de_peso = 0
acumulador_precio_bruto = 0
acumulador_precio_por_kilo = 0
bandera_tipo_mas_caro = True
precio_tipo_mas_caro = 0
tipo_mas_caro = ""

for i in range(1,16):
    #INGRESO DE DATOS PESO DE ALIMENTO CON VALIDACION EN CADA CASO CON TRY EXCEPT PARA VALIDAR TODO TIPO DE ERROR
    while True:
        try:
            peso_alimento = float(input("Ingresar peso [10 - 100]: "))
            if peso_alimento >= 10 and peso_alimento <= 100:
                break
            else:
                print("Error! Peso de alimento fuera de rango")
        except ValueError:
            print("Error! Intentaste ingresar una letra o palabra")
        
    while True:
        try:
            precio_por_kilo = float(input("Ingresar precio por kilo [Mayor a 0]: "))
            if precio_por_kilo > 0:
                break
            else:
                print("Error! Precio fuera de rango")
        except ValueError:
            print("Error! Intentaste ingresar una letra o palabra")

    while True:
        tipo_de_variedad = input("Ingresar tipo de variedad [Vegetal - Animal - Mezcla]: ")
        if tipo_de_variedad == "Vegetal" or tipo_de_variedad == "Animal" or tipo_de_variedad == "Mezcla":
            break
        else:
            print("Error! Tipo de variedad incorrecto")
    #BUSCAR EL TIPO MAS CARO
    if bandera_tipo_mas_caro == True or precio_por_kilo > precio_tipo_mas_caro:
        precio_tipo_mas_caro = precio_por_kilo
        tipo_mas_caro = tipo_de_variedad
        bandera_tipo_mas_caro = False

    #ACUMULADORES
    acumulador_de_peso += peso_alimento
    acumulador_precio_por_kilo += precio_por_kilo

    #CALCULOS
    total_compra = precio_por_kilo * peso_alimento
    acumulador_precio_bruto += total_compra

#Calcular promedio de precio por kilo
promedio_precio_por_kilo = acumulador_precio_por_kilo / 15

#APLICAR DESCUENTO SI CORRESPONDE
if acumulador_de_peso > 300:
    descuento = 25
else:
    if acumulador_de_peso > 100:
        descuento = 15
#Muestro los resultados en pantalla
print(f"El importe bruto es ${acumulador_precio_bruto}")

if descuento > 0:
    #calculo del descuento
    calculo_descuento = acumulador_precio_bruto * descuento / 100
    precio_final_con_descuento = acumulador_precio_bruto - calculo_descuento
    #Mostrar en pantalla
    print(f"El descuento es del {descuento}%")
    print(f"El importe con descuento es ${precio_final_con_descuento}")

print(f"El tipo de alimento mas caro es: {tipo_mas_caro}")
print(f"El promedio de precio por kilo es ${promedio_precio_por_kilo}")

