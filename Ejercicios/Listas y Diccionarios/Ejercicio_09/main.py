from funciones import *
#9. Crear un diccionario que contenga los nombres, edades, fechas de nacimiento, numeros de telefono y correos electrónicos de un numero indeterminado de personas. 
#Luego, concatenar la fecha de nacimiento y el número de teléfono de cada persona con el formato “11-1111-1111 – dd/mm/aaaa” 
#y agregarlo al diccionario (usar un string interpolado con format para hacerlo más facil). Finalmente imprimir en consola el nombre, correo electrónico y los datos concatenados.

personas = []

while True:
#     # diccionario vacio donde voy a almecenar los datos que conforman una persona
    una_persona = {}
    
    # ingreso de datos
    una_persona['nombre'] = pedir_cadena("Ingresar el nombre\n")
    una_persona['edad'] = pedir_entero("Ingresar edad\n")
    una_persona['fecha_nacimiento'] = pedir_fecha("Ingresar fecha de nacimiento 'DD/MM/AAAA'\n")
    una_persona['telefono'] = pedir_telefono("Ingresar su telefono celular '11-1111-1111'\n")
    una_persona['correo'] = pedir_correo("Ingrese correo\n")
    una_persona['telefono_fecha'] = "{} - {}".format(una_persona["telefono"], una_persona['fecha_nacimiento'])
    personas.append(una_persona)

    seguir = input("Para continuar presione 's. De lo contrario cualquier tecla\n").lower()
    if not seguir == "s":
        break

for persona in personas:
    print(f"{persona['nombre']} {persona['correo']} {persona['telefono_fecha']}")
print("FIN DEL PROGRAMA")

