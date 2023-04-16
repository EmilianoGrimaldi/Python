from lista_alumnos import *
#5. Crear un diccionario que contenga los nombres de 20 estudiantes y sus respectivas notas en un examen. Luego imprimir el nombre del estudiante con la nota más alta.

bandera_nota = True

for estudiante in lista_estudiantes:
    if bandera_nota or estudiante["nota"] >= nota_max:
        nota_max = estudiante["nota"]
        nombre_nota_max = estudiante["nombre"]
        bandera_nota = False

for estudiante in lista_estudiantes:
    if nota_max == estudiante["nota"]:
        print(f"{estudiante['nombre']} --> {estudiante['nota']}")