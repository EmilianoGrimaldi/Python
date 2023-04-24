def cargar_lista(lista_origen, lista_destino):

    for item in lista_origen:
        lista_destino.append(item)

def menu(titulo:str,opciones:str)->str:
    print("####             {}             ####\n".format(titulo))
    print("-----------------------------------------------------\n")
    print(opciones)
    opcion = input("Ingrese una opcion\n")
    return opcion

def mostrar_persona(persona):
    print(f'    {persona["id"]:2d}      {persona["nombre"] + " " + persona["apellido"]:20s}     {persona["email"]:33}      {persona["genero"]:^2s}        {persona["edad"]:2d}')

def mostrar_personas(lista):
    print("####             LISTA DE PERSONAS             ####\n")
    print("------------------------------------------------------------------------------------------------------\n")
    print("    ID         NOMBRE                        EMAIL                        GENERO     EDAD")
    print("------------------------------------------------------------------------------------------------------\n")
    for persona in lista:
        mostrar_persona(persona)

