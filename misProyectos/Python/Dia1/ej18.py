numSecret=9
try:
    numSelec= int(input("elige un numero del 1 al 10"))
    if numSelec==numSecret:
        "adivinaste"
    else:
        "no adivinaste"
except ValueError:
    print("Error al ingresar el numero")