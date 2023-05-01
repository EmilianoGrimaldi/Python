# 10)Se necesita un programa que solicite al usuario que ingrese una lista de números enteros de tamaño N. El programa deberá remover el valor máximo y mínimo de la lista y luego calcular y mostrar el promedio de los valores restantes y determinar si el promedio es mayor o menor que la diferencia entre el máximo y el mínimo valor previamente removido.

lista_numeros = []
flag_mayor = True
flag_menor = True
acumulador_num = 0

while True:
    while True:
        try:
            numero = int(input("Ingrese un numero\n"))
            lista_numeros.append(numero)
            break
        except ValueError:
            print("No ingresaste un caracter numerico")
            
    while True:
        continuar = input("Desea continuar cargando numeros s/n\n").lower()
        if continuar == "s" or continuar == "n":
            break
               
    if continuar == "n":
        break
    
#El programa deberá remover el valor máximo y mínimo de la lista
for indice in range(len(lista_numeros)):
    if flag_mayor or lista_numeros[indice] >= num_maximo:
        num_maximo = lista_numeros[indice]
        indice_max = indice
        flag_mayor = False
    
    if flag_menor or lista_numeros[indice] <= num_minimo:
        num_minimo = lista_numeros[indice]
        indice_min = indice
        flag_menor = False

if len(lista_numeros) > 1:
    diferencia_max_min = num_maximo - num_minimo
    lista_numeros.remove(num_maximo)
    lista_numeros.remove(num_minimo) 
    #  luego calcular y mostrar el promedio de los valores restantes
    for num in lista_numeros:
        acumulador_num += num
        
    if len(lista_numeros) > 0:
        promedio_num = acumulador_num / len(lista_numeros)
        #determinar si el promedio es mayor o menor que la diferencia entre el máximo y el mínimo valor previamente removido
        if promedio_num > diferencia_max_min:
            print("El promedio es mayor que la diferencia entre el max y el min")
        else:
            if promedio_num < diferencia_max_min:
                print("El promedio es menor que la diferencia entre el max y el min")
            else:
                print("El promedio y la diferencia son iguales")
    else:
        print("La lista esta vacia")   
else:
    print("No se ingresaron valores suficientes para determinar max y min")   
     





