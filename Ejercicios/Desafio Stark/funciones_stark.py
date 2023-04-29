from mis_funciones import *

def encabezado_campos_heroes():
    print(" NOMBRE                  IDENTIDAD                        EMPRESA          ALTURA   PESO    GENERO    COLOR OJOS                COLOR PELO      FUERZA    INTELIGENCIA\n")

def imprimir_un_heroe(heroe):
    print(f" {heroe['nombre']:23s} {heroe['identidad']:32s} {heroe['empresa']:15s} {heroe['altura']:7}  {heroe['peso']:6}      {heroe['genero']:7s} {heroe['color_ojos']:26s} {heroe['color_pelo']:15s} {heroe['fuerza']:9s} {heroe['inteligencia']}")

def imprimir_heroes(lista):
    for heroe in lista:
        imprimir_un_heroe(heroe)
        
def imprimir_lista_por_campo(lista, campo):
    for i in lista:
        print(i[campo])

def imprimir_lista_nombres_heroes(lista):
    print("\t LISTA DE NOMBRES DE SUPERHEROES\n")
    print("        |       NOMBRES DE HEROES       |     \n")
    for heroe in lista:
        print("\t|\t{:24s}|".format(heroe["nombre"]))
    
def imprimir_nombre_altura_heroes(lista):
    print("\t     NOMBRES Y ALTURAS DE HEROES\n")
    print("|\t    HEROE\t   |\t   ALTURA\t|\n")
    for heroe in lista:
        print(f"|{heroe['nombre']:^26}|{heroe['altura']:^20}|")

def acumulador(lista, clave):
    acumulador = 0
    for item in lista:
        acumulador += item[clave]
    return acumulador

def sacar_promedio(total, cantidad):
    promedio = total / cantidad
    return promedio

def mostrar_promedio(promedio):
    print("{:.2f}".format(promedio))

def cambiar_tipo_campo_dic(lista, clave_a_cambiar, tipo_actual_clave, tipo_nuevo_clave):
    for item in lista:
        if type(item[clave_a_cambiar]) == tipo_actual_clave:
            item[clave_a_cambiar] = tipo_nuevo_clave(item[clave_a_cambiar])

def calcular_minimo_campo_dic(lista, campo):
    flag = True
    for item in lista:
        if flag or item[campo] <= minimo:
            minimo = item[campo]
            flag = False
    return minimo

def buscar_maximo(lista, campo):
    flag_max = True
    for item in lista:
        if flag_max or item[campo] >= maximo:
            maximo = item[campo]
            flag_max = False

    return maximo

def buscar_minimo(lista, campo):
    flag_min = True
    for item in lista:
        if flag_min or item[campo] <= minimo:
            minimo = item[campo]
            flag_min = False

    return minimo

def guardar_los_maximos(lista, campo):
    aux_maximos = []
    mas_alto = buscar_maximo(lista, campo)
    for item in lista:
        if item[campo] == mas_alto:
            aux_maximos.append(item)

    return aux_maximos

def guardar_los_minimos(lista, campo):
    aux_minimos = []
    mas_bajo = buscar_minimo(lista, campo)
    for item in lista:
        if item[campo] == mas_bajo:
            aux_minimos.append(item)

    return aux_minimos

def mostrar_heroe_mas_alto(lista):
    
    lista_mas_altos = guardar_los_maximos(lista, "altura")
    if len(lista_mas_altos) == 1:
        print("\t\t\t\t\t\t\t\tEL HEROE MAS ALTO\n")
        imprimir_un_heroe(lista_mas_altos[0])
    else:
        if len(lista_mas_altos) > 1:
            print("\t\t\t\t\t\t\t\tLOS HEROES MAS ALTOS\n")
            imprimir_heroes(lista_mas_altos)
    
def mostrar_heroe_mas_bajo(lista):
    lista_mas_bajos = guardar_los_minimos(lista, "altura")
    if len(lista_mas_bajos) == 1:
        print("\t\t\t\t\t\t\t\tEL HEROE MAS BAJO\n")
        imprimir_un_heroe(lista_mas_bajos[0])
    else:
        if len(lista_mas_bajos) > 1:
            print("\t\t\t\t\t\t\t\tLOS HEROES MAS BAJOS\n")
            imprimir_heroes(lista_mas_bajos)

