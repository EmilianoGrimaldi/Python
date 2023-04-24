from mis_funciones import *

def imprimir_un_heroe(heroe):
        print(f" {heroe['nombre']:23s} {heroe['identidad']:32s} {heroe['empresa']:15s} {heroe['altura']:7}  {heroe['peso']:6}      {heroe['genero']:7s} {heroe['color_ojos']:26s} {heroe['color_pelo']:15s} {heroe['fuerza']:9s} {heroe['inteligencia']} ")

def imprimir_heroes(lista):
    print(" NOMBRE                  IDENTIDAD                        EMPRESA          ALTURA   PESO    GENERO    COLOR OJOS                COLOR PELO      FUERZA    INTELIGENCIA\n")
    for heroe in lista:
        imprimir_un_heroe(heroe)

def ingresar_menu_desafio_01(lista):
    heroes_masculinos = []
    heroes_femeninos = []

    for heroe in lista:
            if heroe['genero'] == "M":
                heroes_masculinos.append(heroe)
    for heroe in lista:
            if heroe['genero'] == "F":
                heroes_femeninos.append(heroe)
    for heroe in lista:
        if heroe['color_pelo'] == "":
            heroe['color_pelo'] = "No tiene"
    for heroe in lista:
        if heroe['inteligencia'] == "":
            heroe['inteligencia'] = "No tiene"

    while True:
        os.system("cls")
        match menu("STARK INDUSTRIES SUB MENU"," 1 --> Imprimir nombre de todos los superheroes M\n 2 --> Imprimir nombre de todos los superheroes F\n 3 --> El superhéroe más alto de género M\n 4 --> El superhéroe más alto de género F\n 5 --> El superhéroe más bajo de género M\n 6 --> El superhéroe más bajo de género F\n 7 --> Altura promedio de los superhéroes de género M\n 8 --> Altura promedio de los superhéroes de género F\n 9 --> Nombre del superhéroe más alto de género M\n10 --> Nombre del superhéroe más alto de género F\n11 --> Nombre del superhéroe más bajo de género M\n12 --> Nombre del superhéroe más bajo de género F\n13 --> Cuántos superhéroes tienen cada tipo de color de ojos\n14 --> Cuántos superhéroes tienen cada tipo de color de pelo\n15 --> Cuántos superhéroes tienen cada tipo de inteligencia\n16 --> Listar todos los superhéroes agrupados por color de ojos\n17 --> Listar todos los superhéroes agrupados por color de pelo\n18 --> Listar todos los superhéroes agrupados por tipo de inteligencia\n19 --> Volver\n\n"):   
            case "1":
                print("\t\t\t\t\t     ########                NOMBRE DE CADA HEROE               ########\n")
                
                for heroe in lista:
                    if heroe['genero'] == "M":
                        print("\t\t\t\t\t\t\t\t|{:^30}|".format(heroe['nombre']))
            case "2":
                print("\t\t\t\t\t     ########                NOMBRE DE CADA HEROINA              ########\n")
        
                for heroe in lista:
                    if heroe['genero'] == "F":
                            print("\t\t\t\t\t\t\t\t|{:^30}|".format(heroe['nombre']))
            case "3":
                print("\t\t\t\t\t\t\t########                HEROE MAS ALTO               ########\n")
                
                mas_altos = guardar_los_maximos(heroes_masculinos, "altura")
                imprimir_heroes(mas_altos)
            case "4":
                print("\t\t\t\t\t\t\t########                HEROINA MAS ALTA              ########\n")
                mas_altas = guardar_los_maximos(heroes_femeninos, "altura")
                imprimir_heroes(mas_altas)
            case "5":
                print("\t\t\t\t\t\t\t########                HEROE MAS BAJO               ########\n")
                mas_bajos = guardar_los_minimos(heroes_masculinos, "altura")
                imprimir_heroes(mas_bajos)
            case "6":
                print("\t\t\t\t\t\t\t########                HEROINA MAS BAJA               ########\n")
                mas_bajas = guardar_los_minimos(heroes_femeninos, "altura")
                imprimir_heroes(mas_bajas)
            case "7":
                print("\t\t\t\t\t\t\t########                ALTURA PROMEDIO HEROES               ########\n")
                acumulador_edad_masculino = acumular_total_altura(heroes_masculinos)
                promedio_masculino = sacar_promedio(acumulador_edad_masculino, len(heroes_masculinos))
                print("La altura promedio de los heroes es {:.2f}".format(promedio_masculino))
            case "8":
                print("\t\t\t\t\t\t\t########                ALTURA PROMEDIO HEROINAS               ########\n")
                acumulador_edad_femenino = acumular_total_altura(
                        heroes_femeninos)
                promedio_femenino = sacar_promedio(
                        acumulador_edad_femenino, len(heroes_femeninos))
                print("La altura promedio de las heroinas es {:.2f}".format(promedio_femenino))
            case "9":
                print("\t\t\t\t\t\t\t########                NOMBRE DE HEROE MAS ALTO               ########\n")
                mas_altos = guardar_los_maximos(heroes_masculinos, "altura")
                if len(mas_altos) == 1:
                    for heroe in mas_altos:
                        print("El heroe mas alto es {}".format(heroe["nombre"]))
                else:
                    for heroe in mas_altos:
                        print("Los heroes mas altos son\n {}".format(heroe["nombre"]))
            case "10":
                print("\t\t\t\t\t\t\t########                NOMBRE DE HEROINA MAS ALTA               ########\n")
                mas_altas = guardar_los_maximos(heroes_femeninos, "altura")
                if len(mas_altas) == 1:
                    for heroe in mas_altas:
                        print("La heroina mas alta es {}".format(heroe["nombre"]))
                else:
                    for heroe in mas_altas:
                        print("Las heroinas mas altas son\n {}".format(heroe["nombre"]))
            case "11":
                print("\t\t\t\t\t\t\t########                NOMBRE DE HEROE MAS BAJO               ########\n")
                mas_bajos = guardar_los_minimos(heroes_masculinos, "altura")
                if len(mas_bajos) == 1:
                    for heroe in mas_bajos:
                        print("El heroe mas bajo es {}".format(heroe["nombre"]))
                else:
                    for heroe in mas_bajos:
                        print("Los heroes mas bajos son\n {}".format(heroe["nombre"]))
            case "12":
                print("\t\t\t\t\t\t\t########                NOMBRE DE LA HEROINA MAS BAJA             ########\n")
                mas_bajas = guardar_los_minimos(heroes_femeninos, "altura")
                if len(mas_bajas) == 1:
                    for heroe in mas_bajas:
                        print("La heroina mas baja es {}".format(heroe["nombre"]))
                else:
                    for heroe in mas_bajas:
                        print("Las heroinas mas bajas son\n {}".format(heroe["nombre"]))
            case "13":
                print("\t\t\t\t\t     ########                CANTIDAD DE TIPOS DE COLOR DE OJOS             ########\n")
                #Creo un dic vacio para ir guardando los colores como clave y la cantidad como valor
                color_ojos_cant = {}
                
                for heroe in lista:
                    #Hago una busqueda y voy guardando el color de ojos de ese heroe
                    color_ojos = heroe['color_ojos'].lower()
                    #Pregunto si ese color existe dentro del diccionario
                    if color_ojos in color_ojos_cant:
                        #si existe le sumo 1 al valor de ese color
                        color_ojos_cant[color_ojos] += 1
                    else:
                        #sino existe creo la clave de ese color y le asigno el valor 1 (para indicar que es el primer color)
                        color_ojos_cant[color_ojos] = 1
                
                print("\t\t\t\t\t\t\t    |           COLOR OJOS           |   CANTIDAD   |\n")
                #items tranforma ese diccionario en una lista de tuplas clave : valor
                for color,cantidad in color_ojos_cant.items():  
                    print("\t\t\t\t\t\t\t    |\t {:28s}|\t    {:2d}\t    |".format(color,cantidad))
                     
            case "14":
                print("\t\t\t\t\t ########                CANTIDAD DE TIPOS DE COLOR DE PELO             ########\n")
                color_pelo_cant = {}
                for heroe in lista:    
                    color_pelo = heroe['color_pelo'].lower()       
                    if color_pelo in color_pelo_cant:
                        color_pelo_cant[color_pelo] += 1
                    else:
                        color_pelo_cant[color_pelo] = 1
                 
                #items() retorna una lista de tuplas, donde cada tupla tiene dos elementos: el primero es la clave y el segundo es el valor asociado a esa clave.
                
                print("\t\t\t\t\t\t\t    |         COLOR PELO        |  CANTIDAD  |\n")
                for color,cantidad in color_pelo_cant.items():  
                    print("\t\t\t\t\t\t\t    |   {:24s}|{:^12}|".format(color,cantidad))
            case "15":
                print("\t\t\t\t\t ########                CANTIDAD DE TIPOS DE INTELIGENCIA             ########\n")
                inteligencia_cant = {}
                for heroe in lista:    
                    inteligencia = heroe['inteligencia'].lower()

                    if inteligencia in inteligencia_cant:
                        inteligencia_cant[inteligencia] += 1
                    else:
                        inteligencia_cant[inteligencia] = 1
                 
                #items() retorna una lista de tuplas, donde cada tupla tiene dos elementos: el primero es la clave y el segundo es el valor asociado a esa clave.
                
                print("\t\t\t\t\t\t\t    |          INTELIGENCIA        |  CANTIDAD  |\n")
                for inteligencia,cantidad in inteligencia_cant.items():  
                    print("\t\t\t\t\t\t\t    |    {:26s}|\t {:2d}\t|".format(inteligencia,cantidad))
            case "16":
                print("\t\t\t########                LISTA SUPERHEROES POR COLOR DE OJOS             ########\n")
                dict_color_ojos = {}
                #creo un diccionario vacio para ir guardando el color como clave y una lista de nombres como valor
                for heroe in lista:    
                    ojos_color = heroe["color_ojos"].lower()
                    #guardo el color de ojos de ese heroe
                    if  ojos_color not in dict_color_ojos:
                    #pregunto si el color de ojos del heroe NO ESTA en el diccionario
                        dict_color_ojos[ojos_color] = []
                        #Si el color no existe dentro del diccionario, lo creo y le asigno una lista vacia donde voy a guardar los nombres de los heroes 
                    dict_color_ojos[ojos_color].append(heroe['nombre'])
                    #le agrego el nombre del heroe a lista de ese color    
                
                
                for color, heroes in dict_color_ojos.items():
                    print("{:15s}".format(color))
                    for heroe in heroes:
                        print(" --> {}".format(heroe))
            case "17":
                print("\t\t\t########                LISTA SUPERHEROES POR COLOR DE PELO             ########\n")
                dict_color_pelo = {}
                for heroe in lista:    
                    pelo_color = heroe["color_pelo"].lower()

                    if  pelo_color not in dict_color_pelo:
                        dict_color_pelo[pelo_color] = [] 
                    dict_color_pelo[pelo_color].append(heroe['nombre'])    
                
                for color, heroes in dict_color_pelo.items():
                    print("{:15s}".format(color))
                    for heroe in heroes:
                        print(" --> {}".format(heroe))
            case "18":
                print("\t\t\t########                LISTA SUPERHEROES POR INTELIGENCIA             ########\n")
                dic_inteligencia = {}
                for heroe in lista:    
                    inteligencia = heroe['inteligencia'].lower()
                        
                    if inteligencia not in dic_inteligencia:
                        dic_inteligencia[inteligencia] = []
                    
                    dic_inteligencia[inteligencia].append(heroe['nombre'])

                for inteligencia, heroes in dic_inteligencia.items():
                    print("{:15s}".format(inteligencia))
                    for heroe in heroes:
                        print(" --> {}".format(heroe))

            case "19":
                print("Volviendo al menu principal...")
                break
        os.system("pause")        

