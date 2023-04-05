################ Listas (Estructura de datos) #################
#Las listas son una estructura de datos que te permiten almacenar una colección ordenada de elementos, como números, cadenas de texto, objetos, entre otros.

# Las listas se crean utilizando corchetes [], con los elementos separados por comas.

# Los elementos en una lista pueden ser accedidos a través de un índice, comenzando desde cero. Por ejemplo, el primer elemento de una lista se puede acceder utilizando el índice 0.

# Las listas son mutables, lo que significa que puedes agregar, eliminar o cambiar elementos de una lista después de haberla creado.

# Las listas también tienen muchos métodos incorporados, como append(), insert(), remove() y sort(), entre otros, que te permiten modificar la lista de diferentes maneras.
mi_lista = [1, 2, 3, 4, 5]
mi_lista_vacia = []

segundo_elemento = mi_lista[1]  # el índice 1 representa al segundo elemento
print(segundo_elemento)  # esto imprimirá: 2

ultimo_elemento = mi_lista[-1]
print(ultimo_elemento)  # esto imprimirá: 5

mi_lista[2] = 10
print(mi_lista)  # esto imprimirá: [1, 2, 10, 4, 5]

mi_lista.append(6)
print(mi_lista)  # esto imprimirá: [1, 2, 10, 4, 5, 6]

mi_lista.remove(4)
print(mi_lista)  # esto imprimirá: [1, 2, 10, 5, 6]

del mi_lista[2]
print(mi_lista)  # esto imprimirá: [1, 2, 5, 6]

mi_lista = [1, "hola", True, [2, 3, 4]]
print(mi_lista[3][1])  # esto imprimirá: 3

mi_lista = [1, 2, 3, 4, 5]

for elemento in mi_lista:
    print(elemento)

mi_lista = list(range(1, 11))
print(mi_lista)  # esto imprimirá: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mi_lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
#### ORDENAR LISTAS ####
mi_lista.sort() #El método sort() ordena la lista en su lugar (es decir, modifica la lista original), 
print(mi_lista)  # esto imprimirá: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

nueva_lista = sorted(mi_lista) #sorted() devuelve una nueva lista ordenada sin modificar la lista original. 
print(nueva_lista)  # esto imprimirá: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]


mi_lista = [1, 2, 3, 4, 5, 5, 5]

print(mi_lista.count(5))  # esto imprimirá: 3 count() para contar el número de ocurrencias de un elemento en la lista

print(mi_lista.index(3))  # esto imprimirá: 2 index() para encontrar el índice de la primera ocurrencia de un elemento en la lista

mi_lista.extend([6, 7, 8]) #extend() para agregar elementos de otra lista al final de la lista actual.
print(mi_lista)  # esto imprimirá: [1, 2, 3, 4, 5, 5, 5, 6, 7, 8]

###### Suma de listas #####
#Para sumar todos los elementos de una lista en Python, puedes utilizar la función sum(). Esta función toma una lista como argumento y devuelve la suma de todos los elementos de la lista.
mi_lista = [1, 2, 3, 4, 5]
suma = sum(mi_lista)
print(suma)  # esto imprimirá: 15
#la función sum() toma la lista mi_lista como argumento y devuelve la suma de todos sus elementos, que es 15.

#### FOR ####
#También puedes utilizar un bucle for para iterar a través de la lista y sumar manualmente sus elementos.

mi_lista = [1, 2, 3, 4, 5]
suma = 0

for elemento in mi_lista:
    suma += elemento

print(suma)  # esto imprimirá: 15

#inicializamos una variable suma en cero y luego usamos un bucle for para iterar a través de la lista y agregar cada elemento a la suma. Finalmente, imprimimos la suma resultante, que es 15.

#len(). Esta función toma una lista como argumento y devuelve el número de elementos que contiene la lista.
mi_lista = [1, 2, 3, 4, 5]
longitud = len(mi_lista)
print(longitud)  # esto imprimirá: 5
#la función len() toma la lista mi_lista como argumento y devuelve su longitud, que es 5

#for y la función enumerate() para iterar a través de la lista y contar manualmente sus elementos
mi_lista = [1, 2, 3, 4, 5]
longitud = 0

for indice, elemento in enumerate(mi_lista):
    longitud += 1

print(longitud)  # esto imprimirá: 5
#inicializamos una variable longitud en cero y luego usamos un bucle for y la función enumerate() para iterar a través de la lista y contar manualmente cada elemento. Por cada iteración, incrementamos la variable longitud en 1. Finalmente, imprimimos la longitud resultante, que es 5.

###Métodos de lista
#Las listas en Python tienen muchos métodos útiles incorporados que facilitan su manipulación. Algunos de los métodos más comunes incluyen:
# append(): agrega un elemento al final de la lista.
# extend(): agrega todos los elementos de una lista (o cualquier iterador) al final de la lista.
# insert(): inserta un elemento en una posición específica de la lista.
# remove(): elimina la primera aparición de un elemento de la lista.
# pop(): elimina y devuelve el elemento en una posición específica de la lista (o el último elemento si no se especifica la posición).
# index(): devuelve el índice de la primera aparición de un elemento en la lista.
# count(): devuelve el número de veces que aparece un elemento en la lista.
# sort(): ordena los elementos de la lista en orden ascendente (o descendente si se especifica el argumento reverse=True).
# reverse(): invierte el orden de los elementos en la lista.

#########Listas anidadas##########
#Las listas en Python también pueden contener otras listas como elementos. Estas se llaman listas anidadas y se utilizan para representar estructuras de datos más complejas

mi_lista_anidada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#mi_lista_anidada es una lista de tres elementos, donde cada elemento es otra lista de tres elementos. Puedes acceder a los elementos de una lista anidada utilizando índices múltiples

print(mi_lista_anidada[0][1])  # esto imprimirá: 2

###Slice de lista###
# El slicing es una técnica para acceder a una parte de una lista. Puedes acceder a una porción de una lista especificando el índice de inicio, el índice de fin (no inclusive) y un posible paso en la sintaxis [inicio:fin:paso]. Si omites el índice de inicio, Python asume que es el primer elemento de la lista. Si omites el índice de fin, Python asume que es el último elemento de la lista. Si omites el paso, Python asume que es 1. Por ejemplo:

mi_lista = [1, 2, 3, 4, 5]
print(mi_lista[1:4])  # esto imprimirá: [2, 3, 4]

#En este ejemplo, tomamos una porción de mi_lista que va desde el segundo elemento (mi_lista[1]) hasta el cuarto elemento (mi_lista[3]), lo que nos da [2, 3, 4].

#Operadores de lista
# Las listas en Python tienen dos operadores útiles incorporados: in y not in. Estos operadores se utilizan para verificar si un elemento está o no en una lista. Por ejemplo:
mi_lista = [1, 2, 3, 4, 5]
print(3 in mi_lista)  # esto imprimirá: True
print(6 not in mi_lista)  # esto imprimirá: True
# En este ejemplo, utilizamos el operador in para verificar si 3 está en mi_lista. Como 3 está en la lista, el resultado es True. Luego utilizamos el operador not in para verificar si 6 no está en mi_lista. Como 6 no está en la lista, el resultado es True