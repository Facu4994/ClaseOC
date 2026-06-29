try:
    print("cuales fueron tu 3 notas en la materia?")
    nota1 =float(input())
    nota2=float(input())
    nota3=float(input())
    promedio=(nota1+nota2+nota3)/3
    print(f"tu promedio es {promedio}")
except ValueError:
    print("Ingreso incorrecto")