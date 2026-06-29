def contar_letras(palabra):
    letras=len(palabra)
    return letras 
palabra = input("ingrese una palabra: ")
print(f"tu palabra tiene {contar_letras(palabra)}")
