import random
palabraSecreta = ["julio","sabio", "libro", "resto"]
palabraElegida =random.choice(palabraSecreta)
palabraUsuario = input("Ingrese una palabra de 5 letras: ").lower()
cont = 0
while palabraUsuario != palabraElegida:
    print("Incorrecto")
    for i in palabraUsuario:
        if i in palabraElegida:
            cont = cont+1
    print(f"Hay {cont} letras correctas")
    palabraUsuario = input("Ingrese de nuevo la palabra: ").lower()
print(f"Palabra acertada, la palabra era {palabraElegida}")