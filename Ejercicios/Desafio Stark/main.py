from data_stark import lista_personajes
from funciones_stark import *
from mis_funciones import *
import os

while True:
    os.system("cls")
    # CONVIERTO TODAS LAS ALTURAS QUE ESTAN EN STRING LAS PASO A FLOAT
    cambiar_tipo_str_float(lista_personajes,"altura")
    cambiar_tipo_str_float(lista_personajes,"peso")
       
    encabezado_menu()
    opcion = pedir_entero_rango("Ingrese una opcion\n",1,10)
    
    match opcion:
        case 1:
            imprimir_lista_nombres(lista_personajes)
        case 2:
            imprimir_nombre_altura(lista_personajes)
        case 3:
            buscar_mas_alto_y_mostrarlo(lista_personajes)
        case 4:
            buscar_mas_bajo_y_mostrarlo(lista_personajes)
        case 5:
            calcular_altura_promedio_mostrar(lista_personajes)
        case 6:
            mostrar_nombre_mas_alto(lista_personajes)
        case 7:
            mostrar_nombre_mas_bajo(lista_personajes)
        case 8:
            buscar_maximo_peso_mostrar(lista_personajes)
        case 9:
            buscar_minimo_peso_mostrar(lista_personajes)
        case 10:
            if opcion == 10:
                confirmacion = input(
                    "Esta seguro que salir del programa? [s/n]\n").lower()
                if confirmacion == "s":
                    break
    
    os.system("pause")
print("FIN DEL PROGRAMA")