from data_stark import *
from functools import reduce

def mostrar_heroe(heroe:dict):
    print(f'{heroe["nombre"]:20s}        {heroe["identidad"]:30s}{heroe["empresa"]:20s}{heroe["altura"]:20s}{heroe["peso"]:20s}{heroe["genero"]:3s} {heroe["color_ojos"]:10s} {heroe["color_pelo"]:15s} {heroe["fuerza"]:5s} {heroe["inteligencia"]:5s}')

def mostrar_personas(lista:list):
    for heroe in lista:
        mostrar_heroe(heroe)


color_ojos = list(map(lambda per:per["color_ojos"].capitalize(), lista_personajes))
color_ojos_sin_rep = list(set(map(lambda per:per["color_ojos"].capitalize(), lista_personajes)))
print(color_ojos)
print(color_ojos_sin_rep)

masculinos = list(filter(lambda per:per["genero"] == "M" and int(per["fuerza"]) > 10,lista_personajes))

# mostrar_personas(masculinos)

nombres = list(map(lambda per:per["nombre"],masculinos))

print(nombres)

nombre_fuerza = list(map(lambda per: {"nombre": per['nombre'],"fuerza": per['fuerza']},lista_personajes))

nombre_fuerza = list(map(lambda per: [per['nombre'],per['fuerza']],lista_personajes))

print(nombre_fuerza)

mayor_peso = reduce(lambda ant, act: float(act['peso']) if float(act['peso']) > ant else ant, lista_personajes, 0)

personaje_pesado = reduce(lambda ant, act: act if float(act['peso']) > float(ant['peso']) else ant, lista_personajes)

mostrar_heroe(personaje_pesado)