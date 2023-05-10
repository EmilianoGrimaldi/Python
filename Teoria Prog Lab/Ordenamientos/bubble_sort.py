from funciones import *

#BUBBLE SORT 

lista_numeros = [3, 6, 5, 8, 12, 3, 9, 21, 5, 17]
lista_nombres = ["Marcos", "Andrea", "Ramiro", "Jose", "Lucia"]

print(lista_numeros)
#------------------------------------
print("MENOR A MAYOR")
ordenar_lista(lista_numeros)
# tam = len(lista_numeros)
# for i in range(tam-1):#for exterior
#     for j in range(i+1, tam):#for interior se va ejecutar tantas veces como diga el for exterior
#         if lista_numeros[i] > lista_numeros[j]: # > menor a mayor
#             aux = lista_numeros[i]
#             lista_numeros[i] = lista_numeros[j]
#             lista_numeros[j] = aux
print(lista_numeros)

print("---------------------------------")

print("MAYOR A MENOR")
ordenar_lista(lista_numeros,False)
# for i in range(tam-1):#for exterior
#     for j in range(i+1, tam):#for interior se va ejecutar tantas veces como diga el for exterior
#         if lista_numeros[i] < lista_numeros[j]: # < mayor a menor
#             aux = lista_numeros[i]
#             lista_numeros[i] = lista_numeros[j]
#             lista_numeros[j] = aux
print(lista_numeros)

#ORDENANR STRINGS
print("A - Z")

# tam = len(lista_nombres)
# for i in range(tam-1):#for exterior
#     for j in range(i+1, tam):#for interior se va ejecutar tantas veces como diga el for exterior
#         if lista_nombres[i] > lista_nombres[j]: # > menor a mayor
#             aux = lista_nombres[i]
#             lista_nombres[i] = lista_nombres[j]
#             lista_nombres[j] = aux
# print(lista_nombres)

print("-----------------------------------------------")

print("Z - A")

# for i in range(tam-1):#for exterior
#     for j in range(i+1, tam):#for interior se va ejecutar tantas veces como diga el for exterior
#         if lista_nombres[i] < lista_nombres[j]: # < menor a mayor
#             aux = lista_nombres[i]
#             lista_nombres[i] = lista_nombres[j]
#             lista_nombres[j] = aux
print(lista_nombres)


# tam = len(lista_numeros)
# for i in range(tam-1):#for exterior
#     print("i: ", i)
#     for j in range(i+1, tam):#for interior se va ejecutar tantas veces como diga el for exterior
#         print("j: ", j)
#     print("------------------------------")#For exterior

# POR CADA HOLA 5 CHAU EN TOTAL 15 CHAU



# for i in range(3):#for exterior
#     print("i: ", i)
#     for j in range(5):#for interior se va ejecutar tantas veces como diga el for exterior
#         print("j: ", j)
#     print("------------------------------")#For exterior
# POR CADA HOLA 5 CHAU EN TOTAL 15 CHAU


# x = 7
# y = 5
# print(f"x: {x} y: {y}")
# print("-----------------------------")
# print("swap")
# aux = x
# x = y
# y = aux
# print(f"x: {x} y: {y}")
# print("-----------------------------")
# #alternativa
# aux = y
# y = x
# x = aux
# print(f"x: {x} y: {y}")
