# from = dede el archivo
# import = importa * todas las librerias

from calculadora import *

# print(suma(12, 5))
# print(resta(10, 6))
# print(multiplicar(4, 6))
# print(dividir(20, 2))

while True:
    a = float(input("ingrese el valor del primer numero: "))
    b = float(input("ingrese el valor del segundo numero: "))
    menu = "Ingrese la operación a ejecutar: \n 1) suma \n 2) resta \n 3) multiplicacion \n 4) division \n 5) salir \n"
    opcion = input(menu)
    if opcion == "1":
        print(suma(a, b))
    elif opcion == "2":
        print(resta(a, b))
    elif opcion == "3":
        print(multiplicar(a, b))
    elif opcion == "4":
        print(dividir(a, b))
    elif opcion == "5":
        print("Adios!")
        break
    else:
        print("la operación ingresada es invalida")
