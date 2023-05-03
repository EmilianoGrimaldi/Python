from data_stark import *
from data_stark_testing import *
from funciones_stark import *

while True:
    os.system("cls")
    for item in lista_personajes:
        print(type(item["altura"]))
    # lista = []
    stark_normalizar_datos(lista_personajes,"altura",float)
    for item in lista_personajes:
        print(type(item["altura"]))

    opcion = menu("STARK INDUSTRIES"," 1 --> Imprimir nombre de todos los heroes\n 2 --> Imprimir nombre y altura de los heroes\n 3 --> El heroe mas alto\n 4 --> El heroe mas bajo\n 5 --> Altura promedio de los heroes\n 6 --> Nombre del heroe mas alto\n 7 --> Nombre del heroe mas bajo\n 8 --> Heroe mas pesado\n 9 --> Heroe menos pesado\n10 --> Sub menu\n11 --> Salir\n\n")
    
    menu_heroes(lista_personajes,opcion)
    
    if opcion == "11":
        confirmacion = input("Seguro que quiere salir? [s/n]\n").lower()
        if confirmacion == "s":
            break
    os.system("pause")