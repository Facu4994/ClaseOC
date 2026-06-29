def puede_votar(edad):
    if edad>=18:
        return "puede votar"
    else:
        return "no puede votar"

EDAD=int(input("ingresa tu edad "))
puede=puede_votar(EDAD)
print(f"como tiene {EDAD}, {puede_votar(EDAD)}")

