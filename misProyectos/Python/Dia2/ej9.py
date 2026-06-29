precios = {"manzana":80, "naranja":70, "banana":50}
eleccionF=input("elije una fruta: ")
eleccionK=int(input("elije una cantidad de kilos: "))
precio= (precios[eleccionF])*eleccionK
print(f"El precio final es {precio}")
