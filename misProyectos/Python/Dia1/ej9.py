try:
    precio=float(input("cual es el valor del producto "))
    descuento=float(input("cuanto descuento tiene? "))
    preciofinal=precio-descuento*precio/100
    print(f"el monto descontado es {preciofinal}")
except ValueError:
    print("Error, hay que poner numeros")