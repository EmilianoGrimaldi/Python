from data import *
from funciones import *
import os

personas = []

while True:
    os.system("cls")
    match menu("GESTION DE PERSONAS","1 -> CARGAR LISTA\n2 -> MOSTRAR PERSONAS\n3 -> PROXIMAMENTE\n4 -> SALIR\n\n"):
        case "1":
            cargar_lista(origen_data,personas)
        case "2":
            mostrar_personas(personas)    
        case "3":
            pass
        case "4":
            break
    os.system("pause")