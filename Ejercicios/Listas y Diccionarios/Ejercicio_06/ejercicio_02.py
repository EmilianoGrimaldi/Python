from funciones import *
# 2. Crear un diccionario que contenga los nombres de paises y sus capitales (máximo 10 paises y 10 capitales). Pedirle al usuario que ingrese el nombre del pais e imprimir por pantalla el nombre de la capital si existe en el diccionario. De lo contrario informarlo.

flag_pais = False

paises = []

for i in range(10):
    #Dic vacio para crear un dic en cada iteracion y guardar los datos
    dic_paises = {}
    #Carga de datos validados
    dic_paises["pais"] = pedir_string_espacio("Ingrese pais\n")
    dic_paises["capital"] = pedir_string_espacio("Ingrese capital del pais\n")
    #Agrego los dic a la lista para recorrerlos mas tarde
    paises.append(dic_paises)

pais_ingresado = pedir_string_espacio("Ingrese pais a buscar\n")

for pais in paises:
    if pais_ingresado == pais["pais"]:
        capital = pais["capital"]
        flag_pais = True
    
if flag_pais:
    print(capital)
else:
    print("No se encontro ese pais")