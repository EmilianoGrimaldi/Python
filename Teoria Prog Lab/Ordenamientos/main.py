from data import *
from funciones import *

def mostrar_persona(persona:dict):
    print(f'{persona["id"]:2d}        {persona["nombre"]:20}{persona["apellido"]:20}{persona["email"]:40}{persona["genero"]:5}{persona["edad"]:5}')

def mostrar_personas(lista:list):
    for persona in lista:
        mostrar_persona(persona)


ordenar_lista_doble_criterio_creciente_decreciente(origen_data,"edad", "genero", False)
print("------------------------------")
mostrar_personas(origen_data)

