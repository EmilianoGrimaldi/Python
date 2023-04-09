#5 Para una veterinaria se pide clasificar el ingreso de pacientes hasta que el usuario quiera (se limita a 1 perrito por ingreso), se les pide:
# nombre, precio de la consulta (validar entre 500$ y 2500$) raza: (validar entre caniche, ovejero, siberiano), edad (validar 1 a 15) y peso (entre 25 y 40 kilos) determinar:
# 1. Generar un listado con todos los datos de los pacientes ordenados por edad.
# 2. Generar un listado de los perros que pesen más de 30 kilos y ordenarla por nombre.
# 3. Si la facturación en bruto supera los 5000$, hay que agregarle un 21% de impuesto por ingresos brutos e informarlo.
# 4. Informar el nombre y el peso del perro con más peso.

#crear un bucle que le permita cargar al usuario los pacientes que quiera. 
continuar = "s"
pacientes = []
lista_mas_30_kg = []
facturacion = 0
bandera_mas_peso = False
# lista_mas_30_kg = []
while continuar == "s":
    #Ingreso y validacion de datos
    while True:
        nombre_perro = input("Ingrese el nombre del perro\n")
        if nombre_perro.isalpha():
            break
        else:
            print("Error! Solo se permiten caracteres alfabeticos")
    
    while True:
        try:
            precio_consulta = int(input("Ingrese precio de la consulta [entre 500$ y 2500$]\n"))
            if precio_consulta >= 500 and precio_consulta <= 2500:
                break
            else:
                print("Error! Precio fuera de rango")
        except ValueError:
            print("Error! Se pidio un entero")

    while True:
        raza_perro = input("Ingrese raza [caniche - ovejero - siberiano]\n").lower()
        if raza_perro == "caniche" or raza_perro == "ovejero" or raza_perro == "siberiano":
            break
        else:
            print("Error! Ingreso una raza inexistente")

    while True:
        try:
            edad_perro = int(input("Ingrese edad [entre 1 y 15]\n"))
            if edad_perro >= 1 and edad_perro <= 15:
                break
            else:
                print("Error! Edad fuera de rango")
        except ValueError:
            print("Error! Se pidio un entero")

    while True:
        try:
            peso_perro = float(input("Ingrese peso [entre 25 y 40 kilos]\n"))
            if peso_perro >= 25 and peso_perro <= 40:
                break
            else:
                print("Error! Peso fuera de rango")
        except ValueError:
            print("Error! Se pidio un entero")
    
    un_paciente = [nombre_perro, precio_consulta, raza_perro, edad_perro, peso_perro]
    pacientes.append(un_paciente)
    facturacion += precio_consulta

    if bandera_mas_peso == False or peso_perro > mas_peso: 
        nombre_mas_peso = nombre_perro
        mas_peso = peso_perro
        bandera_mas_peso = True

    if peso_perro > 30:
        lista_mas_30_kg.append(un_paciente)

    continuar = input("Ingrese 's' si desea continuar cargando. Para salir presione cualquier boton\n")



lista_ordenada_edad = sorted(pacientes, key = lambda x: x[3])
pacientes_peso = sorted(lista_mas_30_kg, reverse=False)

# 1. Generar un listado con todos los datos de los pacientes ordenados por edad.
print("LISTA DE LOS PACIENTES ORDENADOS POR EDAD\n")
for un_paciente in lista_ordenada_edad: # --> pacientes[un_paciente]
    print(f"Nombre: {un_paciente[0]} -- Precio de consulta: ${un_paciente[1]} -- Raza de perro: {un_paciente[2]} -- Edad: {un_paciente[3]} -- Peso: {un_paciente[4]}")
# 2. Generar un listado de los perros que pesen más de 30 kilos y ordenarla por nombre.
print("LISTA DE PERROS DE MAS 30KG ORDENADOS POR NOMBRE\n")
for un_paciente in pacientes_peso: # --> pacientes[un_paciente]
    print(f"Nombre: {un_paciente[0]} -- Precio de consulta: ${un_paciente[1]} -- Raza de perro: {un_paciente[2]} -- Edad: {un_paciente[3]} -- Peso: {un_paciente[4]}")
# 3. Si la facturación en bruto supera los 5000$, hay que agregarle un 21% de impuesto por ingresos brutos e informarlo.
if facturacion > 5000:
    impuesto = 21
    suma_impuesto = (impuesto * facturacion)/100 
    total = facturacion + suma_impuesto
    print(f"La facturacion es ${facturacion}\nEl aumento del impuesto es de ${suma_impuesto}\nEl total con aumento es ${total}")
else:
    print(f"La facturacion es ${facturacion}")
# 4. Informar el nombre y el peso del perro con más peso.
print(f"El perro con mas peso es {nombre_mas_peso}\nTiene un peso de {mas_peso}kg")

#La función sorted() tiene varios parámetros opcionales que permiten personalizar el ordenamiento de los elementos en la lista. A continuación te muestro los principales parámetros:

# iterable: Es el único parámetro obligatorio y corresponde al objeto iterable que se desea ordenar, por ejemplo una lista, tupla o conjunto.

# key: Es un parámetro opcional que recibe una función que devuelve un valor que se utiliza para ordenar los elementos. Por ejemplo, si queremos ordenar una lista de números según su valor absoluto, podemos pasar key=abs como argumento a la función sorted.

# reverse: Es un parámetro opcional que indica si se desea ordenar la lista en orden ascendente (reverse=False) o descendente (reverse=True). El valor por defecto es False.