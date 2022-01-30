
# creando la fumcion
def saludo():
    print("Hola esto es una funcion")

# Pasando parametros a la funcion


def funcion_parametros(a, b):
    print(f'este es el valos de A: {a} y el valor de B: {b} ')


# funcion con valores por defecto
def mensaje(nombre, mensaje="Adios"):
    #saludo = mensaje + " " + nombre
    print(f'saludo {nombre} {mensaje}')

# funcion con valores indefinidos(listas)


def saluda(*nombres):
    for item in nombres:
        print(item)


#saluda("phyton", "javascrit", "flask", "djandgo", "css", "html")


def elementos(**params):
    for key in params:
        print(key, params[key])


elementos(ciudad="Tijuana", pais="Mexico")


# invocando a la funcion
# saludo()
#funcion_parametros(12, 34)
# mensaje("Cris")
