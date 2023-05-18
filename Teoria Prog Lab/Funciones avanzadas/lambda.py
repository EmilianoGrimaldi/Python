def operacion(operando_a, operando_b, calculo):
    return calculo(operando_a,operando_b)

def calcular_superficie1(base, altura):
    return base * altura

calcular_superficie2 = lambda base, altura: base * altura

print(operacion(5, 6, calcular_superficie2))