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


def sub_menu(lista):
    personajes_femeninos = []
    personajes_masculinos = []
    personajes_color_ojos = []
    # personajes_ojos_brown = []
    # personajes_ojos_blue = []
    # personajes_ojos_green = []
    # personajes_ojos_yellow_without_irises = []
    # personajes_ojos_hazel = []
    # personajes_ojos_yellow = []
    # personajes_ojos_silver = []
    # personajes_ojos_red = []
    
    for personaje in lista:
        if personaje['genero'] == "M":
            personajes_masculinos.append(personaje)
    for personaje in lista:
        if personaje['genero'] == "F":
            personajes_femeninos.append(personaje)
    for personaje in lista:
        personajes_color_ojos.append(personaje["color_ojos"])

    while True:
        os.system("cls")
        encabezado("########                STARK INDUSTRIES SUB MENU                ########\n\n1 --> Imprimir nombre de todos los superheroes masculinos\n2 --> Imprimir nombre de todos los superheroes femeninos\n3 --> El superhéroe más alto de género masculino\n4 --> El superhéroe más alto de género femenino\n5 --> El superhéroe más bajo de género masculino\n6 --> El superhéroe más bajo de género femenino\n7 --> Altura promedio de los superhéroes de género masculino\n8 --> Altura promedio de los superhéroes de género femenino\n9 --> Nombre del superhéroe más alto de género M\n10 --> Nombre del superhéroe más alto de género F\n11 --> Nombre del superhéroe más bajo de género M\n12 --> Nombre del superhéroe más bajo de género F\n13 --> Cuántos superhéroes tienen cada tipo de color de ojos\n14 --> Cuántos superhéroes tienen cada tipo de color de pelo\n15 --> Cuántos superhéroes tienen cada tipo de inteligencia\n16 --> Listar todos los superhéroes agrupados por color de ojos\n17 --> Listar todos los superhéroes agrupados por color de pelo\n18 --> Listar todos los superhéroes agrupados por tipo de inteligencia\n19 --> Volver\n\n")
        opcion = pedir_entero_rango("Ingrese una opcion\n", 1, 19)

        match opcion:
            case 1:
                encabezado(
                    "########                NOMBRE DE CADA SUPERHEROE MASCULINO               ########\n")
                for personaje in lista:
                    if personaje['genero'] == "M":
                        print("\t\t\t|{:^30}|".format(personaje['nombre']))
            case 2:
                encabezado(
                    "########                NOMBRE DE CADA SUPERHEROE FEMENINO              ########\n")
                for personaje in lista:
                    if personaje['genero'] == "F":
                        print("\t\t\t|{:^30}|".format(personaje['nombre']))
            case 3:
                encabezado(
                    "########                SUPERHEROE MAS ALTO MASCULINO               ########\n")
                mas_alto = buscar_maximo(personajes_masculinos, "altura")
                mas_altos = guardar_los_maximos(
                    personajes_masculinos, mas_alto, "altura")
                imprimir_lista(mas_altos)

            case 4:
                encabezado(
                    "########                SUPERHEROE MAS ALTO FEMENINO               ########\n")
                mas_alta = buscar_maximo(personajes_femeninos, "altura")
                mas_altas = guardar_los_maximos(
                    personajes_femeninos, mas_alta, "altura")
                imprimir_lista(mas_altas)

            case 5:
                encabezado(
                    "########                SUPERHEROE MAS BAJO MASCULINO               ########\n")
                mas_bajo = buscar_minimo(personajes_masculinos, "altura")
                mas_bajos = guardar_los_minimos(
                    personajes_masculinos, mas_bajo, "altura")
                imprimir_lista(mas_bajos)
            case 6:
                encabezado(
                    "########                SUPERHEROE MAS BAJO FEMENINO               ########\n")
                mas_baja = buscar_minimo(personajes_femeninos, "altura")
                mas_bajas = guardar_los_minimos(
                    personajes_femeninos, mas_baja, "altura")
                imprimir_lista(mas_bajas)
            case 7:
                encabezado(
                    "########                ALTURA PROMEDIO MASCULINO               ########\n")
                acumulador_edad_masculino = acumular_total_altura(
                    personajes_masculinos)
                promedio_masculino = sacar_promedio(
                    acumulador_edad_masculino, len(personajes_masculinos))
                mostrar_promedio(promedio_masculino)
            case 8:
                encabezado(
                    "########                ALTURA PROMEDIO FEMENINO               ########\n")
                acumulador_edad_femenino = acumular_total_altura(
                    personajes_femeninos)
                promedio_femenino = sacar_promedio(
                    acumulador_edad_femenino, len(personajes_femeninos))
                mostrar_promedio(promedio_femenino)
            case 9:
                encabezado(
                    "########                NOMBRE DE SUPERHEROE MAS ALTO MASCULINO               ########\n")
                mas_alto = buscar_maximo(personajes_masculinos, "altura")
                mas_altos = guardar_los_maximos(
                    personajes_masculinos, mas_alto, "altura")
                imprimir_lista_por_campo(mas_altos, "nombre")
            case 10:
                encabezado(
                    "########                NOMBRE DE SUPERHEROE MAS ALTO FEMENINO               ########\n")
                mas_alta = buscar_maximo(personajes_femeninos, "altura")
                mas_altas = guardar_los_maximos(
                    personajes_femeninos, mas_alta, "altura")
                imprimir_lista_por_campo(mas_altas, "nombre")
            case 11:
                encabezado(
                    "########                NOMBRE DE SUPERHEROE MAS BAJO               ########\n")
                mas_bajo = buscar_minimo(personajes_masculinos, "altura")
                mas_bajos = guardar_los_minimos(
                    personajes_masculinos, mas_bajo, "altura")
                imprimir_lista_por_campo(mas_bajos, "nombre")
            case 12:
                encabezado(
                    "########                NOMBRE DE LA SUPERHEROE MAS BAJA             ########\n")
                mas_baja = buscar_minimo(personajes_femeninos, "altura")
                mas_bajas = guardar_los_minimos(
                    personajes_femeninos, mas_baja, "altura")
                imprimir_lista_por_campo(mas_bajas, "nombre")
            case 13:
                color_ojos = set(personajes_color_ojos)
                for color in color_ojos:
                    print(color)
            case 14:
                pass
            case 15:
                pass
            case 16:
                pass
            case 17:
                pass
            case 18:
                pass
            case 19:
                print("Volviendo al menu principal")
                break

        os.system("pause")


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
            sub_menu(lista)
