try:
    num1 = float(input("Pon el primer numero "))
    num2 = float(input("Pon el numero que lo divide "))
    print("El resultado es", num1/num2)
except ValueError:
    print("No se puso el numero")
except ZeroDivisionError:
    print("No se puede dividir por cero")