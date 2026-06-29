try:
    num = int(input("Ponga un numero "))
    if num > 0:
        print("El numero es positivo")
    elif num == 0:
        print("El numero es igual a 0")
    else:
        print("El numero es negativo")
except ValueError:
    print("Error al ingresar el numero")