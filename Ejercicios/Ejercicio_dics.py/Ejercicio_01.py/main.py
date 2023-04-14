from lista_personas import *
# 1. Crear un diccionario que contenga los nombres y edades de 5 personas. Luego imprimir por pantalla el nombre y la edad de cada persona.

for persona in personas:
    print(f'{persona["nombre"]} --> {persona["edad"]}')
