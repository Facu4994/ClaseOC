def es_par(numero):
    if numero%2==0:
        return True
    else:
        return False
num = int(input("cual es tu numero"))
resultado = es_par(num)
print(resultado)