def conversor(celsius):
    resultado = celsius * 9/5 + 32
    print(f"El resultado es {resultado} F")
    return resultado
temperatura = float(input("Cuanto hay de temperatura? "))
conversor(temperatura)