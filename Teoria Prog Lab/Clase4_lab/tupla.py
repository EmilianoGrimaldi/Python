#tupla
#Es inmutable --> no se puede modificar
#Sirve xq es mas rapida para leerlo nomas
#puedo transformar la tupla(freeze) en una lista la modifico(desfreeze) y la vuelvo a transformar en tupla(freeze)
#Es una lista constante
# t1 = (1,2,3,4,5,"tupla")
# t2 = 1, 2, 3, 4, 5, 6
t3 = tuple([2,3,4,5])

# print(type(t1))
# print(type(t2))
print(type(t3))
print("################")
li = list(t3)
# print(t1)
# print(t2)
print(type(li))
print("################")
tu = tuple(li)
print(type(tu)) 
print("################")
for item in t3:
    print(item)
print("################")
print(t3.count(10))
print("################")
print(t3.index(3))
print("################")
print(5 in t3)