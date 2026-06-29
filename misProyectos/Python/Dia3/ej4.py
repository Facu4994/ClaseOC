def numeros(num1, num2, num3):
    if num1>num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
numuno = int(input("el primer num es?"))
numdos = int(input("el segundo es?"))
numtres = int(input("y el tercero?"))
numMayor=numeros(numuno,numdos,numtres)
print(f"el num mayor es: {numMayor}")