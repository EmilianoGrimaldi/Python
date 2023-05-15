import json

with open(r"Teoria Prog Lab\Archivos\personas.json","r") as archivo:
    
    lista = json.load(archivo)
    
print(lista)