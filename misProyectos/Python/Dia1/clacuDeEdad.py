añoNacimiento = int(input("En que año naciste?"))
añoActual = 2026
edad = añoActual - añoNacimiento
print(f"tu edad es {edad}")
if edad < 18:
    print("pero esos menor de edad y no podes tomar vino")
else:
    print("sos mayor de edad toma mi vino blanco")