def mostrar_promedio_alturas_heroes(lista):
    print("\t\t\t\t\t\t\t\tALTURA PROMEDIO DE LOS SUPERHEROES\n")
    altura_total = acumulador(lista,"altura")
    promedio_altura = sacar_promedio(altura_total, len(lista))
    print("La altura promedio de los heroes es {:.2f}".format(promedio_altura))

def mostrar_nombre_heroe_mas_alto(lista):
    
    lista_aux = guardar_los_maximos(lista, "altura")
    
    if len(lista_aux) == 1:
        print("\t\t\t\t\t\t\t\tNOMBRE DEL HEROE MAS ALTO\n")
        print(f"El heroe mas alto es {lista_aux[0]['nombre']}")
    else:
        if len(lista_aux) > 1:
            print("\t\t\t\t\t\t\t\tNOMBRES DE LOS HEROES MAS ALTOS\n")
            print("Los heroes mas altos son")
            imprimir_lista_por_campo(lista_aux,"nombre")

def mostrar_nombre_heroe_mas_bajo(lista):
    lista_mas_bajos = guardar_los_minimos(lista, "altura")
    
    if len(lista_mas_bajos) == 1:
        print("\t\t\t\t\t\t\t\tNOMBRE DE HEROE MAS BAJO\n")
        print("El heroe mas bajo es {}".format(lista_mas_bajos[0]["nombre"]))
    else:
        if len(lista_mas_bajos) > 1:
            print("\t\t\t\t\t\t\t\tNOMBRES DE LOS HEROES MAS BAJOS\n")
            print("Los heroes mas bajos son\n")
            imprimir_lista_por_campo(lista_mas_bajos,"nombre")

def mostrar_maximo_peso_heroe(lista):
    lista_mas_pesados = guardar_los_maximos(lista, "peso")
    if len(lista_mas_pesados) == 1:
        print("\t\t\t\t\t\t\t\tHEROE MAS PESADO\n")
        print("El heroe mas pesado es {}".format(lista_mas_pesados[0]["nombre"]))
    else:
        if len(lista_mas_pesados) > 1:
            print("\t\t\t\t\t\t\t\tHEROES MAS PESADOS\n")
            print("Los heroes mas pesados son\n")
            imprimir_lista_por_campo(lista_mas_pesados,"nombre")
                   
def mostrar_minimo_peso_heroe(lista):
    lista_menos_pesados = guardar_los_minimos(lista, "peso")
    if len(lista_menos_pesados) == 1:
        print("\t\t\t\t\t\t\t\tHEROE MENOS PESADO\n")
        print("El heroe menos pesado es {}".format(lista_menos_pesados[0]["nombre"]))
    else:
        if len(lista_menos_pesados) > 1:
            print("\t\t\t\t\t\t\t\tHEROES MENOS PESADOS\n")
            print("Los heroes menos pesados son\n")
            imprimir_lista_por_campo(lista_menos_pesados,"nombre")

def filtrar_heroes(lista:list, clave:str, valor:str)-> list:
    lista_filtrada = []
    for item in lista:
        if item[clave] == valor:
            lista_filtrada.append(item)
    return lista_filtrada

def listar_nombre_genero(lista:list, genero:str):
    heroes = filtrar_heroes(lista,"genero",genero)
    if genero == "M":
        print("\t\t\t\t\t     ########                NOMBRE DE CADA HEROE               ########\n")
        for heroe in heroes:
            print("\t\t\t\t\t\t\t\t|{:^30}|".format(heroe['nombre']))
    else:
        print("\t\t\t\t\t     ########                NOMBRE DE CADA HEROINA              ########\n")
        for heroe in heroes:
            print("\t\t\t\t\t\t\t\t|{:^30}|".format(heroe['nombre']))

