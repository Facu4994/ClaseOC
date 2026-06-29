sumaTotal = 0
try:
    num = int(input("Ingrese el numero: "))
    while num != 0:
        sumaTotal += num
        num = int(input("Ingrese el numero: "))
    print(sumaTotal)
except ValueError:
    print("Error, hay que poner numeros")