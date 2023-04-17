#8. Crear un diccionario que contenga los nombres, edades, salario por día, días trabajados de 10 empleados. Luego, calcular el salario total de cada empleado y agregarlo al diccionario. Finalmente, imprimir en consola los nombres de los empleados junto con la edad y el salario total.
from funciones import *
from funciones_ejercicio import *

empleados = []

for empleado in range(2):
    un_empleado = {}
    un_empleado['nombre'] = pedir_string("Ingrese nombre del empleado\n")
    un_empleado['edad'] = pedir_entero_rango("Ingrese edad del empleado [18 - 65]\n",17,66)
    un_empleado['salario_diario'] = pedir_flotante("Ingrese salario diario del empleado\n")
    un_empleado['dias_trabajados'] = pedir_entero("Ingrese cuantos dias trabajó'\n")
    un_empleado['salario_total'] = calcular_salario_total(un_empleado['salario_diario'],un_empleado['dias_trabajados'])

    empleados.append(un_empleado)

for empleado in empleados:
    print(f"{empleado['nombre']}    -->  {empleado['edad']}   -->   {empleado['salario_total']}")