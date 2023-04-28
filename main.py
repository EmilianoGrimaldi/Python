def calcular_dolares_pesos(dolares:int,precio_dolar:int)->float:
    calculo = (dolares * precio_dolar) / 1
    return calculo

def calcular_pesos_dolares(pesos:int,precio_dolar:int)->float:
    calculo = (pesos * 1) / precio_dolar
    return calculo

print(calcular_dolares_pesos(22000000,467))
print(calcular_pesos_dolares(400000000,467))
