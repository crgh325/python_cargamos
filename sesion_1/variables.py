# comentario de una linea


"""
comentario en
varias lineas

"""

# Reglas para definir variables
# snake_case (con guion bajo y todo en minuscula)

# import keyword
# edad = 28  # tipo entero
# nombre = "cristian"  # tipo streang
# precio = 25.7  # tipo float
# estado = True  # tipo bool

"""
print(type(edad)) #int
print(type(nombre)) #str
print(type(precio)) #float
print(type(estado)) #bool
"""

# colecciones
"""
lista_cursos = ["python", "flask", "django"]  # list
sueldo = (199, 1700, 1850)  # tuple #inmutable
empleados = {'codigo': 'a100', 'codigo': 'a200'}  # dict
print(type(lista_cursos))
print(type(sueldo))
print(type(empleados))
"""

# palabras reservadas
# print(keyword.kwlist)


# conversion de datos
"""
valor = "234"
valor2 = 100
valor3 = 295.16

print(type(int(valor)))
print(type(float(valor2)))
print(type(str(valor3)))
"""

# ejercicios practicos
# calcular peso de un objeto

# masa = 75
# gravedad = 9.81
# peso = masa*gravedad
# print(peso)

# promedio de notas
# funcion input .  permite ingresar valores por consola
# nom_alum = input("Ingrese el nombre de un alumno:")
# nota_uno = float(input("Ingrese Nota1:"))
# nota_dos = float(input("Ingrese Nota2:"))
# promedio = (nota_uno+nota_dos)/2

# tipos de concatenacion
# print("El promedio es: "+str(promedio))
# print("El promedio es: ", promedio)
# print("El promedio del alumno {} es: {}".format(nom_alum, promedio))  # forma pythonica

# operadores matematicos
# print(2+2)  # 4
# print(4*8)  # 32
# print(5/3)  # 1.666666
#operacion = 5/3
# print(5//3)  # 1
# print(23 % 2)  # 1 residuo de la division

# print("El valor formateado es: %.2f" % operacion)  # redondear


# operadores logicos
# " > Mayor "
# " < Menor"""
# " >= Mayor Igual"
# " <= Menor Igual"
# " != Diferente"
# " == " Igual
# " and " y
# "or " o
# "not " negacion

# LO QUE SE INGRESA POR POR PANTALLA LO TOMA COMO STR

# ejercicio
# pizza = int(input("Hola, ¿cuantas rebanadas de pizza has traido...?"))
# comidas = int(input("¿Y cuantas rebanadas se comieron...?"))
# print(
#     f'Si trajiste {pizza} rebanadas de pizza y se comieron {comidas}, quedan {pizza - comidas}')


# Separadores y tabuladores y saltos de linea

#print("hola", "mundo", sep='<->')

# elimina los saltos de linea
#print("hola", end="")
# print("mundo")

print("salto de linea. viene un salto \n\n")
print("\t tabulador \n\n")
print("comillas .Comillas dentro :\"Hola\" ")
