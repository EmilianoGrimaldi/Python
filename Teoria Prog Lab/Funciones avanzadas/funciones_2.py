def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def operacion(operando_a, operando_b, calculo):
    return calculo(operando_a,operando_b)

def calcular_superficie(base, altura):
    return base * altura


# print(operacion(10, 2, sumar))
# print(operacion(10, 2, restar))
# print(operacion(10, 2, multiplicar))
# print(operacion(10, 2, dividir))
print(operacion(10, 2, calcular_superficie))