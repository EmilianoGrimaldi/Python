
"""
#TEXTO
todo es texto (ascii)
corta el binario en pedazos de 8 bits (1 byte)
para leerlo pasa cada uno de esos bytes por el codigo ascii
#(texto plano)
Un txt, html, js, py
Es algo que podemos abrir con cualquier procesador de texto, todo lo que contiene es codigo ascii

#ARCHIVO BINARIO
- combinaciones de texto ascii con cosas en complemento a2, dir de memoria 
"""
#MODO APERTURA
# path relativo / absoluto
"""
relativo -> encontrar el archivo desde donde estamos parados
absoluto -> desde la unidad de almacenamiento, todas las carpetas hasta donde esta el archivo
la direccion exacta
"""
""" 
"r" read (lectura de texto)
"w" write (escritura texto)
"rb" lectura binaria
"wb" escritura binaria
"a" append 
"ab" append pero en archivo binario
"""

# archivo = open(r"Teoria Prog Lab\Archivos\hola.txt","r")
lista = []

with open(r"Teoria Prog Lab\Archivos\hola.txt","r") as archivo:
# contenido = archivo.read()
# contenido = contenido.split("\n")
# contenido = archivo.readline()
    for linea in archivo:
        lista.append(linea.replace("\n",""))
# for linea in contenido:
#     print(linea, end="")
# for i in range(len(lineas)):
#     # lineas[i] = lineas[i].replace("\n","")
#     lineas[i] = lineas[i].strip("\n")

print(lista)

