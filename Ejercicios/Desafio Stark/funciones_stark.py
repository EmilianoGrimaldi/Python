from mis_funciones import *


def cambiar_tipo_str_float(lista, campo):
    for personaje in lista:
        if type(personaje[campo]) == str:
            personaje[campo] = float(personaje[campo])


def encabezado(mensaje):
    print(mensaje)


def encabezado_menu():
    encabezado("########                STARK INDUSTRIES                 ########\n\n1 --> Imprimir nombre de todos los superheroes\n2 --> Imprimir nombre y altura de los superheroes\n3 --> El superheroe mas alto\n4 --> El superheroe mas bajo\n5 --> Altura promedio de los superheroes\n6 --> Nombre del superheroe mas alto\n7 --> Nombre del superheroe mas bajo\n8 --> Superheroe mas pesado\n9 --> Superheroe menos pesado\n10 --> Sub menu\n11 --> Salir\n\n")


def imprimir_lista_por_campo(lista, campo):
    for i in lista:
        print(i[campo])


def imprimir_lista(lista):
    for personaje in lista:
        print(f"{personaje}")


def imprimir_lista_nombres(lista):
    encabezado("\tLISTA DE NOMBRES DE SUPERHEROES\n")
    imprimir_lista_por_campo(lista, "nombre")


def imprimir_nombre_altura(lista):
    encabezado("|\tSUPERHEROE\t   |\t   ALTURA\t|\n")
    for personaje in lista:
        print(f"|{personaje['nombre']:^26}|{personaje['altura']:^20}|")


def acumular_total_altura(lista):
    acumulador = 0
    for personaje in lista:
        acumulador += personaje["altura"]
    return acumulador


def sacar_promedio(suma_total, cantidad_total):
    promedio = suma_total / cantidad_total
    return promedio


def mostrar_promedio(promedio):
    print("{:.2f}".format(promedio))


def cambiar_tipo_campo_dic(lista, tipo_actual, tipo_nuevo, clave_a_cambiar):
    for i in lista:
        if type(i[clave_a_cambiar]) == tipo_actual:
            i[clave_a_cambiar] = tipo_nuevo(i[clave_a_cambiar])


def calcular_minimo_campo_dic(lista, campo):
    flag = True
    for i in lista:
        if flag or i[campo] <= minimo:
            minimo = i[campo]
            flag = False
    return minimo


def buscar_maximo(lista, campo):
    flag_max = True
    for personaje in lista:
        if flag_max or personaje[campo] >= maximo:
            maximo = personaje[campo]
            flag_max = False

    return maximo


def buscar_minimo(lista, campo):
    flag_min = True
    for personaje in lista:
        if flag_min or personaje[campo] <= minimo:
            minimo = personaje[campo]
            flag_min = False

    return minimo


def guardar_los_maximos(lista, mas_alto, campo):
    aux_maximos = []
    for personaje in lista:
        if personaje[campo] == mas_alto:
            aux_maximos.append(personaje)

    return aux_maximos


def guardar_los_minimos(lista, mas_bajo, campo):
    aux_minimos = []
    for personaje in lista:
        if personaje[campo] == mas_bajo:
            aux_minimos.append(personaje)

    return aux_minimos


def buscar_mas_alto_y_mostrarlo(lista):
    encabezado("\tSUPERHEROES MAS ALTOS\n")
    # busco el personaje mas alto
    altura_maxima = buscar_maximo(lista, "altura")
    # verifico si hay mas de uno con la misma altura maxima y lo guardo en una lista aparte
    lista_mas_altos = guardar_los_maximos(lista, altura_maxima, "altura")
    # imprimo los mas altos sea uno o mas
    imprimir_lista(lista_mas_altos)


def buscar_mas_bajo_y_mostrarlo(lista):
    encabezado("\tSUPERHEROES MAS BAJOS\n")
    # busco el personaje mas bajo
    altura_minima = buscar_minimo(lista, "altura")
    # verifico si hay mas de uno con la misma altura minima y lo guardo en una lista aparte
    lista_mas_bajos = guardar_los_minimos(lista, altura_minima, "altura")
    # imprimo los mas bajos sea uno o mas
    imprimir_lista(lista_mas_bajos)


def calcular_altura_promedio_mostrar(lista):
    encabezado("\tALTURA PROMEDIO DE LOS SUPERHEROES\n")
    altura_total = acumular_total_altura(lista)
    promedio_altura = sacar_promedio(altura_total, len(lista))
    mostrar_promedio(promedio_altura)


def mostrar_nombre_mas_alto(lista):
    encabezado("\tNOMBRE DE SUPERHEROES MAS ALTOS\n")
    altura_maxima = buscar_maximo(lista, "altura")
    lista_aux = guardar_los_maximos(lista, altura_maxima, "altura")
    imprimir_lista_por_campo(lista_aux, "nombre")


def mostrar_nombre_mas_bajo(lista):
    encabezado("\tNOMBRE DE SUPERHEROES MAS BAJOS\n")
    altura_minima = buscar_minimo(lista, "altura")
    lista_aux = guardar_los_minimos(lista, altura_minima, "altura")
    imprimir_lista_por_campo(lista_aux, "nombre")


def buscar_maximo_peso_mostrar(lista):
    encabezado("\tSUPERHEROES MAS PESADOS\n")
    peso_maximo = buscar_maximo(lista, "peso")
    lista_mas_pesados = guardar_los_maximos(lista, peso_maximo, "peso")
    imprimir_lista(lista_mas_pesados)


def buscar_minimo_peso_mostrar(lista):
    encabezado("\tSUPERHEROES MENOS PESADOS\n")
    peso_minimo = buscar_minimo(lista, "peso")
    lista_menos_pesados = guardar_los_minimos(lista, peso_minimo, "peso")
    imprimir_lista(lista_menos_pesados)


def menu_personajes(lista, opcion):
    # CONVIERTO TODAS LAS ALTURAS QUE ESTAN EN STRING LAS PASO A FLOAT
    cambiar_tipo_str_float(lista, "altura")
    cambiar_tipo_str_float(lista, "peso")

    match opcion:
        case 1:
            imprimir_lista_nombres(lista)
        case 2:
            imprimir_nombre_altura(lista)
        case 3:
            buscar_mas_alto_y_mostrarlo(lista)
        case 4:
            buscar_mas_bajo_y_mostrarlo(lista)
        case 5:
            calcular_altura_promedio_mostrar(lista)
        case 6:
            mostrar_nombre_mas_alto(lista)
        case 7:
            mostrar_nombre_mas_bajo(lista)
        case 8:
            buscar_maximo_peso_mostrar(lista)
        case 9:
            buscar_minimo_peso_mostrar(lista)
        case 10:
            pass
            # sub_menu(lista)