def listar_mas_alto_genero(lista:list, genero:str):
    heroes = filtrar_heroes(lista,"genero",genero)
    mas_altos = guardar_los_maximos(heroes, "altura")
    
    if len(mas_altos) == 1:
        if genero == "M":
            print("\t\t\t\t\t\t\t########                HEROE MAS ALTO               ########\n")
            imprimir_heroes(mas_altos)
        else:
            print("\t\t\t\t\t\t\t########                HEROINA MAS ALTA               ########\n")
            imprimir_heroes(mas_altos)
    else:
        if len(mas_altos) > 1:
            if genero == "M":
                print("\t\t\t\t\t\t\t########                HEROES MAS ALTOS               ########\n")
                imprimir_heroes(mas_altos)
            else:
                print("\t\t\t\t\t\t\t########                HEROINAS MAS ALTAS               ########\n")
                imprimir_heroes(mas_altos)

def listar_mas_bajo_genero(lista:list, genero:str):
    heroes = filtrar_heroes(lista,"genero",genero)
    mas_bajos = guardar_los_minimos(heroes, "altura")
    if len(mas_bajos) == 1:
        if genero == "M":
            print("\t\t\t\t\t\t\t########                HEROE MAS BAJO               ########\n")
            imprimir_heroes(mas_bajos)
        else:
            print("\t\t\t\t\t\t\t########                HEROINA MAS BAJA               ########\n")
            imprimir_heroes(mas_bajos)
    else:
        if len(mas_bajos) > 1:
            if genero == "M":
                print("\t\t\t\t\t\t\t########                HEROES MAS BAJOS               ########\n")
                imprimir_heroes(mas_bajos)
            else:
                print("\t\t\t\t\t\t\t########                HEROINAS MAS BAJAS               ########\n")
                imprimir_heroes(mas_bajos)

def promediar_altura_genero(lista:list,genero:str):
    heroes = filtrar_heroes(lista,"genero",genero)
    acumulador_edad = acumulador(heroes,"altura")
    promedio = sacar_promedio(acumulador_edad, len(heroes))
    if genero == "M":
        print("\t\t\t\t\t\t\t########                ALTURA PROMEDIO HEROES               ########\n")
        print("La altura promedio de los heroes es {:.2f}".format(promedio))
    else:
        print("\t\t\t\t\t\t\t########                ALTURA PROMEDIO HEROINAS               ########\n")
        print("La altura promedio de las heroinas es {:.2f}".format(promedio))


def nombrar_mayor_altura_genero(lista:list,genero:str):
    heroes = filtrar_heroes(lista,"genero",genero)
    lista_alturas = guardar_los_maximos(heroes, "altura")

    if len(lista_alturas) == 1:
        if genero == "M":
            print("\t\t\t\t\t\t\t########                NOMBRE DE HEROE MAS ALTO               ########\n")
            print("El heroe mas alto es {}".format(lista_alturas[0]["nombre"]))
        else:
            print("\t\t\t\t\t\t\t########                NOMBRE DE HEROINA MAS ALTA               ########\n")    
            print("La heroina mas alta es {}".format(lista_alturas[0]["nombre"]))
    else:
        if len(lista_alturas) > 1:
            if genero == "M":
                print("\t\t\t\t\t\t\t########                NOMBRES DE HEROES MAS ALTOS               ########\n")
                print("Los heroes mas altos son")
                imprimir_lista_por_campo(lista_alturas,"nombre")
            else:
                print("\t\t\t\t\t\t\t########                NOMBRES DE HEROINAS MAS ALTAS               ########\n")
                print("Las heroinas mas altas son")
                imprimir_lista_por_campo(lista_alturas,"nombre")

def nombrar_menor_altura_genero(lista:list,genero:str):

    heroes = filtrar_heroes(lista,"genero",genero)
    lista_alturas = guardar_los_minimos(heroes, "altura")

    if len(lista_alturas) == 1:
        if genero == "M":
            print("\t\t\t\t\t\t\t########                NOMBRE DE HEROE MAS BAJO               ########\n")
            print("El heroe mas bajo es {}".format(lista_alturas[0]["nombre"]))
        else:
            print("\t\t\t\t\t\t\t########                NOMBRE DE HEROINA MAS BAJA               ########\n")    
            print("La heroina mas baja es {}".format(lista_alturas[0]["nombre"]))
    else:
        if len(lista_alturas) > 1:
            if genero == "M":
                print("\t\t\t\t\t\t\t########                NOMBRES DE HEROES MAS BAJOS               ########\n")
                print("Los heroes mas bajos son")
                imprimir_lista_por_campo(lista_alturas,"nombre")
            else:
                print("\t\t\t\t\t\t\t########                NOMBRES DE HEROINAS MAS BAJAS               ########\n")
                print("Las heroinas mas bajas son")
                imprimir_lista_por_campo(lista_alturas,"nombre")

