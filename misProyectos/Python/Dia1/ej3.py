try:
 dolar = int(input("cuantos dolares tenes?"))
 pesos =dolar*1500
 print(f"estos dolares valen ${pesos} pesos")
except ValueError:
 print("Error, hay que poner numeros no letras")