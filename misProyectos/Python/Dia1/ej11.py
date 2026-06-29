try:
    num1=float(input("pone un numero"))
    num2=float(input("pone otro numero"))
    if num1 < num2:
        print("el segundo numero es mayor")
    else:
        print("el primer numero es mayor")
except ValueError:
    print("Error al ingresar el numero")