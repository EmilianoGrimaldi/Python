#3- Realizar una carga indefinida de números, añadirlos a una lista e indicar que posición de memoria es la que mas ocurrencias tiene dentro de esa lista.

#bucle hasta que el usuario quiera cargar numeros

seguir = "s"
lista_numeros = []
bandera_max_ocurrencias = True

while seguir == "s":
    while True:
        try:
            numero = int(input("Ingrese un numero: "))
            break 
        except ValueError:
            print("Ingresaste una letra en ves de un entero")
    #Agrego los numeros al final de la lista
    lista_numeros.append(numero)
    #Busco el numero max de ocurrencias
    for elemento in lista_numeros:
      if bandera_max_ocurrencias == True or ocurrencias > max_ocurrencias:
        ocurrencias = lista_numeros.count(elemento)
        elemento_mas_ocurrencias = elemento
        max_ocurrencias = ocurrencias
        bandera_max_ocurrencias = False
    
    seguir = input("Para seguir ingrese 's'. O presione cualquier tecla para salir\n")

# Imprimimos el elemento que aparece con mayor frecuencia y su cantidad de ocurrencias
print("El elemento que más se repite es:", elemento_mas_ocurrencias)
print("Se repite", max_ocurrencias, "veces")

# Para encontrar la posición de memoria del elemento con más ocurrencias,
# puedes utilizar el método `index()` para buscar su primera aparición en la lista:
posicion = lista_numeros.index(elemento_mas_ocurrencias)
print("La posición del elemento que más se repite es:", posicion)
