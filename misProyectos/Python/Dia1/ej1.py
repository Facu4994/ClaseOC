try:
 cuenta = float(input("¿Cual es el total de la cuenta? "))
 porcentaje = int(input("¿Cual es el porcentaje que quiere dejar? "))
 propina = cuenta*porcentaje/100
 print(f"La cuenta es ${cuenta} y la propina es ${propina}")
except ValueError:
 print("Error, hay que poner numeros no letras")