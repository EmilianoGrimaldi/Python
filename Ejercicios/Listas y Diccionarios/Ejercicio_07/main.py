from funciones import *
from funciones_ejercicio_7 import *
#7. Crear un diccionario que contenga los nombres, edades, alturas (en metros), pesos (en kilogramos) y ciudades de un numero indeterminados de personas. 
# Luego calcular el indice de masa corporal (IMC) de cada persona y agregarlo al diccionario. 
# Finalmente, imprimir en pantalla los nombres de las personas junto con su ciudad y si IMC (redondeando a 2 decimales).

seguir = "s"
lista_personas = []

while seguir == "s":

    dic_persona  = {}

    #ingreso de datos
    dic_persona["nombre"] = pedir_string_espacio("Ingrese nombre de la persona\n")
    dic_persona["edad"] = pedir_entero_rango("Ingrese edad de la persona\n",0,110)
    dic_persona["altura"] = pedir_flotante("Ingrese la altura en metros\n")
    dic_persona["peso"] = pedir_flotante("Ingrese peso de la persona en kg\n")
    dic_persona["ciudad"] = pedir_string_espacio("Ingrese ciudad de la persona\n")
    dic_persona["imc"] = calcular_imc(dic_persona["peso"],dic_persona["altura"])
    lista_personas.append(dic_persona)

    seguir = input("Quiere continuar? Presione 's'. Cualquier tecla para salir\n")
    if  not seguir == "s":
        break

#mostrar datos en pantalla
for persona in lista_personas:
    print(f"{persona['nombre']} de {persona['ciudad']} tiene {persona['imc']:.2f} de indice de masa muscular")