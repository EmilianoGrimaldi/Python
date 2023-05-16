import json

persona_string = '{"id": 1, "nombre": "Juan", "edad": 40}'
print(type(persona_string)) # str
persona_dict = json.loads(persona_string)
print(type(persona_dict)) # dict
persona_json = json.dumps(persona_dict, indent=2)
print(type(persona_json)) # str json
print(persona_json)