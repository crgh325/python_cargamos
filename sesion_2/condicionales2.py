"""
Dado el sueldo actual de un empleado
si este es menor a $8000.00 se incrementa un 12%
en caso contratio es el 8%. Al final mostrar el aumento y su nuevo sueldo

"""

# 1 entrada de datos
#sueldo = float(input("Ingrese el sueldo del trabajador: $"))

# 2 evaluar
# if sueldo < 8000:
#     aumento = sueldo*0.12
# else:
#     aumento = sueldo*0.08
# nuevo_sueldo = sueldo + aumento
# print(f'El Aumento es ${aumento:.2f}, el nuevo sueldo es: ${nuevo_sueldo:.2f}')


"""
*CATEGORIAS
RECURSOS HUMANOS = 3
CONTABILIDAD = 5

"""
codigo_empleado = input("Ingrese el codigo del empleado: ")
categoria = int(input("Ingrese la categoria: "))
antiguedad = int(input("Ingrese los años de antiguedad: "))
#flag= bandera
respuesta = False
if categoria == 3 or categoria == 5:
    if antiguedad >= 5:
        respuesta = True
elif categoria == 2 and antiguedad >= 10:
    respuesta = True
if respuesta:
    resultado = "Reune las caracteristicas para el puesto"
else:
    resultado = " No reunes las caracteristicas para el puesto"
    print(f'El Empleado con código {codigo_empleado}' + resultado)
