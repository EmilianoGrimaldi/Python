# 12/4/23
# DICCIONARIOS (otra estructura de datos)

# lista = [1, 2, 3]
# diccionario = {"nota1": 2, "nota2": 4, "promedio": 2.0}
# diccionario tam 3
# clave - valor
# print(type(diccionario))
# print(diccionario)
# print(diccionario["nota1"])
# print(diccionario["nota2"])
# print(diccionario["promedio"])

# los diccionarios no estan ordenados y no necesitan estar ordenados xq accedemos a el por su clave

# for elemento in lista:
#    print(elemento)
# print("---------------------------")

# for clave in diccionario:
#     print(clave)

# print("---------------------------")

# for clave in diccionario:
#     print(diccionario[clave])

# print("---------------------------")

# for clave in diccionario:
#     print(clave, diccionario[clave])

alumno = {
    "legajo": 103450,
    "nombre": "Juan",
    "apellido": "Perez",
    "email": "juancito@gmail.com",
    "edad": 20
}

# print(alumno)
# print(alumno["nombre"])
# print(id(alumno))

# print("#############################")

# alumno["nombre"] = "Emiliano"
# print(alumno["nombre"])
# print(alumno)
# print(id(alumno))

# alumno["localidad"] = "Avellaneda"
# print(alumno)

# del alumno["email"]
# print(alumno)

# METODOS DICCIONARIO
# print(alumno.keys())
# for key in alumno.keys():
#     print(key)
# print("##############################")
# for valor in alumno.values():
#     print(valor)
# print("##############################")
# print(alumno["nombre"])
# print(alumno.get("nombre"))
# campo = "nombre"
# print(alumno[campo])
# print(alumno.get(campo))
# SI QUIERO ENTRAR A UN CAMPO QUE NO TENGO VA A APARECER UNA EXCEPCION KEY ERROR

notas = []

# carga de notas
for i in range(2):
    dic = {}
    auxInt = int(input("Ingrese nota parcial 1\n"))
    dic["nota1"] = auxInt

    auxInt = int(input("Ingrese nota parcial 2\n"))
    dic["nota2"] = auxInt

    dic["promedio"] = (dic["nota1"] + dic["nota2"]) / 2

    notas.append(dic)

# print(notas)
print("PARCIAL 1        PARCIAL 2       PROMEDIO")
for calificacion in notas:
    print(
        f"{calificacion['nota1']:2d} {calificacion['nota2']:2d} {calificacion['promedio']:.2f}")


# Funciones
# para definir una funcion
# puede devolver algo o no devolver nada

# cuerpo o desarrollo de la funcion
# def saludar():
#     print("Hola")

# def saludar(nombre):
#     print(f"Hola {nombre}")

# Para q me devuelva
# def sumar(a, b):
#     return a + b

# Llamado o la invocacion de la funcion
# saludar()
# saludar("Fede")
# x = sumar(4,5)
# x = sumar(19,5)
# print(x)
