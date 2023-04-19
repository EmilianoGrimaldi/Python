from funciones import *
from bancarias import *
# 11. Crear un diccionario que contenga los nombres, edades, saldos en cuentas bancarias y un codigo de cliente (debe ser un string de 8 caracteres alfanumérico) y un porcentaje de impuesto a aplicar. Imprimir por consola el codigo del cliente y el balance final de la cuenta.

cuentas_bancarias = []

while True:

    una_cuenta_bancaria = {} 

    una_cuenta_bancaria['nombre'] = pedir_cadena("Ingrese su nombre\n")
    una_cuenta_bancaria['edad'] = pedir_entero_rango("Ingrese su edad [Mayor a 18]\n", 18, 120)
    una_cuenta_bancaria['saldo'] = pedir_entero("Ingresar saldo de cuenta\n")
    while True:
        una_cuenta_bancaria['id_cliente'] = pedir_cadena_alfanumerica("Ingrese codigo de cliente alfanumerico [8 caracteres]\n")
        if len(una_cuenta_bancaria['id_cliente']) == 8:
            break
        else:
            print("El codigo de cliente no cumple con los caracteres requeridos")
    una_cuenta_bancaria['impuesto'] = pedir_entero("Ingresar porcentaje de impuesto a aplicar\n")
    
    calculo_balance = (una_cuenta_bancaria['saldo'] * una_cuenta_bancaria['impuesto'])/100
    una_cuenta_bancaria['balance'] = una_cuenta_bancaria['saldo'] + calculo_balance

    cuentas_bancarias.append(una_cuenta_bancaria)

    seguir = input("Para continuar --> ['s'] y Para salir --> [Cualquier tecla pra salir]\n")
    if seguir != 's':
        seguir = input("Seguro que quiere salir? Para continuar --> ['s'] y Para salir --> [Cualquier tecla pra salir]\n")
        if seguir != 's':
            break

print("\tCODIGO DE CLIENTE\tBALANCE FINAL")
for cliente in cuentas_bancarias:
    print(f"{cliente['id_cliente']:>20} {cliente['balance']:>20}")