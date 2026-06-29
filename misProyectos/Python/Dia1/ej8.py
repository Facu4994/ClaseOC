try:
    dias = int(input("Pon los dias "))
    segundos = dias*24*60*60
    print(f"La cantidad de segundos son {segundos}")
except ValueError:
    print("Error al poner los dias")