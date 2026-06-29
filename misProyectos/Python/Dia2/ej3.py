try:
    num = int(input("elije un numero para multiplicar"))
    for i in range(1,11):
        print(f"{num}X{i}=", num*i)
except ValueError:
    print("Error, hay que poner numeros")