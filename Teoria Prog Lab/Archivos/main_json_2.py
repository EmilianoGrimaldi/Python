import json

with open(r"Teoria Prog Lab\Archivos\personas.json","r") as archivo:
    
    lista = json.load(archivo)
    
print(lista)


# ¡Claro! El módulo `json` de Python proporciona varias herramientas para trabajar con datos JSON. A continuación se detallan algunas de las más comunes:

# 1. `json.dumps()`: convierte un objeto Python en una cadena JSON.
# 2. `json.loads()`: convierte una cadena JSON en un objeto Python.
# 3. `json.dump()`: escribe un objeto Python en un archivo JSON.
# 4. `json.load()`: lee un archivo JSON y devuelve un objeto Python.
# 5. `json.JSONEncoder`: una clase que se puede personalizar para definir la forma en que se codifican los objetos Python en JSON. Se puede subclase para personalizar la codificación de tipos de datos específicos.
# 6. `json.JSONDecoder`: una clase que se puede personalizar para definir la forma en que se decodifican los datos JSON en objetos Python. Se puede subclase para personalizar la decodificación de tipos de datos específicos.
# 7. `ensure_ascii`: un argumento opcional que especifica si se deben escapar los caracteres ASCII no válidos en la salida JSON.
# 8. `indent`: un argumento opcional que especifica la cantidad de espacio en blanco que se utilizará para la indentación en la salida JSON.
# 9. `sort_keys`: un argumento opcional que especifica si las claves en la salida JSON se deben ordenar alfabéticamente.

# Estas herramientas son muy útiles para trabajar con datos JSON en Python. Por ejemplo, `json.dumps()` y `json.loads()` se pueden utilizar para codificar y decodificar datos JSON en aplicaciones web y móviles, mientras que `json.dump()` y `json.load()` se pueden utilizar para leer y escribir archivos JSON en el disco. La personalización de las clases `JSONEncoder` y `JSONDecoder` permite la manipulación de tipos de datos complejos y la personalización de la codificación y decodificación de datos JSON, mientras que los argumentos opcionales `ensure_ascii`, `indent` y `sort_keys` brindan más control sobre el formato de salida JSON.