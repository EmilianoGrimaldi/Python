from mis_funciones import *

def imprimir_dic_completo(lista):
    for item in lista:
        for clave,valor in item.items():
            print("{} --> {}".format(clave,valor))

def menu_01():
        print("""
 ------------->                STARK INDUSTRIES SUB MENU                <-------------""")
        print("""
 1  --> Imprimir nombre de todos los superheroes M
 2  --> Imprimir nombre de todos los superheroes F
 3  --> El superhéroe más alto de género M
 4  --> El superhéroe más alto de género F
 5  --> El superhéroe más bajo de género M
 6  --> El superhéroe más bajo de género F
 7  --> Altura promedio de los superhéroes de género M
 8  --> Altura promedio de los superhéroes de género F
 9  --> Nombre del superhéroe más alto de género M
 10 --> Nombre del superhéroe más alto de género F
 11 --> Nombre del superhéroe más bajo de género M
 12 --> Nombre del superhéroe más bajo de género F
 13 --> Cuántos superhéroes tienen cada tipo de color de ojos
 14 --> Cuántos superhéroes tienen cada tipo de color de pelo
 15 --> Cuántos superhéroes tienen cada tipo de inteligencia
 16 --> Listar todos los superhéroes agrupados por color de ojos
 17 --> Listar todos los superhéroes agrupados por color de pelo
 18 --> Listar todos los superhéroes agrupados por tipo de inteligencia
 19 --> Volver\n\n""")
        opcion = pedir_entero_rango("Ingrese una opcion\n", 1, 19)
        return opcion


