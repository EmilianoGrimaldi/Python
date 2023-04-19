from funciones import *
#10. Crear un diccionario que contenga los nombres, edades, alturas (en centímetros) y géneros de 10 personas. Luego, convertir las alturas de centímetros a pies y pulgadas sabiendo que un pie son 30.48 cm y 1 pulgada son 2.54 cm) y agregar los datos al diccionario. Finalmente, imprimir en consola los nombres de las personas con su genero y su altura en pies y pulgadas.

personas = []

for persona in range(2):
    una_persona = {}
    
    una_persona['nombre'] = pedir_cadena("Ingrese nombre\n")
    una_persona['edad'] = pedir_entero("Ingrese edad\n")
    una_persona['altura'] = pedir_entero("Ingrese altura en cm\n")
    while True:
        una_persona['genero'] = input("Ingrese genero 'F' o 'M'\n").lower()
        if una_persona['genero'] == "f" or una_persona['genero'] == "m":
            break
        else:
            print("Error genero! No se encontro")
    una_persona['altura_pie'] = pasar_cm_pies(una_persona['altura'])
    una_persona['altura_pulgada'] = pasar_cm_pulgadas(una_persona['altura'])

    personas.append(una_persona)


for persona in personas:
    print(f"{persona['nombre']} su genero es {persona['genero']} y tiene una altura de {persona['altura_pie']:.2f} pies y en pulgadas tiene una altura de {persona['altura_pulgada']:.2f} pulgadas") 

