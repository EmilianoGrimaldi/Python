# init funcion que inicializa la clase
#objeto es un tipo de dato creada por un programador
#un objeto es una representación de una cosa o entidad del mundo real en la programación, con características (datos) y acciones (métodos) asociadas.
# una funcion esta definida de forma global y un metodo es una funcion definida dentro de un objeto para trabajar con ese objeto depende donde lo defina es una cosa u otra
# las variables dentro de un objeto se les llama atributos

#PascalCase
#camelCase
#snake_case

class Persona:
   
    def __init__(self, id:int, nombre:str, apellido:str, edad:int) -> None:
    #Metodo init reserva o pide un espacio en memoria para crear un objeto
    #es un método especial  que se utiliza para inicializar objetos de una clase (metodo constructor)
    # self guarda la direccion de memoria donde se construyo esa clase
    #El metodo constructor: Consigue espacio en memoria con "self" y se encarga de recibir los valores e inicializarlos
        self.id = id # self en una direccion de memoria
        self.__nombre = nombre.capitalize() # cuando pongo self le digo q quiero que esa variable se guarde en esa direccion de memoria
        self._apellido = apellido.capitalize() #protegido
        self.__edad = edad # __ para transformar en privado un atributo

        #print(self) # la direccion de memoria de esta clase Persona (0x0000020194FEED10)
        #print(self.id) # la id que le pase por parametro
    # @property
    # def edad(self):
    #     return self.__edad

    # @edad.setter
    # def edad(self, value:int):
    #     if type(value) == int and value > 0:
    #         self.__edad = value

    def set_edad(self, value:int):
        if type(value) == int and value > 0:
            self.__edad = value

    def get_edad(self):
        return self.__edad
    
    # @property
    # def nombre(self):
    #     return self.__nombre

    # @nombre.setter
    # def nombre(self, value:str):
    #         self.__nombre = value.capitalize()
    
    def set_nombre(self, value:str):
        if value.isalpha():
            self.__nombre = value.capitalize()

    def get_nombre(self):
        return self.__nombre

    def presentarse(self):
        return f"Hola soy {self.__nombre} y tengo {self.__edad} años"
    
#herencia unica
#herencia
#Los atributos protegidos funcionan como privados para el exterior, pero publicos para la herencia
class Empleado(Persona):
    def __init__(self, id: int, nombre: str, apellido: str, edad: int, sueldo:float) -> None:
        super().__init__(id, nombre, apellido, edad)
        self.sueldo = sueldo

    def presentarse(self):
        return f"Hola soy un empleado me llamo {self.get_nombre()} y gano ${self.sueldo}"
    
#Esa clase la llamo como si fuera una funcion
Persona_1 = Persona(1,"alberto", "Grimaldi", 23) #persona_1 se encuentra en la memoria estatica y se guarda la direccion de memoria del la clase persona. Seria la misma direccion de memoria
empleado_1 = Empleado(1,"emiliano", "Grimaldi", 55, 255)
print(empleado_1.presentarse())
# print(Persona_1.get_nombre())
# Persona_2 = Persona(2,"Indiana", "Jones", 50)
# print(type(Persona_1)) #<class '__main__.Persona'>  _main_ -> modulo.clase Persona 
# print(Persona_1) # Persona object(objeto persona) at 0x0000020194FEED10 -> self (direccion de memoria)

# print(Persona_1.id)
# print(Persona_2.id)

# lista = []
# lista.append(Persona_1)
# lista.append(Persona_2)
# print(lista)

# El encapsulamiento tiene varios beneficios:
# Protección de datos: Al encapsular los atributos de una clase, se evita que se acceda directamente a ellos y se modifiquen de manera incorrecta. Los métodos de acceso permiten un control más preciso sobre cómo se accede y se modifica los datos.

# Abstracción: El encapsulamiento permite ocultar los detalles internos de implementación y proporcionar una interfaz simplificada para interactuar con los objetos. Esto facilita el uso de los objetos sin preocuparse por cómo funcionan internamente.

# Reusabilidad: Al encapsular datos y comportamiento en una clase, se pueden crear múltiples instancias de esa clase y reutilizarla en diferentes partes del programa. Esto promueve la reutilización de código y reduce la duplicación.

# print(Persona_1.edad)
# print(Persona_1.presentarse())

# Persona_1.edad = 30

# print(Persona_1.edad)
# print(Persona_1.presentarse())

# print(Persona_1.get_edad())
# print(Persona_1.presentarse())

# Persona_1.set_edad(23)

# print(Persona_1.get_edad())
# print(Persona_1.presentarse())

# print(Persona_2.presentarse())

# print(Persona_1.get_edad())
# Persona_1.set_edad(25)
# print(Persona_1.get_edad())

# print(Persona_1.get_nombre())
# print(Persona_1.presentarse())

# Persona_1.set_nombre("alberto")

# print(Persona_1.get_nombre())
# print(Persona_1.presentarse())
