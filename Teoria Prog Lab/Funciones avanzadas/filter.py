numeros = [4, 5, 2, 8, 7, 9]

pares = []
def esPar(valor)-> bool:
    return valor % 2 == 0

#filter me devuelve bool TRUE o FALSE
  
pares = list(filter(lambda valor: not valor % 2, numeros))  
     
print(esPar(47))
print(pares)