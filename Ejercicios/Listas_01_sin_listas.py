# 1-
# Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de autos que tienen disponible a la venta. 
# Para esto se necesita saber de cada auto: la marca, el año del modelo y el precio (validar los tipos de datos ingresados) y 
# mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio sin usar listas primero, y despues usando listas y comparar la composición del código.


while True:
    marca_auto_uno = input("Ingrese la marca del auto: ")
    if marca_auto_uno.isalpha() :
        break
    else:
        print("ERROR! Se permiten solo palabras")

while True:
    auto_modelo_uno = input("Ingrese año de modelo: ")
    if auto_modelo_uno.isdigit():
        auto_modelo_uno = int(auto_modelo_uno)
        break
    else:
        print("ERROR! No se ingreso un numero")

while True:
    auto_precio_uno = input("Ingrese precio del auto: ")
    if auto_precio_uno.isdigit():
        auto_precio_uno = float(auto_precio_uno)
        break
    else:
        print("ERROR! No se ingreso un numero")

while True:
        marca_auto_dos = input("Ingrese la marca del auto: ")
        if marca_auto_dos.isalpha() :
            break
        else:
            print("ERROR! Se permiten solo palabras")
    
while True:
    auto_modelo_dos = input("Ingrese año de modelo: ")
    if auto_modelo_dos.isdigit():
        auto_modelo_dos = int(auto_modelo_dos)
        break
    else:
        print("ERROR! No se ingreso un numero")

while True:
    auto_precio_dos = input("Ingrese precio del auto: ")
    if auto_precio_dos.isdigit():
        auto_precio_dos = float(auto_precio_dos)
        break
    else:
        print("ERROR! No se ingreso un numero")

if marca_auto_uno < marca_auto_dos:
    print(f"{marca_auto_uno} {auto_modelo_uno} ${auto_precio_uno}")
    print(f"{marca_auto_dos} {auto_modelo_dos} ${auto_precio_dos}")
else:
    print(f"{marca_auto_dos} {auto_modelo_dos} ${auto_precio_dos}")
    print(f"{marca_auto_uno} {auto_modelo_uno} ${auto_precio_uno}")