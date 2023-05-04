# # METODOS CADENAS

# 1. capitalize(): Convierte la primera letra de una cadena en mayúscula y el resto en minúsculas.
# Ejemplo: 
# ```
# texto = "hola, ¿cómo estás?"
# print(texto.capitalize())
# # Output: Hola, ¿cómo estás?
# ```

# 2. casefold(): Convierte la cadena a minúsculas y elimina cualquier caracter que pueda tener varias representaciones, como las letras con acentos o diacríticos.
# Ejemplo:
# ```
# texto = "Höla, ¿cómo estás?"
# print(texto.casefold())
# # Output: hola, ¿cómo estás?
# ```

# 3. center(width[, fillchar]): Devuelve la cadena centrada dentro de una cadena de longitud "width". Opcionalmente, se puede especificar un caracter fillchar para rellenar el espacio vacío.
# Ejemplo:
# ```
# texto = "Hola"
# print(texto.center(10, "-"))
# # Output: --Hola---
# ```

# 4. count(sub[, start[, end]]): Devuelve el número de ocurrencias de la subcadena "sub" en la cadena. Se pueden especificar los índices de inicio y finalización.
# Ejemplo:
# ```
# texto = "La casa de la pradera"
# print(texto.count("a"))
# # Output: 5
# ```

# 5. encode(encoding[, errors]): Codifica la cadena utilizando el método de codificación especificado y devuelve una cadena de bytes.
# Ejemplo:
# ```
# texto = "hola"
# texto_encoded = texto.encode("utf-8")
# print(texto_encoded)
# # Output: b'hola'
# ```

# 6. endswith(suffix[, start[, end]]): Devuelve True si la cadena termina con la subcadena "suffix". Se pueden especificar los índices de inicio y finalización.
# Ejemplo:
# ```
# texto = "Hola, ¿cómo estás?"
# print(texto.endswith("?"))
# # Output: True
# ```

# 7. expandtabs([tabsize]): Reemplaza los caracteres de tabulación en la cadena por un número específico de espacios (8 por defecto).
# Ejemplo:
# ```
# texto = "Hola\tamigo"
# print(texto.expandtabs(4))
# # Output: Hola    amigo
# ```

# 8. find(sub[, start[, end]]): Devuelve el índice de la primera ocurrencia de la subcadena "sub" en la cadena. Si no se encuentra, devuelve -1. Se pueden especificar los índices de inicio y finalización.
# Ejemplo:
# ```
# texto = "Hola, ¿cómo estás?"
# print(texto.find(","))
# # Output: 4
# ```

# 9. format(*args, **kwargs): Formatea la cadena con los argumentos proporcionados y los sustituye en las llaves {} de la cadena.
# Ejemplo:
# ```
# texto = "Hola, {} ¿cómo estás?".format("amigo")
# print(texto)
# # Output: Hola, amigo ¿cómo estás?
# ```

# 10. format_map(mapping): Reemplaza las llaves `{}` en la cadena con las claves y valores especificados en el diccionario de mapeo. Este método es similar al método `format()` pero utiliza un diccionario en lugar de argumentos posicionales.
# Ejemplo:
# ```
# punto = {'x': 4, 'y': -5}
# cadena = "Las coordenadas son ({x}, {y})".format_map(punto)
# print(cadena)
# # Output: "Las coordenadas son (4, -5)"
# ```


# 11. index(sub[, start[, end]]): Devuelve el índice de la primera ocurrencia de la subcadena "sub" en la cadena. Si no se encuentra, genera una excepción ValueError. Se pueden especificar los índices de inicio y finalización.
# Ejemplo:
# ```
# texto = "Hola, ¿cómo estás?"
# print(texto.index(","))
# # Output: 4
# ```

# 12. isalnum(): Devuelve True si la cadena es alfanumérica, es decir, si solo contiene letras y números.
# Ejemplo:
# ```
# texto = "Hola123"
# print(texto.isalnum())
# # Output: True
# ```

# 13. isalpha(): Devuelve True si la cadena solo contiene letras.
# Ejemplo:
# ```
# texto = "Hola"
# print(texto.isalpha())
# # Output: True
# ```

# 14. isdecimal(): Devuelve True si la cadena solo contiene dígitos decimales (0-9).
# Ejemplo:
# ```
# texto = "123"
# print(texto.isdecimal())
# # Output: True
# ```

# 15. isdigit(): Devuelve True si la cadena solo contiene dígitos. Además de los dígitos decimales, también incluye caracteres como los superíndices y subíndices numéricos.
# Ejemplo:
# ```
# texto1 = "123"
# texto2 = "²34"
# print(texto1.isdigit())
# # Output: True
# print(texto2.isdigit())
# # Output: True
# ```

