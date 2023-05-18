# numeros = [4, 5, 2, 3, 7, 9]

# duplicados1 = []

# for numero in numeros:
#     dupli = numero * 2
#     duplicados1.append(dupli)
    

# duplicados = list(map(lambda value: value * 2, numeros))

# print(numeros)
# print(duplicados)
# print(duplicados1)

nombres = ["Juan", "Emiliano", "Federico", "Nahuel"]

def contar_caracteres(cadena:str):
    return len(cadena)

contar_caracteres_v2 = list(map(lambda nombre: len(nombre), nombres))

print(contar_caracteres_v2)