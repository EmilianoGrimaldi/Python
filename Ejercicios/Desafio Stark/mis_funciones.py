def acumular_total_campo_dic(lista, campo):
    acumulador = 0
    for i in lista:
        acumulador += i[campo]    
    return acumulador

def sacar_promedio(suma_total, cantidad_total):
    promedio = suma_total / cantidad_total
    return promedio

def cambiar_tipo_campo_dic(lista, tipo_actual, tipo_nuevo, clave_a_cambiar):
    for i in lista:
        if type(i[clave_a_cambiar]) == tipo_actual:
            i[clave_a_cambiar] = tipo_nuevo(i[clave_a_cambiar])

def imprimir_campo_dic(lista,campo):
    for i in lista:
        print(i[campo])

def calcular_maximo_campo_dic(lista, campo):
    flag = True
    for i in lista:
        if flag or i[campo] >= maximo:
            maximo = i[campo]
            flag = False
    return maximo

def calcular_minimo_campo_dic(lista, campo):
    flag = True
    for i in lista:
        if flag or i[campo] <= minimo:
            minimo = i[campo]
            flag = False
    return minimo

def agrupar_maximos_minimos(lista, campo, max_o_min):
    aux = []
    for i in lista:
        if i[campo] == max_o_min:
            aux.append(i)
    return aux

    