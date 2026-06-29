try:
    peso=float(input("cuanto pesas?"))
    altura=float(input("cuanto medis?"))
    IMC= peso/(altura*altura)
    print(f"tu IMC es {IMC}")
except ValueError:
    print("Error al ingresar el numero")
except ZeroDivisionError:
    print("No se puede dividir por 0")