def cambiar_tipo_str_float(lista, campo):
    for item in lista:
        if type(item[campo]) == str:
            item[campo] = float(item[campo])

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


def acumular_total_altura(lista):
    acumulador = 0
    for heroe in lista:
        acumulador += heroe["altura"]
    return acumulador


def sacar_promedio(dividendo, divisor):
    promedio = dividendo / divisor
    return promedio


def mostrar_promedio(promedio):
    print("{:.2f}".format(promedio))


def cambiar_tipo_campo_dic(lista, tipo_actual, tipo_nuevo, clave_a_cambiar):
    for item in lista:
        if type(item[clave_a_cambiar]) == tipo_actual:
            item[clave_a_cambiar] = tipo_nuevo(item[clave_a_cambiar])


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
        imprimir_heroes(lista_mas_altos)
    else:
        if len(lista_mas_altos) > 1:
            print("\t\t\t\t\t\t\t\tLOS HEROES MAS ALTOS\n")
            imprimir_heroes(lista_mas_altos)
    


def mostrar_heroe_mas_bajo(lista):
    lista_mas_bajos = guardar_los_minimos(lista, "altura")
    if len(lista_mas_bajos) == 1:
        print("\t\t\t\t\t\t\t\tEL HEROE MAS BAJO\n")
        imprimir_heroes(lista_mas_bajos)
    else:
        if len(lista_mas_bajos) > 1:
            print("\t\t\t\t\t\t\t\tLOS HEROES MAS BAJOS\n")
            imprimir_heroes(lista_mas_bajos)


