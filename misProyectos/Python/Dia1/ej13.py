try:
    nota=float(input("cual es tu nota?"))
    if nota < 6:
        print("estas desaprobado")
    else:
        print("estas aprobado")
except ValueError:
    print("Error al ingresar la nota")