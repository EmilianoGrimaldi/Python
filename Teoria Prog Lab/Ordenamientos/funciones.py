def ordenar_lista_creciente(lista:list):
    tam = len(lista)
    for i in range(tam-1):
        for j in range(i+1, tam):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def ordenar_lista_decreciente(lista:list):
    tam = len(lista)
    for i in range(tam-1):
        for j in range(i+1, tam):
            if lista[i] < lista[j]: 
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def ordenar_lista(lista:list,creciente = True):
    tam = len(lista)
    for i in range(tam-1):
        for j in range(i+1, tam):
            if (creciente and lista[i] > lista[j]) or (lista[i] < lista[j] and not creciente):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

def ordenar_lista_dic(lista:list,key:str, creciente = True):
    tam = len(lista)
    for i in range(tam-1):
        for j in range(i+1, tam):
            if (creciente and lista[i][key] > lista[j][key]) or (lista[i][key] < lista[j][key] and not creciente):
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