def mostrar_promedio_alturas_heroes(lista):
    print("\t\t\t\t\t\t\t\tALTURA PROMEDIO DE LOS SUPERHEROES\n")
    altura_total = acumular_total_altura(lista)
    promedio_altura = sacar_promedio(altura_total, len(lista))
    print("La altura promedio de los heroes es {:.2f}".format(promedio_altura))


def mostrar_nombre_heroe_mas_alto(lista):
    
    lista_aux = guardar_los_maximos(lista, "altura")
    
    if len(lista_aux) == 1:
        print("\t\t\t\t\t\t\t\tNOMBRE DEL HEROE MAS ALTO\n")
        for heroe in lista_aux:
            print("El heroe mas alto es {}".format(heroe['nombre']))
    else:
        if len(lista_aux) > 1:
            print("\t\t\t\t\t\t\t\tNOMBRES DE LOS HEROES MAS ALTOS\n")
            for heroe in lista_aux:
                print("Los heroes mas altos son \n {}".format(heroe['nombre']))


def mostrar_nombre_heroe_mas_bajo(lista):
    lista_aux = guardar_los_minimos(lista, "altura")
    
    if len(lista_aux) == 1:
        print("\t\t\t\t\t\t\t\tNOMBRE DE HEROE MAS BAJO\n")
        for heroe in lista_aux:    
            print("El heroe mas bajo es {}".format(heroe["nombre"]))
    else:
        if len(lista_aux) > 1:
            print("\t\t\t\t\t\t\t\tNOMBRES DE LOS HEROES MAS BAJOS\n")
            for heroe in lista_aux:
                print("Los heroes mas bajos son \n {}".format(heroe["nombre"]))

