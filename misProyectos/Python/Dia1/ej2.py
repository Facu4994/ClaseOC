try:
 num = int(input("Ponga un numero "))
 if num%2 == 0:
    print("Tu numero es par")
 else:
    print("Tu numero es impar")
except ValueError:
 print("Error, hay que poner numeros no letras")