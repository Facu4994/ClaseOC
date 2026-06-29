try:
    Htrabajadas=float(input("cuantas horas trabajas por dia?"))
    tarifaxhora=float(input("cuanto cobras por hora?"))
    salario=Htrabajadas*tarifaxhora
    print(f"tu salario es {salario} por dia")
except ValueError:
    print("Error, hay que poner numeros pa")