def mostrar_maximo_peso_heroe(lista):
    lista_mas_pesados = guardar_los_maximos(lista, "peso")
    if len(lista_mas_pesados) == 1:
        print("\t\t\t\t\t\t\t\tHEROE MAS PESADO\n")
        for heroe in lista_mas_pesados:
            print("El heroe mas pesado es {}".format(heroe["nombre"]))
    else:
        if len(lista_mas_pesados) > 1:
            print("\t\t\t\t\t\t\t\tHEROES MAS PESADOS\n")
            for heroe in lista_mas_pesados:
                print("Los heroes mas pesados son \n {}".format(heroe["nombre"]))
            
        
def mostrar_minimo_peso_heroe(lista):
    lista_menos_pesados = guardar_los_minimos(lista, "peso")
    if len(lista_menos_pesados) == 1:
        print("\t\t\t\t\t\t\t\tHEROE MENOS PESADO\n")
        for heroe in lista_menos_pesados:
            print("El heroe menos pesado es {}".format(heroe["nombre"]))
    else:
        if len(lista_menos_pesados) > 1:
            print("\t\t\t\t\t\t\t\tHEROES MENOS PESADOS\n")
            for heroe in lista_menos_pesados:
                print("Los heroes menos pesados son \n {}".format(heroe["nombre"]))


def menu_heroes(lista,opcion):
    # CONVIERTO TODAS LAS ALTURAS QUE ESTAN EN STRING LAS PASO A FLOAT
    cambiar_tipo_str_float(lista, "altura")
    cambiar_tipo_str_float(lista, "peso")
    
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