from data import *

flag_edad_maxima = True
# datos_personas_mayor = []

for persona in origen_data:
    if flag_edad_maxima or persona["edad"] >= edad_maxima :
        edad_maxima = persona["edad"]
        datos_mayor_edad = persona
        flag_edad_maxima = False

print(edad_maxima)

#para filtrar 
for persona in origen_data:
    if edad_maxima == persona["edad"]:
        print(persona)
        # datos_personas_mayor.append(persona)

# print(datos_personas_mayor)