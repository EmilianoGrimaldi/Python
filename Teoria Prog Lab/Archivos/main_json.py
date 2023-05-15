import json

persona_string = '{"id": 1, "nombre": "Juan", "edad": 40}'
print(type(persona_string))
persona_dict = json.loads(persona_string)
print(type(persona_dict))
persona_json = json.dumps(persona_dict, indent=2)
print(type(persona_json))
print(persona_json)