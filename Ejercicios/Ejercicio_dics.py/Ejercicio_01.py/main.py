#1. Crear un diccionario que contenga los nombres y edades de 5 personas. Luego imprimir por pantalla el nombre y la edad de cada persona.

for persona in range(5):
    personas = {"nombre","edad"}
    while True:
        personas["nombre"] = input("Ingresar nombre\n")
        if personas["nombre"].isalpha():
            break
        else:
            print(f"Usted ingreso {personas['nombre']}, y se pidio un nombre")
    while True:
        try:
            personas["edad"] = int(input("Ingrese edad\n"))
            break
        except ValueError:
            print("Error de tipo. Se ingreso un caracter alfabetico")

for persona in personas:
    print(f"Nombre --> {persona["nombre"]}, Edad --> {personas["edad"]}")