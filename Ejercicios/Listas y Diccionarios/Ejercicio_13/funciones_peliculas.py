def encabezado()->None:
    print(f'       TITULO                        DIRECTOR         AÑO DE ESTRENO               GENERO                  DURACION\n')

def mostrar_una_pelicula(pelicula)->None:
    print(f"    {pelicula['titulo']:30s}{pelicula['director']:25s}{pelicula['anio_estreno']:20s}{pelicula['genero']:30s}{pelicula['duracion']:3s}")

def mostrar_peliculas(peliculas:list)->None:
    for pelicula in peliculas:
        mostrar_una_pelicula(pelicula)


def filtrar_pelicula_duracion(lista:list, duracion_ingresada:str, campo_comparar:str, campo_guardar:str)->None:
    lista_filtrada = []
    for item in lista:
        if item[campo_comparar] <= duracion_ingresada:
            lista_filtrada.append(item[campo_guardar])
    
    return lista_filtrada

def mostrar_titulos(lista:list, encabezado:str)->None:
    print(f'       {encabezado}\n')
    for item in lista:
        print(f"       {item}")