from mis_funciones import *
#12. Crear una lista de diccionarios que contenga información sobre 5 libros, incluyendo título, autor, editorial, año de publicación, y género. Luego, pedir al usuario que ingrese un género y mostrar en pantalla todos los títulos de ese género con todos los datos

lista_libros = []

for libro in range(5):
    libro = {}
    libro["titulo"] = input("Ingrese titulo del libro\n")
    libro["autor"] = input("Ingrese autor\n")
    libro["editorial"] = input("Ingresar editorial\n")
    libro["año_publicacion"] = pedir_entero("Ingresar año de publicacion\n")
    libro["genero"] = input("Ingresar genero del libro\n")

    lista_libros.append(libro)

# pedir al usuario que ingrese un género y mostrar en pantalla todos los títulos de ese género con todos los datos
genero_libro = input("Ingresar genero del libro a buscar\n")

lista_genero = []
esta_libro = True
for libro in lista_libros:
    if genero_libro == libro["genero"]:
        esta_libro = False
        lista_genero.append(libro)

if not esta_libro:
    for libro in lista_genero:
        print(libro)
else:
    print("No existe ese genero de libro")