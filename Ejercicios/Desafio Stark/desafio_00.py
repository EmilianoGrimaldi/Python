from data_stark import lista_personajes
from funciones_stark import *

while True:
    os.system("cls")
    
    encabezado_menu()
    opcion = pedir_entero_rango("Ingrese una opcion\n",1,11)
    menu_personajes(lista_personajes, opcion)

    if opcion == 11:
        confirmacion = input("Seguro que quiere salir? [n --> para continuar] [cualquier tecla para salir]\n").lower()
        if confirmacion != "n":
            break
    
    os.system("pause")
print("FIN DEL PROGRAMA")