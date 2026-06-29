try:
    altura=int(input("cuantos cm tiene tu rectangulo de altura? "))
    base=int(input("y la la base? "))
    area=altura*base
    print(f"el area de tu rectangulo o cuadrado es {area} cm cuadrados")
except ValueError:
    print("Ingrese numeros, no letras")