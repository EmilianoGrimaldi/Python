from lista_frutas import *
#3. Crear un diccionario que contenga los nombres de 10 frutas y su precio en dolares. Pedir al usuario que ingrese el nombre de una fruta y luego imprimir en pantalla su precio correspondiente en pesos.

flag_frutas = False
dolar = 221
while True:
    fruta_nombre = input("Ingrese nombre de fruta\n").lower()
    if fruta_nombre.isalpha():
        break
    else:
        print(f"Se pidio una cadena alfabetica. Usted ingreso {fruta_nombre}")

for fruta in frutas:
    if fruta_nombre == fruta["nombre"]:
        precio_pesos = (fruta["precio"] * dolar) / 1
        flag_frutas = True
    
if flag_frutas:
    print(f"{fruta_nombre} --> ${precio_pesos:.2f}")
else:
    print("No se encontro esa fruta")