from funciones import *

#5. Crear un diccionario que contenga los nombres de 20 estudiantes y sus respectivas notas en un examen. Luego imprimir el nombre del estudiante con la nota más alta.

bandera_nota = True
alumnos = []

for i in range(3):
    #Dic vacio para crear un dic en cada iteracion y guardar los datos
    dic_notas = {}
    #Carga de datos validados
    dic_notas["nombre_alumno"] = pedir_string_espacio("Ingrese nombre del alumno\n")
    dic_notas["nota"] = pedir_entero_rango("Ingrese nota entre 1 - 10\n", 0, 11)
    #Agrego los dic a la lista para recorrerlos mas tarde
    alumnos.append(dic_notas)

for estudiante in alumnos:
    if bandera_nota or estudiante["nota"] >= nota_max:
        nota_max = estudiante["nota"]
        nombre_nota_max = estudiante["nombre_alumno"]
        bandera_nota = False

for estudiante in alumnos:
    if nota_max == estudiante["nota"]:
        print(f"{estudiante['nombre_alumno']} --> {estudiante['nota']}")