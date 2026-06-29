selecUsuario=input("seleciona tijera, piedra o papel").lower()
print("el programa eligio piedra")
if selecUsuario=="tijera":
    print("perdiste, piedra rompe tijera")
if selecUsuario=="papel":
    print("ganaste, papel envuelve piedra")
elif selecUsuario == "piedra":
    print("empate, las piedras se rompen entre si")