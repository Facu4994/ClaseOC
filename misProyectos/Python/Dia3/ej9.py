def crearMail(nombre,apellido):
    gmail = f"{nombre}.{apellido}@empresa.com"
    print(f"El gmail es: {gmail}")
    return gmail
nombre = input("Ingrese el nombre: ").lower()
apellido = input("Ingrese el apellido: ").lower()
crearMail(nombre,apellido)