def contar_items_categoria(lista:list,clave:str)->dict:
    #Creo un dic vacio para ir guardando los items como clave y la cantidad como valor
    dic_aux = {}
    
    for item in lista:
        #Hago una busqueda y voy guardando el item en una var
        item_guardado = item[clave].capitalize() # Primer letra en mayuscula el resto minuscula
        #Pregunto si ese item existe dentro del diccionario
        if item_guardado in dic_aux:
            #si existe le sumo 1 al valor de ese item
            dic_aux[item_guardado] += 1
        else:
            #sino existe creo la clave de ese item y le asigno el valor 1 (para indicar que es el primer item)
            dic_aux[item_guardado] = 1
    
    return dic_aux

def listar_cantidad_color_ojos(lista:list)-> None:
    print("\t\t\t\t\t     ########                CANTIDAD DE TIPOS DE COLOR DE OJOS             ########\n")
    
    color_ojos = contar_items_categoria(lista,"color_ojos")  
    
    print("\t\t\t\t\t\t\t    |           COLOR OJOS           |   CANTIDAD   |\n")
    #items tranforma ese diccionario en una lista de tuplas clave : valor
    for color,cantidad in color_ojos.items():  
        print("\t\t\t\t\t\t\t    |\t {:28s}|\t    {:2d}\t    |".format(color,cantidad))
        
def listar_cantidad_color_pelo(lista:list)->None:
    print("\t\t\t\t\t ########                CANTIDAD DE TIPOS DE COLOR DE PELO             ########\n")
    color_pelo = contar_items_categoria(lista,"color_pelo")
    
    print("\t\t\t\t\t\t\t    |         COLOR PELO        |  CANTIDAD  |\n")
    for color,cantidad in color_pelo.items():  
        print("\t\t\t\t\t\t\t    |   {:24s}|{:^12}|".format(color,cantidad))
 
def listar_cantidad_tipo_inteligencia(lista:list)->None: 
    print("\t\t\t\t\t ########                CANTIDAD DE TIPOS DE INTELIGENCIA             ########\n")
    
    tipo_inteligencia = contar_items_categoria(lista,"inteligencia")
    
    print("\t\t\t\t\t\t\t    |          INTELIGENCIA        |  CANTIDAD  |\n")
    for inteligencia,cantidad in tipo_inteligencia.items():
        print("\t\t\t\t\t\t\t    |    {:26s}|\t {:2d}\t|".format(inteligencia,cantidad))

def inicializar_clave_vacia(lista:list,clave:str,cadena_inicializar:str)-> None:
    for heroe in lista:
        if heroe[clave] == "":
            heroe[clave] = cadena_inicializar

def filtrar_heroe_categoria(lista:list, clave:str)-> dict:
    dic = {}
    
    for item in lista:
        value = item[clave].capitalize()
        if value in dic:
            dic[value].append(item)
        else:
            dic[value] = [item]
            
    return dic

def mostrar_heroe_categoria(lista:list, diccionario:dict)-> None:
    for item, valores in diccionario.items():
        print(f"\n\t\t\t\t\t\t\t\t\t{item}\n")
        imprimir_heroes(valores)

def listar_heroes_por_color_ojos(lista:list)-> None:
    print("\t\t\t########                LISTA HEROES POR COLOR DE OJOS             ########\n")
    heroes_por_color_ojos = filtrar_heroe_categoria(lista,"color_ojos")
    mostrar_heroe_categoria(lista, heroes_por_color_ojos)

def listar_heroes_por_color_pelo(lista:list)-> None:
    print("\t\t\t########                LISTA HEROES POR COLOR DE PELO             ########\n")
    heroes_por_color_pelo = filtrar_heroe_categoria(lista,"color_pelo")
    mostrar_heroe_categoria(lista, heroes_por_color_pelo)
    
