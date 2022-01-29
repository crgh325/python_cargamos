# for para

# for _ in range(10):
#     print("hola mundo")


# for x in range(10):
#    print(x, "hola mundo")

# for x in range(1, 10, 2):
#   print(x)


# while mientras

# i = 0
# while i <= 100:
#     print(i)
#     i = i+1

# contraseña = "python"
# while True:
#     con = input("Ingrese la contraseña:")
#     if con == contraseña:
#         print("Contraseña correcta")
#         break
#     else:
#         print("Contraseña errada")


contraseña = "python"
cont = 0
while True:
    con = input("Ingrese la contraseña:")
    if con == contraseña:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña errada")
        cont += 1
        if cont == 3:
            print("Supero los intentos permitidos, pruebe mas tarde")
            break
