import random
secreto= random.randint(1,10)
numeroelegido=int(input("elegi un numero"))
while numeroelegido != secreto:
    print("el numero dicho es incorrecto")
    if numeroelegido < secreto:
        print("El numero secreto es mayor")
    else:
        print("El numero secreto es menor")
    
    numeroelegido=int(input("Elegi un numero: "))

print(f"Adivinaste, el numero siempre fue {secreto}")

