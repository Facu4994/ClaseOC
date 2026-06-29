def calcular_precio_final(precio, descuento):
  resultado = precio-precio*descuento/100
  print(resultado)
  return resultado
num=float(input("ingrese el precio: "))
num2=int(input("ingrese el descuento: "))
calcular_precio_final(num,num2)