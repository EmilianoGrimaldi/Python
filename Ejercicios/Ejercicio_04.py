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
# A. El importe total a pagar, BRUTO sin descuento.
# B. El importe total a pagar con descuento (Solo si corresponde).
# C. Informar el tipo de alimento más caro.
# D. El promedio de precio por kilo en total.

acumulador_de_peso = 0
precio_total_bruto = 0
descuento = 0
bandera_tipo_mas_caro = True

for i in range(1,3):
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
    
    precio_compra = peso_alimento * precio_por_kilo

    acumulador_de_peso += peso_alimento
    precio_total_bruto += precio_compra 

    if bandera_tipo_mas_caro == True:
        tipo_mas_caro = tipo_de_variedad
        precio_mas_caro = precio_por_kilo
        bandera_tipo_mas_caro = False
    else:
        if precio_por_kilo > precio_mas_caro:
            tipo_mas_caro = tipo_de_variedad
            precio_mas_caro = precio_por_kilo

# Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de
# descuento sobre el precio bruto, o si compro más de 300 kilos en total, tengo un 25%
# de descuento sobre el precio bruto.
if acumulador_de_peso >= 100:
    descuento = 15

if acumulador_de_peso > 300:
    descuento = 25



