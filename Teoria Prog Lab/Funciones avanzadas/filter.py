numeros = [4, 5, 2, 8, 7, 9]

pares = []
def esPar(valor)-> bool:
    return valor % 2 == 0

#filter me devuelve bool TRUE o FALSE
  
pares = list(filter(lambda valor: valor % 2 == 0, numeros))  
     
print(esPar(47))
print(pares)
