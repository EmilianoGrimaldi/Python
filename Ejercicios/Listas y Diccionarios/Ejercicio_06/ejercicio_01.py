from funciones import *
# 1. Crear un diccionario que contenga los nombres y edades de 5 personas. Luego imprimir por pantalla el nombre y la edad de cada persona.

personas = []

for i in range(5):
    #Dic vacio para crear un dic en cada iteracion y guardar los datos
    dic_nombres = {}
    #Carga de datos validados
    dic_nombres["nombre"] = pedir_string("Ingrese nombre\n")
    dic_nombres["edad"] = pedir_entero("Ingrese edad\n")
    #Agrego los dic a la lista para recorrerlos mas tarde
    personas.append(dic_nombres)

for persona in personas:
    print(f"{persona['nombre']} --> tiene {persona['edad']} años")