def menu_desafio_01(lista):
    personajes_masculinos = []
    personajes_femeninos = []

    for personaje in lista:
            if personaje['genero'] == "M":
                personajes_masculinos.append(personaje)
    for personaje in lista:
            if personaje['genero'] == "F":
                personajes_femeninos.append(personaje)
    for personaje in lista:
        if personaje['color_pelo'] == "":
            personaje['color_pelo'] = "No tiene"
    for personaje in lista:
        if personaje['inteligencia'] == "":
            personaje['inteligencia'] = "No tiene"

    while True:
        os.system("cls")
        match menu_01():   
            case 1:
                print(
                        "########                NOMBRE DE CADA SUPERHEROE MASCULINO               ########\n")
                for personaje in lista:
                        if personaje['genero'] == "M":
                                print("\t\t\t|{:^30}|".format(personaje['nombre']))
            case 2:
                print(
                        "########                NOMBRE DE CADA SUPERHEROE FEMENINO              ########\n")
                for personaje in lista:
                        if personaje['genero'] == "F":
                                print("\t\t\t|{:^30}|".format(personaje['nombre']))
            case 3:
                print(
                        "########                SUPERHEROE MAS ALTO MASCULINO               ########\n")
                
                mas_alto = buscar_maximo(personajes_masculinos, "altura")
                mas_altos = guardar_los_maximos(
                        personajes_masculinos, mas_alto, "altura")
                imprimir_dic_completo(mas_altos)
            case 4:
                print(
                        "########                SUPERHEROE MAS ALTO FEMENINO               ########\n")
                mas_alta = buscar_maximo(personajes_femeninos, "altura")
                mas_altas = guardar_los_maximos(
                        personajes_femeninos, mas_alta, "altura")
                imprimir_dic_completo(mas_altas)

            case 5:
                print(
                        "########                SUPERHEROE MAS BAJO MASCULINO               ########\n")
                mas_bajo = buscar_minimo(personajes_masculinos, "altura")
                mas_bajos = guardar_los_minimos(
                        personajes_masculinos, mas_bajo, "altura")
                imprimir_dic_completo(mas_bajos)
                
            case 6:
                print(
                        "########                SUPERHEROE MAS BAJO FEMENINO               ########\n")
                mas_baja = buscar_minimo(personajes_femeninos, "altura")
                mas_bajas = guardar_los_minimos(
                        personajes_femeninos, mas_baja, "altura")
                imprimir_dic_completo(mas_bajas)
                
            case 7:
                print(
                        "########                ALTURA PROMEDIO MASCULINO               ########\n")
                acumulador_edad_masculino = acumular_total_altura(
                        personajes_masculinos)
                promedio_masculino = sacar_promedio(
                        acumulador_edad_masculino, len(personajes_masculinos))
                mostrar_promedio(promedio_masculino)
            case 8:
                print(
                        "########                ALTURA PROMEDIO FEMENINO               ########\n")
                acumulador_edad_femenino = acumular_total_altura(
                        personajes_femeninos)
                promedio_femenino = sacar_promedio(
                        acumulador_edad_femenino, len(personajes_femeninos))
                mostrar_promedio(promedio_femenino)
            case 9:
                print(
                        "########                NOMBRE DE SUPERHEROE MAS ALTO MASCULINO               ########\n")
                mas_alto = buscar_maximo(personajes_masculinos, "altura")
                mas_altos = guardar_los_maximos(
                        personajes_masculinos, mas_alto, "altura")
                imprimir_lista_por_campo(mas_altos, "nombre")
            case 10:
                print(
                        "########                NOMBRE DE SUPERHEROE MAS ALTO FEMENINO               ########\n")
                mas_alta = buscar_maximo(personajes_femeninos, "altura")
                mas_altas = guardar_los_maximos(
                        personajes_femeninos, mas_alta, "altura")
                imprimir_lista_por_campo(mas_altas, "nombre")
            case 11:
                print(
                        "########                NOMBRE DE SUPERHEROE MAS BAJO               ########\n")
                mas_bajo = buscar_minimo(personajes_masculinos, "altura")
                mas_bajos = guardar_los_minimos(
                        personajes_masculinos, mas_bajo, "altura")
                imprimir_lista_por_campo(mas_bajos, "nombre")
            case 12:
                print(
                        "########                NOMBRE DE LA SUPERHEROE MAS BAJA             ########\n")
                mas_baja = buscar_minimo(personajes_femeninos, "altura")
                mas_bajas = guardar_los_minimos(
                        personajes_femeninos, mas_baja, "altura")
                imprimir_lista_por_campo(mas_bajas, "nombre")
            case 13:
                print("########                CANTIDAD DE TIPOS DE COLOR DE OJOS             ########\n")
                color_ojos_cant = {}
                for personaje in lista:
                    color_ojos = personaje['color_ojos']
                    if color_ojos in color_ojos_cant:
                        color_ojos_cant[color_ojos] += 1
                    else:
                        color_ojos_cant[color_ojos] = 1
                
                print(" |           COLOR OJOS           |   CANTIDAD   |\n")
                for color,cantidad in color_ojos_cant.items():  
                    print(" |    {:28s}|{:^14}|".format(color,cantidad))
                     
            case 14:
                print("########                CANTIDAD DE TIPOS DE COLOR DE PELO             ########\n")
                color_pelo_cant = {}
                for personaje in lista:    
                    color_pelo = personaje['color_pelo']       
                    if color_pelo in color_pelo_cant:
                        color_pelo_cant[color_pelo] += 1
                    else:
                        color_pelo_cant[color_pelo] = 1
                 
                #items() retorna una lista de tuplas, donde cada tupla tiene dos elementos: el primero es la clave y el segundo es el valor asociado a esa clave.
                
                print(" |         COLOR PELO        |  CANTIDAD  |\n")
                for color,cantidad in color_pelo_cant.items():  
                    print(" |   {:24s}|{:^12}|".format(color,cantidad))
            case 15:
                print("########                CANTIDAD DE TIPOS DE INTELIGENCIA             ########\n")
                inteligencia_cant = {}
                for personaje in lista:    
                    inteligencia = personaje['inteligencia']

                    if inteligencia in inteligencia_cant:
                        inteligencia_cant[inteligencia] += 1
                    else:
                        inteligencia_cant[inteligencia] = 1
                 
                #items() retorna una lista de tuplas, donde cada tupla tiene dos elementos: el primero es la clave y el segundo es el valor asociado a esa clave.
                
                print(" |          INTELIGENCIA        |  CANTIDAD  |\n")
                for inteligencia,cantidad in inteligencia_cant.items():  
                    print(" |    {:26s}|{:^12}|".format(inteligencia,cantidad))
            case 16:
                print("########                LISTA SUPERHEROES POR COLOR DE OJOS             ########\n")
                dict_color_ojos = {}
                for heroe in lista:    
                    ojos_color = heroe["color_ojos"]
                    if  ojos_color not in dict_color_ojos:
                        dict_color_ojos[ojos_color] = [] 
                    dict_color_ojos[ojos_color].append(heroe['nombre'])    
                
                for color, heroes in dict_color_ojos.items():
                    print("{:15s}".format(color))
                    for heroe in heroes:
                        print(" --> {}".format(heroe))
            case 17:
                print("########                LISTA SUPERHEROES POR COLOR DE PELO             ########\n")
                dict_color_pelo = {}
                for heroe in lista:    
                    pelo_color = heroe["color_pelo"]

                    if  pelo_color not in dict_color_pelo:
                        dict_color_pelo[pelo_color] = [] 
                    dict_color_pelo[pelo_color].append(heroe['nombre'])    
                
                for color, heroes in dict_color_pelo.items():
                    print("{:15s}".format(color))
                    for heroe in heroes:
                        print(" --> {}".format(heroe))
            case 18:
                print("########                LISTA SUPERHEROES POR INTELIGENCIA             ########\n")
                dic_inteligencia = {}
                for personaje in lista:    
                    inteligencia = personaje['inteligencia']
                        
                    if inteligencia not in dic_inteligencia:
                        dic_inteligencia[inteligencia] = []
                    
                    dic_inteligencia[inteligencia].append(personaje['nombre'])

                for inteligencia, personajes in dic_inteligencia.items():
                    print("{:15s}".format(inteligencia))
                    for personaje in personajes:
                        print(" --> {}".format(personaje))

            case 19:
                print("Volviendo al menu principal")
                break
        os.system("pause")        

