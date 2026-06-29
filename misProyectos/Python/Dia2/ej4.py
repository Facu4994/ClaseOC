palabra = input("Ingrese una palabra: ")
cont =  0
for letras in palabra:
    if letras in "aeiouAEIOU":
        print(letras)
        cont += 1
print(cont)