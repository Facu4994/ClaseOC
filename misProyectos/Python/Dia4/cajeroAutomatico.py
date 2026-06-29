saldo = 1000
pinUsuario = "1234"
def verificarUsuario(pin):
    if pin == pinUsuario:
        pass
        return True
    else:
        return False
def retirar(monto):
    if monto <= saldo:
        saldoNuevo = saldo-monto
        print(f"Te queda de saldo ${saldoNuevo}")
        return saldoNuevo
    else:
        print("No puedes retirar esa cantidad")
print("🏦 Bienvenido al Banco de Python")
inputPin = input("Ingrese el PIN: ")
if verificarUsuario(inputPin):
    print(f"Acceso concedido, el saldo es ${saldo}")
    try:
        monto = float(input("Ingrese el monto a retirar: "))
        retirar(monto)
    except ValueError:
        print("Error al ingresar el monto")
else:
    print("PIN incorrecto, cuidate que te vamos a agarrar")