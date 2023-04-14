from paises import *
# 2. Crear un diccionario que contenga los nombres de paises y sus capitales (máximo 10 paises y 10 capitales). Pedirle al usuario que ingrese el nombre del pais e imprimir por pantalla el nombre de la capital si existe en el diccionario. De lo contrario informarlo.

flag_pais = False

while True:
    pais_nombre = input("Ingrese nombre del pais\n")
    if pais_nombre.isalpha():
        break
    else:
        print(f"Se pidio una cadena alfabetica. Usted ingreso {pais_nombre}")

for pais in paises:
    if pais_nombre == pais["nombre"]:
        capital = pais["capital"]
        flag_pais = True
    
if flag_pais:
    print(capital)
else:
    print("No se encontro ese pais")