# init funcion que inicializa la clase
#PascalCase
#camelCase
#snake_case

class Persona:
    def __init__(self, id:int, nombre:str, apellido:str, edad:int) -> None:
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

Persona_yo = Persona(1,"Emiliano", "Grimaldi", 23)
Persona_amigo = Persona(2,"Federico", "Scopelliti", 27)

print(type(Persona_yo))
print(type(Persona))
