"""
for .- cuando se conoce el numero de veces que se repetira el bucle
while.cuando el bucle termina cuando sucede un valor true

"""

# for num in range(1, 10, 2):
#   print(num)


# contador = 0
# acumulador = 0
# for x in range(1, 6):
#     sueldo = float(input(f'Ingrese sueldo {x}: '))
#     contador = contador+1
#     acumulador = acumulador + sueldo
#     promedio_sueldo = acumulador / contador
# print(f'La cantidad de empleados procesados es: {contador}')
# print(f'El total de la planilla es: {acumulador}')
# print(f'El promedio de sueldo es: {promedio_sueldo}')
# print("Fin del bucle")

# Break es salir del bucle
# Continue es seguir la secuencia del bucle

# for i in range(1, 10):
#     if i == 7:
#         breakelse
#         continue
#     print(i)

# i = 0
# suma = 0
# while i < 100:
#     i = i+1
#     suma = suma+i
#     print(i)
# print(f'La suma de todos los numero es: {suma}')


# programa que solicite la contraseña de ingreso, si es errada, reintentar, n veces

# from pickle import TRUE

# contador = 0
# contraseña = "python"
# usuario = input('Ingrese el nombre del usuario: ')
# while True:
#     con = input('Ingrese la contraseña: ')
#     if con == contraseña:
#         print(f'Bienvenido al sistema {usuario}')
#         break
#     else:
#         contador = contador + 1
#         print(f'La contraseña es errada, vuelva a intertarlo {contador}')
#         if contador == 3:
#             print("Supero los intentos, se bloqueara el acceso")
#             break


# import random
# numero_secreto = random.randint(1, 100)
# intentos = 0
# while True:
#     numero = int(input("Cual es el número secreto?"))
#     intentos = intentos+1
#     if numero == numero_secreto:
#         print("Acertaste!!!")
#         print(f'Numero de intentos {intentos}')
#     else:
#         if numero_secreto > numero:
#             print(f'El Numero secreto es mayor que {numero}')
#         else:
#             print(f'El Numero secreto es menor que {numero}')


# Challenger 1
# escribir programa que solicite ingresar 10 notas de alumnos y nos informe
# cuantos tienen notas mayores a o iguales a 17 y cuantos menores
# utilizar While

# notas_mayores_17 = 0
# notas_menores_17 = 0
# i = 1
# while i <= 10:
#     notas = float(input(f'ingrese la nota del alumno: {i}'))
#     if notas >= 17:
#         notas_mayores_17 = notas_mayores_17+1
#     else:
#         notas_menores_17 = notas_menores_17+1
#     i += 1
# print(
#     f'La cantidad de estudiantes con notas mayores a 17 puntos es: {notas_mayores_17}')
# print(
#     f'La cantidad de estudiantes con notas menores a 17 puntos es: {notas_menores_17}')


# Challenger2

"""
Hacer un programa que simule lo que debo pagar en una tienda online, me debe pedir el nombre del
producto su precio y cantidad podemos hacer n compras hasta que yo se le indique en el mensaje
que desea seguir comprando s/n

"""

acumulador_pago = 0
total_pago = 0
while True:
    producto = input("Ingrese el producto a comprar: ")
    precio = int(input("Ingrese el precio del producto: "))
    cantidad = int(input("ingrese la cantidad a comprar: "))
    acumulador_pago = cantidad * precio
    total_pago = total_pago + acumulador_pago
    msj = input("¿Desea seguir comprando? ( S / N )")
    if msj.upper() == "N":
        print(f'El total a pagar es: {total_pago}')
        break
