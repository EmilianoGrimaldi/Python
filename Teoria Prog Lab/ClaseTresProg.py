# numeros = []
# bandera_max = False
# for n in range(5):
#     while True:
#         try:
#             numeros.append(int(input("Ingrese un numero\n")))
#             break
#         except ValueError:
#             print("Error de tipo. Va un entero")
        
# for numero in numeros: 
#     if bandera_max == False or numero > num_max: 
#         num_max = numero
#         bandera_max = True

# print(f"El max es {num_max}")

#SABER SI ESTA O NO ESTA

# numeros = [1,2,3,4,5]
# bandera_esta = False
# numero_buscado = int(input("Ingrese un numero\n"))

# for numero in numeros:
#     if numero == numero_buscado:
#         bandera_esta = True
#         break

# if bandera_esta:
#     print("El numero esta en la lista")
# else:
#     print("El numero NO esta en la lista")

#BUSCAR INDICE DE ALGO QUE EXISTE EN UNA LISTA

# indice = -1
# for i in range(len(numeros)):
#     if numeros[i] == numero_buscado:
#         indice = i
#         break

# if indice != -1:
#     print(f"El numero esta en el indice {indice}")
# else:
#     print("El numero NO esta en la lista")
import os #Bibliotecas #PARA LIMPIAR LA CONSOLA
#HACER MENU

# flag_opcion1 = False
# flag_opcion2 = False
# flag_opcion3 = False
# while True:
#     os.system("cls") #PARA LIMPIAR LA CONSOLA
#     print("### MENU DE OPCIONES ###\n")
#     print("1 - Hola")
#     print("2 - Como estas?")
#     print("3 - Chau")
#     print("4 - Salir\n")
#     opcion = input("Ingrese opcion: ")
#     if opcion == "1":
#         print("Opcion 1")
#         flag_opcion1 = True
#     else:
#         if opcion == "2":
#             if flag_opcion1:
#                 print("Opcion 2")
#                 flag_opcion2 = True
#             else: 
#                 print("Primero ingresa a la opcion 1")
#         else:
#             if opcion == "3":
#                 if flag_opcion2:
#                     print("Opcion 3")
#                     flag_opcion3 = True
#                 else:
#                     print("Primero ingresa a la opcion 2")
#             else:
#                 if opcion == "4":
#                     salir = input("Confirma salida? s/n\n")
#                     if salir == "s":
#                         break
#     os.system("pause")

#MAS DE LISTAS
notas_p1 = [7,2,4,6,10]
notas_p2 = [4,7,10,8,3]
promedios = []

#carga de notas
for i in range(5):
    prom = (notas_p1[i] + notas_p2[i]) / 2
    promedios.append(prom)
print("PARCIAL 1        PARCIAL 2       PROMEDIO")
for i in range(len(promedios)):
    print(f"   {notas_p1[i]:2d}              {notas_p2[i]:2d}              {promedios[i]:.2f}")