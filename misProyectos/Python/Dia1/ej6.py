try:
    gradosC = float(input("Coloca los grados celsius "))
    Fahrenheit = (gradosC*9/5)+32
    print(f"Los grados Fahrenheit son {Fahrenheit}")
except ValueError:
    print("Error al ingresar la temperatura")