def cambiar_tipo_str_float(lista, campo):
    for personaje in lista:
        if type(personaje[campo]) == str:
            personaje[campo] = float(personaje[campo])

def menu():
    print("########                STARK INDUSTRIES                 ########\n\n1 --> Imprimir nombre de todos los superheroes\n2 --> Imprimir nombre y altura de los superheroes\n3 --> El superheroe mas alto\n4 --> El superheroe mas bajo\n5 --> Altura promedio de los superheroes\n6 --> Nombre del superheroe mas alto\n7 --> Nombre del superheroe mas bajo\n8 --> Superheroe mas pesado\n9 --> Superheroe menos pesado\n10 --> Sub menu\n11 --> Salir\n\n")
    opcion = pedir_entero_rango("Ingrese una opcion\n",1,11)
    return opcion


def imprimir_lista_por_campo(lista, campo):
    for i in lista:
        print(i[campo])


def imprimir_lista(lista):
    for personaje in lista:
        print(f"{personaje}")


def imprimir_lista_nombres(lista):
    print("\tLISTA DE NOMBRES DE SUPERHEROES\n")
    imprimir_lista_por_campo(lista, "nombre")


def imprimir_nombre_altura(lista):
    print("|\tSUPERHEROE\t   |\t   ALTURA\t|\n")
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
    print("\tSUPERHEROES MAS ALTOS\n")
    # busco el personaje mas alto
    altura_maxima = buscar_maximo(lista, "altura")
    # verifico si hay mas de uno con la misma altura maxima y lo guardo en una lista aparte
    lista_mas_altos = guardar_los_maximos(lista, altura_maxima, "altura")
    # imprimo los mas altos sea uno o mas
    imprimir_lista(lista_mas_altos)


def buscar_mas_bajo_y_mostrarlo(lista):
    print("\tSUPERHEROES MAS BAJOS\n")
    # busco el personaje mas bajo
    altura_minima = buscar_minimo(lista, "altura")
    # verifico si hay mas de uno con la misma altura minima y lo guardo en una lista aparte
    lista_mas_bajos = guardar_los_minimos(lista, altura_minima, "altura")
    # imprimo los mas bajos sea uno o mas
    imprimir_lista(lista_mas_bajos)


def calcular_altura_promedio_mostrar(lista):
    print("\tALTURA PROMEDIO DE LOS SUPERHEROES\n")
    altura_total = acumular_total_altura(lista)
    promedio_altura = sacar_promedio(altura_total, len(lista))
    mostrar_promedio(promedio_altura)


def mostrar_nombre_mas_alto(lista):
    print("\tNOMBRE DE SUPERHEROES MAS ALTOS\n")
    altura_maxima = buscar_maximo(lista, "altura")
    lista_aux = guardar_los_maximos(lista, altura_maxima, "altura")
    imprimir_lista_por_campo(lista_aux, "nombre")


def mostrar_nombre_mas_bajo(lista):
    print("\tNOMBRE DE SUPERHEROES MAS BAJOS\n")
    altura_minima = buscar_minimo(lista, "altura")
    lista_aux = guardar_los_minimos(lista, altura_minima, "altura")
    imprimir_lista_por_campo(lista_aux, "nombre")


def buscar_maximo_peso_mostrar(lista):
    print("\tSUPERHEROES MAS PESADOS\n")
    peso_maximo = buscar_maximo(lista, "peso")
    lista_mas_pesados = guardar_los_maximos(lista, peso_maximo, "peso")
    imprimir_lista(lista_mas_pesados)


def buscar_minimo_peso_mostrar(lista):
    print("\tSUPERHEROES MENOS PESADOS\n")
    peso_minimo = buscar_minimo(lista, "peso")
    lista_menos_pesados = guardar_los_minimos(lista, peso_minimo, "peso")
    imprimir_lista(lista_menos_pesados)


def menu_personajes(lista):
    # CONVIERTO TODAS LAS ALTURAS QUE ESTAN EN STRING LAS PASO A FLOAT
    cambiar_tipo_str_float(lista, "altura")
    cambiar_tipo_str_float(lista, "peso")
    
    while True:
        os.system("cls")
        match menu():
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
                menu_desafio_01(lista)
            case 11:
                confirmacion = input("Seguro que quiere salir? [n --> para continuar] [cualquier tecla para salir]\n").lower()
                if confirmacion != "n":
                    break  
        os.system("pause")

