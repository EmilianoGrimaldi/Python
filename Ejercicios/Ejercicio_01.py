# Ejercicio 01
# La división de higiene está trabajando en un control de stock para productos
# sanitarios. Debemos realizar la carga de
# una compra de productos de prevención de contagio, de cada una debe obtener los
# siguientes datos:
# · El tipo ("barbijo", "jabón" o "alcohol")
# · El precio
# · La cantidad de unidades
# · La marca
# · El fabricante
# Se debe informar los datos de la compra procesados para poder iniciar el control de
# stock.

while True:  # Siempre va a entrar al bucle
    try:
        producto_tipo = str(
            input("Ingresar tipo de producto [barbijo - jabon - alcohol]: "))
        if (producto_tipo == "barbijo" or producto_tipo == "jabon" or producto_tipo == "alcohol"):
            break  # para salir del bucle infinito
        else:
            print("Tipo incorrecto")
    except ValueError:
        print("No se ingreso una palabra")

while True:  # Siempre va a entrar al bucle
    try:
        precio_producto = int(
            input("Ingresar precio del producto [Superior a 0]: "))
        if (precio_producto > 0):
            break  # para salir del bucle infinito
        else:
            print("Error! Precio inferior a 0")
    except ValueError:
        print("Eso no es un numero")

while True:  # Siempre va a entrar al bucle
    try:
        cantidad_productos = int(
            input("Ingresar cantidad de productos [Superior a 0]: "))
        if (cantidad_productos > 0):
            break  # para salir del bucle infinito
        else:
            print("Error! Cantidad inferior a 0")
    except ValueError:
        print("Eso no es un numero")
# · La marca
marca_producto = str(input("Ingrese marca del producto: "))

# · El fabricante
fabricante_producto = str(input("Ingrese fabricante del producto: "))

print(f"El tipo de producto es {producto_tipo}")
print(f"El precio del producto es ${precio_producto}")
print(f"La cantidad de unidades es {cantidad_productos}")
print(f"La marca del producto es {marca_producto}")
print(f"El fabricante del producto es {fabricante_producto}")
