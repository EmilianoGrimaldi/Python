from funciones import *
#4. Crear un diccionario que contenga los nombres de 5 animales y la cantidad de patas que tienen. Pedir al usuario que ingrese el nombre del animal e imprimir en pantalla la cantidad de patas correspondiente.

flag_animal = False
animales = []

for i in range(5):
    #Dic vacio para crear un dic en cada iteracion y guardar los datos
    dic_animales = {}
    #Carga de datos validados
    dic_animales["animal_nombre"] = pedir_string_espacio("Ingrese tipo de animal\n")
    dic_animales["cantidad_patas"] = pedir_entero("Ingrese las patas que tiene el animal\n")
    #Agrego los dic a la lista para recorrerlos mas tarde
    animales.append(dic_animales)

animal_ingresado = pedir_string_espacio("Ingrese animal a buscar\n")

for animal in animales:
    if animal_ingresado == animal["animal_nombre"]:
        patas = animal["cantidad_patas"]
        flag_animal = True
    
if flag_animal:
    print(f"{animal_ingresado} --> tiene {patas} patas")
else:
    print("No se encontro ese animal")