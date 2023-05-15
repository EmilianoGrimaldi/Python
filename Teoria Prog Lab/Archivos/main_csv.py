lista_personas = []

with open("Teoria Prog Lab\Archivos\personas.csv","r") as file:
    
    for line in file:
        line = line.replace("\n","")
        lista_personas.append(line.split(","))
        
        
    
for persona in lista_personas:
    print(persona)