from funciones import *
flag_frutas = False
lista_frutas = []
dolar = 221
for i in range(10):
    #Dic vacio para crear un dic en cada iteracion y guardar los datos
    dic_frutas = {}
    #Carga de datos validados
    dic_frutas["nombre"] = pedir_string_espacio("Ingrese fruta\n")
    dic_frutas["precio"] = pedir_flotante("Ingrese precio de fruta en dolares\n")
    #Agrego los dic a la lista para recorrerlos mas tarde
    lista_frutas.append(dic_frutas)

fruta_ingresada = pedir_string_espacio("Ingrese nombre de fruta\n")

for fruta in lista_frutas:
    if fruta_ingresada == fruta["nombre"]:
        precio_pesos = (fruta["precio"] * dolar) / 1
        flag_frutas = True
    
if flag_frutas:
    print(f"{fruta_ingresada} --> ${precio_pesos:.2f}")
else:
    print("No se encontro esa fruta")