def listar_heroes_por_inteligencia(lista)-> None:
    print("\t\t\t########                LISTA HEROES POR INTELIGENCIA             ########\n")
    heroes_por_inteligencia = filtrar_heroe_categoria(lista,"inteligencia")
    mostrar_heroe_categoria(lista, heroes_por_inteligencia)

def ingresar_menu_desafio_01(lista):
    while True:
        os.system("cls")
        match menu("STARK INDUSTRIES SUB MENU"," 1 --> Imprimir nombre de todos los superheroes M\n 2 --> Imprimir nombre de todos los superheroes F\n 3 --> El superhéroe más alto de género M\n 4 --> El superhéroe más alto de género F\n 5 --> El superhéroe más bajo de género M\n 6 --> El superhéroe más bajo de género F\n 7 --> Altura promedio de los superhéroes de género M\n 8 --> Altura promedio de los superhéroes de género F\n 9 --> Nombre del superhéroe más alto de género M\n10 --> Nombre del superhéroe más alto de género F\n11 --> Nombre del superhéroe más bajo de género M\n12 --> Nombre del superhéroe más bajo de género F\n13 --> Cuántos superhéroes tienen cada tipo de color de ojos\n14 --> Cuántos superhéroes tienen cada tipo de color de pelo\n15 --> Cuántos superhéroes tienen cada tipo de inteligencia\n16 --> Listar todos los superhéroes agrupados por color de ojos\n17 --> Listar todos los superhéroes agrupados por color de pelo\n18 --> Listar todos los superhéroes agrupados por tipo de inteligencia\n19 --> Volver\n\n"):   
            case "1":
                listar_nombre_genero(lista,"M")
            case "2":
                listar_nombre_genero(lista,"F")
            case "3":
                listar_mas_alto_genero(lista,"M")
            case "4":
                listar_mas_alto_genero(lista,"F")
            case "5":
                listar_mas_bajo_genero(lista,"M")
            case "6":
                listar_mas_bajo_genero(lista,"F")
            case "7":
                promediar_altura_genero(lista,"M")
            case "8":
                promediar_altura_genero(lista,"F")
            case "9":
                nombrar_mayor_altura_genero(lista,"M")
            case "10":
                nombrar_mayor_altura_genero(lista,"F")
            case "11":
                nombrar_menor_altura_genero(lista,"M")
            case "12":
                nombrar_menor_altura_genero(lista,"F")
            case "13":
                listar_cantidad_color_ojos(lista)   
            case "14":
                listar_cantidad_color_pelo(lista)
            case "15":
                listar_cantidad_tipo_inteligencia(lista)
            case "16":
                listar_heroes_por_color_ojos(lista)
            case "17":
                listar_heroes_por_color_pelo(lista)
            case "18":
                listar_heroes_por_inteligencia(lista)
            case "19":
                print("Volviendo al menu principal...")
                break
        os.system("pause")

def menu_heroes(lista,opcion):
    # CONVIERTO TODAS LAS ALTURAS QUE ESTAN EN STRING LAS PASO A FLOAT
    cambiar_tipo_campo_dic(lista,"altura",str,float)
    cambiar_tipo_campo_dic(lista,"peso",str,float)
    # Inicializo las claves vacias con "No tiene"
    inicializar_clave_vacia(lista,"color_pelo","No tiene")
    inicializar_clave_vacia(lista,"inteligencia","No tiene")
    
    match opcion:
        case "1":
            imprimir_lista_nombres_heroes(lista)    
        case "2":
            imprimir_nombre_altura_heroes(lista)
        case "3":
            mostrar_heroe_mas_alto(lista)
        case "4":
            mostrar_heroe_mas_bajo(lista)
        case "5":
            mostrar_promedio_alturas_heroes(lista)
        case "6":
            mostrar_nombre_heroe_mas_alto(lista)
        case "7":
            mostrar_nombre_heroe_mas_bajo(lista)
        case "8":
            mostrar_maximo_peso_heroe(lista)
        case "9":
            mostrar_minimo_peso_heroe(lista)
        case "10":
            ingresar_menu_desafio_01(lista)