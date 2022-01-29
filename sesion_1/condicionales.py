# num1 = int(input("ingrese numero1: "))
# num2 = int(input("ingrese numero2: "))

# if num1 > num2:
#     print("El numero mayor es", num1)
# elif num1 == num2:
#     print("Los numero son iguales")
# else:
#     print("El numero mayor es", num2)


candidato = input("Elija su candidato:")
if candidato.upper() == "A" or candidato.upper() == "D":
    print("Usted voto por el partido Rojo")
elif candidato.upper() == "B":
    print("Usted voto por el partido Azul")
elif candidato.upper() == "C":
    print("Usted voto por el partido Verde")
else:
    print("Opcion errada")
