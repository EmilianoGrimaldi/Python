from funciones import *
#6. Rehacer los primeros 5 ejercicios pero sin hardcodear los diccionarios, es decir, el diccionario debe empezar vacio y deberán cargar las claves y valores del diccionario por consola.

## 1. Crear un diccionario que contenga los nombres y edades de 5 paises. Luego imprimir por pantalla el nombre y la edad de cada persona.
paises = []

for i in range(2):
    #Dic vacio para crear un dic en cada iteracion y guardar los datos
    dic_paises = {}
    #Carga de datos validados
    dic_paises["nombre"] = pedir_string("Ingrese nombre\n")
    dic_paises["edad"] = pedir_entero("Ingrese edad\n")
    #Agrego los dic a la lista para recorrerlos mas tarde
    paises.append(dic_paises)

for persona in paises:
    print(f"{persona['nombre']} --> tiene {persona['edad']} años")