# 16. isidentifier(): Devuelve True si la cadena es un identificador válido en Python, es decir, si cumple con las reglas de nomenclatura de variables.
# Ejemplo:
# ```
# texto1 = "nombre"
# texto2 = "2nombre"
# print(texto1.isidentifier())
# # Output: True
# print(texto2.isidentifier())
# # Output: False
# ```

# 17. islower(): Devuelve True si todas las letras de la cadena están en minúscula.
# Ejemplo:
# ```
# texto = "hola"
# print(texto.islower())
# # Output: True
# ```

# 18. isnumeric(): Devuelve True si la cadena solo contiene caracteres numéricos, incluidos los caracteres numéricos de otros sistemas de escritura.
# Ejemplo:
# ```
# texto1 = "123"
# texto2 = "٣٤٥"
# print(texto1.isnumeric())
# # Output: True
# print(texto2.isnumeric())
# # Output: True
# ```

# 19. isprintable(): Devuelve True si todos los caracteres de la cadena son imprimibles, es decir, si no son caracteres de control.
# Ejemplo:
# ```
# texto1 = "Hola"
# texto2 = "Hola\n"
# print(texto1.isprintable())
# # Output: True
# print(texto2.isprintable())
# # Output: False
# ```

# 20. isspace(): Devuelve True si la cadena solo contiene caracteres de espacio en blanco (espacios, tabulaciones, saltos de línea, etc.).
# Ejemplo:
# ```
# texto1 = "   "
# texto2 = "   \n"
# print(texto1.isspace())
# # Output: True
# print(texto2.isspace())
# # Output: True
# ```

# 21. istitle(): Devuelve True si la cadena está en formato de título, es decir, si todas las palabras comienzan con mayúscula y el resto de las letras están en minúscula.
# Ejemplo:
# ```
# texto1 = "Hola Mundo"
# texto2 = "Hola mundo"
# print(texto1.istitle())
# # Output: True
# print(texto2.istitle())
# # Output: False
# ```

# 22. isupper(): Devuelve True si todas las letras de la cadena están en mayúscula.
# Ejemplo:
# ```
# texto = "HOLA"
# print(texto.isupper())
# # Output: True
# ```

# 23. join(iterable): Devuelve una cadena que es la concatenación de los elementos del iterable, separados por la cadena que llama al método.
# Ejemplo:
# ```
# separador = "-"
# cadena = separador.join(["hola", "mundo"])
# print(cadena)
# # Output: "hola-mundo"
# ```

# 24. ljust(width[, fillchar]): Devuelve la cadena justificada a la izquierda en una cadena de ancho fijo, rellenando los espacios faltantes con caracteres de relleno (por defecto, espacios en blanco).
# Ejemplo:
# ```
# texto = "hola"
# ancho = 10
# relleno = "-"
# cadena = texto.ljust(ancho, relleno)
# print(cadena)
# # Output: "hola------"
# ```

# 25. lower(): Devuelve una copia de la cadena con todas las letras en minúscula.
# Ejemplo:
# ```
# texto = "HOLA"
# print(texto.lower())
# # Output: "hola"
# ```

# 26. lstrip([chars]): Devuelve una copia de la cadena con los caracteres iniciales especificados eliminados (por defecto, los espacios en blanco).
# Ejemplo:
# ```
# texto = "   hola   "
# print(texto.lstrip())
# # Output: "hola   "
# ```

# 27. maketrans(x[, y[, z]]): Devuelve un diccionario que se puede usar con el método translate() para reemplazar caracteres.
# Ejemplo:
# ```
# from_str = "aeiou"
# to_str = "12345"
# tabla = str.maketrans(from_str, to_str)
# texto = "hola mundo"
# print(texto.translate(tabla))
# # Output: "h4l1 m3nd4"
# ```

# 28. partition(sep): Divide la cadena en una tupla con tres elementos: la parte antes del separador, el separador en sí y la parte después del separador. Si el separador no se encuentra, la tupla contiene la cadena original y dos cadenas vacías.
# Ejemplo:
# ```
# texto = "hola,mundo"
# print(texto.partition(","))
# # Output: ("hola", ",", "mundo")
# ```

# 29. replace(old, new[, count]): Devuelve una copia de la cadena con todas las ocurrencias de "old" reemplazadas por "new". Se puede especificar el número máximo de reemplazos a realizar.
# Ejemplo:
# ```
# texto = "hola mundo"
# print(texto.replace("o", "0"))
# # Output: "h0la mund0"
# ```

# 30. rfind(sub[, start[, end]]): Devuelve el índice de la última ocurrencia de la subcadena "sub" en la cadena. Si no se encuentra, devuelve -1. Se pueden especificar los índices de inicio y fin de la búsqueda.
# Ejemplo:
# ```
# texto = "hola mundo"
# print(texto.rfind("o"))
# # Output: 7
# ```

