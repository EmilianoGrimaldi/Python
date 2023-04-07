# 1-
# Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de autos que tienen disponible a la venta. 
# Para esto se necesita saber de cada auto: la marca, el año del modelo y el precio (validar los tipos de datos ingresados) y 
# mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio sin usar listas primero, y despues usando listas y comparar la composición del código.

seguir = "s"
autos = []

while seguir == "s":
    while True:
        marca_auto = input("Ingrese la marca del auto: ")
        if marca_auto.isalpha() :
            break
        else:
            print("ERROR! Se permiten solo palabras")

    while True:
        anio_auto = input("Ingrese año de modelo: ")
        if anio_auto.isdigit():
            anio_auto = int(anio_auto)
            break
        else:
            print("ERROR! No se ingreso un numero")

    while True:
        precio_auto = input("Ingrese precio del auto: ")
        if precio_auto.isdigit():
            precio_auto = float(precio_auto)
            break
        else:
            print("ERROR! No se ingreso un numero")
    # para hacer una lista de autos, primero tengo que saber que es un auto
    auto = [marca_auto, anio_auto, precio_auto]
    #necesito otra variable para almecenar la lista de autos y almacenarlos al final de la lista
    autos.append(auto)
    # autos[auto[marca_auto, anio_auto, precio_auto]]
    while True:
        seguir = input("'s' para continuar y 'n' para salir\n")
        if(seguir == "s" or seguir == "n"):
            break
        else:
            print("ERROR! Opcion incorrecta.")
rango = len(autos)
autos.sort()
for i in range(rango):
    print(f"Marca: {autos[i][0]} Año: {autos[i][1]} Precio: {autos[i][2]}")
##nueva_lista = sorted(autos)
# for i in range(rango):
#     print(nueva_lista[i])