from desafio_00 import *

def menu():
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
    
while True:
    os.system("cls") 
    personajes_masculinos = []
    personajes_femeninos = []
    
    for personaje in lista_personajes:
        if personaje['genero'] == "M":
            personajes_masculinos.append(personaje)
    for personaje in lista_personajes:
        if personaje['genero'] == "F":
            personajes_femeninos.append(personaje)

    match menu():
        case 1:
            encabezado(
                "########                NOMBRE DE CADA SUPERHEROE MASCULINO               ########\n")
            for personaje in lista_personajes:
                if personaje['genero'] == "M":
                    print("\t\t\t|{:^30}|".format(personaje['nombre']))
        case 2:
            encabezado(
                "########                NOMBRE DE CADA SUPERHEROE FEMENINO              ########\n")
            for personaje in lista_personajes:
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
            pass
        case 14:
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