# 31. rindex(sub[, start[, end]]): Funciona igual que rfind(), pero si no se encuentra la subcadena, genera una excepción ValueError en lugar de devolver -1.
# Ejemplo:
# ```
# texto = "hola mundo"
# print(texto.rindex("o"))
# # Output: 7
# ```

# 32. rjust(width[, fillchar]): Devuelve la cadena justificada a la derecha en una cadena de ancho fijo, rellenando los espacios faltantes con caracteres de relleno (por defecto, espacios en blanco).
# Ejemplo:
# ```
# texto = "hola"
# ancho = 10
# relleno = "-"
# cadena = texto.rjust(ancho, relleno)
# print(cadena)
# # Output: "------hola"
# ```

# 33. rpartition(sep): Divide la cadena en una tupla con tres elementos: la parte antes del separador, el separador en sí y la parte después del separador. La búsqueda comienza desde el final de la cadena. Si el separador no se encuentra, la tupla contiene dos cadenas vacías y la cadena original.
# Ejemplo:
# ```
# texto = "hola,mundo"
# print(texto.rpartition(","))
# # Output: ("hola", ",", "mundo")
# ```

# 34. rsplit([sep[, maxsplit]]): Devuelve una lista de las palabras en la cadena, separadas por el separador especificado (por defecto, los espacios en blanco). La búsqueda comienza desde el final de la cadena. Se puede especificar el número máximo de separaciones a realizar.
# Ejemplo:
# ```
# texto = "hola mundo"
# print(texto.rsplit())
# # Output: ["hola", "mundo"]
# ```

# 35. rstrip([chars]): Devuelve una copia de la cadena con los caracteres finales especificados eliminados (por defecto, los espacios en blanco).
# Ejemplo:
# ```
# texto = "   hola   "
# print(texto.rstrip())
# # Output: "   hola"
# ```

# 36. split([sep[, maxsplit]]): Devuelve una lista de las palabras en la cadena, separadas por el separador especificado (por defecto, los espacios en blanco). Se puede especificar el número máximo de separaciones a realizar.
# Ejemplo:
# ```
# texto = "hola mundo"
# print(texto.split())
# # Output: ["hola", "mundo"]
# ```

# 37. splitlines([keepends]): Devuelve una lista de las líneas en la cadena, separadas por los caracteres de salto de línea. Si keepends es True, los caracteres de salto de línea se incluyen al final de cada línea.
# Ejemplo:
# ```
# texto = "hola\nmundo"
# print(texto.splitlines())
# # Output: ["hola", "mundo"]
# ```

# 38. startswith(prefix[, start[, end]]): Devuelve True si la cadena comienza con el prefijo especificado. Se pueden especificar los índices de inicio y fin de la búsqueda.
# Ejemplo:
# ```
# texto = "hola mundo"
# print(texto.startswith("h"))
# # Output: True
# ```

# 39. strip([chars]): Devuelve una copia de la cadena con los caracteres iniciales y finales especificados eliminados (por defecto, los espacios en blanco).
# Ejemplo:
# ```
# texto = "   hola   "
# print(texto.strip())
# # Output: "hola"
# ```

# 40. swapcase(): Devuelve una copia de la cadena con las mayúsculas convertidas en minúsculas y viceversa.
# Ejemplo:
# ```
# texto = "HoLa MuNdO"
# print(texto.swapcase())
# # Output: "hOlA mUnDo"
# ```

# 41. title(): Devuelve una copia de la cadena con la primera letra de cada palabra convertida a mayúscula y el resto a minúscula.
# Ejemplo:
# ```
# texto = "hola mundo"
# print(texto.title())
# # Output: "Hola Mundo"
# ```

# 42. translate(table): Devuelve una copia de la cadena donde se reemplazan los caracteres según la tabla de traducción especificada. La tabla debe ser un objeto de la clase bytes, bytearray o dict.
# Ejemplo:
# ```
# texto = "hola mundo"
# tabla = str.maketrans("aeiou", "12345")
# print(texto.translate(tabla))
# # Output: "h1l1 m5nd4"
# ```

# 43. upper(): Devuelve una copia de la cadena en mayúsculas.
# Ejemplo:
# ```
# texto = "hola mundo"
# print(texto.upper())
# # Output: "HOLA MUNDO"
# ```

# 44. zfill(width): Devuelve la cadena rellena con ceros a la izquierda hasta alcanzar el ancho especificado.
# Ejemplo:
# ```
# texto = "42"
# ancho = 5
# cadena = texto.zfill(ancho)
# print(cadena)
# # Output: "00042"
# ```

