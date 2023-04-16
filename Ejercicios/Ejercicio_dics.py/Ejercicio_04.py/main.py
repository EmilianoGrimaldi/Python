from lista_animales import *
#4. Crear un diccionario que contenga los nombres de 5 animales y la cantidad de patas que tienen. Pedir al usuario que ingrese el nombre del animal e imprimir en pantalla la cantidad de patas correspondiente.

flag_animal = False
while True:
    animal_ingresado = input("Ingrese nombre de animal\n").lower()
    if animal_ingresado.isalpha():
        break
    else:
        print(f"Se pidio una cadena alfabetica. Usted ingreso {animal_ingresado}")

for animal in animales:
    if animal_ingresado == animal["animal_nombre"]:
        patas = animal["animal_cantidad_patas"]
        flag_animal = True
    
if flag_animal:
    print(f"{animal_ingresado} --> tiene {patas} patas")
else:
    print("No se encontro ese animal")