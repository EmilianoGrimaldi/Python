from data_stark import lista_personajes
from mis_funciones import *
import os

flag_mas_alto = True
flag_mas_bajo = True
flag_menos_peso = True
flag_mas_peso = True
lista_mas_altos = []
lista_mas_bajos = []
lista_menos_pesados = []
lista_mas_pesados = []
acumulador_altura = 0

while True:
    os.system("cls")
    # CONVIERTO TODAS LAS ALTURAS QUE ESTAN EN STRING LAS PASO A FLOAT
    cambiar_tipo_campo_dic(lista_personajes,str,float,"altura")
    cambiar_tipo_campo_dic(lista_personajes,str,float,"peso")
    while True:
        try:
            opcion = int(input("########                STARK INDUSTRIES                 ########\n\n1 --> Imprimir nombre de todos los superheroes\n2 --> Imprimir nombre y altura de los superheroes\n3 --> El superheroe mas alto\n4 --> El superheroe mas bajo\n5 --> Altura promedio de los superheroes\n6 --> Nombre del superheroe maximo\n7 --> Nombre del superheroe minimo\n8 --> Superheroe mas pesado\n9 --> Superheroe menos pesado\n10 --> Salir\n\n"))
            if opcion >= 1 and opcion <= 10:
                break
            else:
                print("Error! Opcion inexistente\n")
        except ValueError:
            print(f"Error de tipo. Ingrese una opcion numerica\n")

    match opcion:
        case 1:
            imprimir_campo_dic(lista_personajes,"nombre")
        case 2:
            for personaje in lista_personajes:
                print(f"{personaje['nombre']}, su altura es --> {personaje['altura']:.2f} m")
        case 3:
            altura_maxima = calcular_maximo_campo_dic(lista_personajes,"altura")
            lista_mas_altos = agrupar_maximos_minimos(lista_personajes,"altura",altura_maxima)
            for personaje in lista_mas_altos:
                print(f"El mas alto es {personaje['nombre']} y su altura es {personaje['altura']:.2f} m")
        case 4:
            altura_minima = calcular_minimo_campo_dic(lista_personajes,"altura")
            lista_mas_bajos = agrupar_maximos_minimos(lista_personajes, "altura", altura_minima)
            for personaje in lista_mas_bajos:
                print(f"El mas bajo es {personaje['nombre']} y su altura es {personaje['altura']:.2f} m")
        case 5:
            total_altura = acumular_total_campo_dic(lista_personajes, "altura")
            altura_promedio = sacar_promedio(total_altura,len(lista_personajes))
            print(f"La altura promedio es {altura_promedio:.2f}")
        case 6:
            for personaje in lista_mas_altos:
                print(f"El mas alto es --> {personaje['nombre']}, su altura es --> {personaje['altura']:.2f} m y su identidad es --> {personaje['identidad']}")
        case 7:
            for personaje in lista_mas_bajos:
                print(f"El mas bajo es --> {personaje['nombre']}, su altura es --> {personaje['altura']:.2f} m y su identidad es --> {personaje['identidad']}")
        case 8:
            peso_maximo = calcular_maximo_campo_dic(lista_personajes, "peso")
            lista_mas_pesados = agrupar_maximos_minimos(lista_personajes, "peso", peso_maximo)

            for personaje in lista_mas_pesados:
                print(f"El superheroe mas pesado es {personaje['nombre']} y su peso es {personaje['peso']:.3f} kg")
        case 9:
            peso_minimo = calcular_minimo_campo_dic(lista_personajes, "peso")
            lista_menos_pesados = agrupar_maximos_minimos(lista_personajes, "peso", peso_minimo)
            for personaje in lista_menos_pesados:
                print(f"El superheroe menos pesado es {personaje['nombre']} y su peso es {personaje['peso']:.3f} kg")
        case 10:
            if opcion == 10:
                confirmacion = input(
                    "Esta seguro que salir del programa? [s/n]\n").lower()
                if confirmacion == "s":
                    break
    os.system("pause")
print("FIN DEL PROGRAMA")