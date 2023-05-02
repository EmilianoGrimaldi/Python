from data import *
from funciones_peliculas import *
#13. Crear una lista de diccionarios que contenga información sobre 5 películas, incluyendo título, director, año de estreno, género y duración en minutos. 
#Luego, pedir al usuario que ingrese una duración máxima y mostrar por consola los títulos de las películas que no excedan esa duración ordenado alfabéticamente por nombre de la pelicula (pueden usar listas auxiliares para guardar datos).

duracion_maxima = input("Ingrese la duracion maxima de la pelicula\n")
lista_peliculas_duracion = filtrar_pelicula_duracion(lista_peliculas,duracion_maxima,"duracion","titulo")
lista_peliculas_duracion.sort()
mostrar_titulos(lista_peliculas_duracion,"TITULO")
