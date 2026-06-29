def minutos_a_horas(minutos):
    horas = minutos//60
    restominutos = minutos%60
    print(f"Son {horas} horas y {restominutos} minutos")
min = int(input("Ingrese los minutos: "))
minutos_a_horas(min)