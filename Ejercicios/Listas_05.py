#5 Para una veterinaria se pide clasificar el ingreso de pacientes hasta que el usuario quiera (se limita a 1 perrito por ingreso), se les pide:
# nombre, precio de la consulta (validar entre 500$ y 2500$) raza: (validar entre caniche, ovejero, siberiano), edad (validar 1 a 15) y peso (entre 25 y 40 kilos) determinar:
# 1. Generar un listado con todos los datos de los pacientes ordenados por edad.
# 2. Generar un listado de los perros que pesen más de 30 kilos y ordenarla por nombre.
# 3. Si la facturación en bruto supera los 5000$, hay que agregarle un 21% de impuesto por ingresos brutos e informarlo.
# 4. Informar el nombre y el peso del perro con más peso.

#crear un bucle que le permita cargar al usuario los pacientes que quiera. 
continuar = "s"
pacientes = []

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
    ####################################################
    paciente = [nombre_perro, precio_consulta, raza_perro, edad_perro, peso_perro]
    pacientes.append(paciente)

    continuar = input("Ingrese 's' si desea continuar cargando. Para salir presione cualquier boton\n")

# 1. Generar un listado con todos los datos de los pacientes ordenados por edad.
# Ordenamos la lista de pacientes por edad
pacientes_ordenados = sorted(pacientes, key=lambda paciente: paciente[3])

# Imprimimos el listado de pacientes ordenado por edad
print("Listado de pacientes ordenado por edad:")
for paciente in pacientes_ordenados:
    print("-" * 40)
    print(f"Nombre: {paciente[0]}")
    print(f"Precio de la consulta: ${paciente[1]}")
    print(f"Raza: {paciente[2]}")
    print(f"Edad: {paciente[3]} años")
    print(f"Peso: {paciente[4]} kilos")

# 2. Generar un listado de los perros que pesen más de 30 kilos y ordenarla por nombre.
# 3. Si la facturación en bruto supera los 5000$, hay que agregarle un 21% de impuesto por ingresos brutos e informarlo.
# 4. Informar el nombre y el peso del perro con más peso.