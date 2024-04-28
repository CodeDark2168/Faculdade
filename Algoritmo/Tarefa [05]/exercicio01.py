import math

print("==============================")
x1 = float(input("Informe o valor de x1: "))
x2 = float(input("Informe o valor de x2: "))
y1 = float(input("Informe o valor de y1: "))
y2 = float(input("Informe o valor de y2: "))
calculo = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("O resultado do cálculo é " + str(round(calculo, 2)))
print("==============================")